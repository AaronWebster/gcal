# Copyright 2020 Aaron Webster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pickle
import sys
import os

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from collections.abc import Sequence

from absl import app
from absl import flags
from absl import logging

CONFIG_DIR = os.path.join(os.getenv('HOME'), '.config', 'gcal')
TOKEN_FILE = os.path.join(CONFIG_DIR, 'token.pickle')
CREDENTIALS_FILE = os.path.join(CONFIG_DIR, 'credentials.json')
CALENDAR_ID_FILE = os.path.join(CONFIG_DIR, 'default_calendar.pickle')


def main(argv: Sequence[str]) -> None:
  if not os.path.exists(CONFIG_DIR):
    os.mkdir(CONFIG_DIR)
    logging.info('Created config directory %s' % CONFIG_DIR)

  if os.path.exists(CALENDAR_ID_FILE):
    with open(CALENDAR_ID_FILE, 'rb') as f:
      calendar_id = pickle.load(f)
  else:
    calendar_id = input('Default calendar ID: ')

    with open(CALENDAR_ID_FILE, 'wb') as f:
      pickle.dump(calendar_id, f)

    logging.info('Calendar ID %s written to %s' %
                 (calendar_id, CALENDAR_ID_FILE))

  if not os.path.exists(CREDENTIALS_FILE):
    logging.fatal(
        'No credentials found.  Download credentials from '
        'https://console.cloud.google.com/apis/credentials and save to %s.' %
        CREDENTIALS_FILE)

  creds = None
  if os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, 'rb') as f:
      creds = pickle.load(f)

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, [
          'https://www.googleapis.com/auth/calendar.events',
          'https://www.googleapis.com/auth/calendar'
      ])
      creds = flow.run_local_server(port=33045)

    with open(TOKEN_FILE, 'wb') as f:
      pickle.dump(creds, f)

  if len(argv) < 2:
    print('Missing required calendar event description.')
    sys.exit()

  service = build('calendar', 'v3', credentials=creds, cache_discovery=False)
  created_event = service.events().quickAdd(calendarId=calendar_id,
                                            text=' '.join(
                                                sys.argv[1:])).execute()

  if created_event['status'] != 'confirmed':
    logging.fatal('Could not create event: %s' % created_event['status'])
  else:
    print('Event successfuly created %s' % created_event['htmlLink'])


if __name__ == '__main__':
  app.run(main)

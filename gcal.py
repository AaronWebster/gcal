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

from __future__ import print_function
import pickle
import sys
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from absl import app
from absl import flags
from absl import logging

FLAGS = flags.FLAGS

flags.DEFINE_string('default_calendar', None, 'Set default calendar.')
flags.DEFINE_bool('reset_credentials', False, 'Reset credentials.')

CONFIG_DIR = os.path.join(os.getenv('HOME'), '.gcal')
TOKEN_FILE = os.path.join(CONFIG_DIR, 'token.pickle')
CREDENTIALS_FILE = os.path.join(CONFIG_DIR, 'credentials.json')
DEFAULT_CALENDAR_FILE = os.path.join(CONFIG_DIR, 'default_calendar.pickle')


def main(argv):
  if not os.path.exists(CONFIG_DIR):
    os.mkdir(CONFIG_DIR)

  if FLAGS.default_calendar:
    with open(DEFAULT_CALENDAR_FILE, 'wb') as f:
      pickle.dump(FLAGS.default_calendar, f)
    logging.info('Default calendar set to %s', FLAGS.default_calendar)
    sys.exit()

  if FLAGS.reset_credentials:
    logging.info('Resetting credentials.')
    for f in (TOKEN_FILE, CREDENTIALS_FILE):
      if os.path.exists(f):
        os.remove(f)

  calendar_id = None
  if not os.path.exists(DEFAULT_CALENDAR_FILE):
    logging.info(
        'Default calendar not set.  Use --default_calendar to specify.')
    sys.exit(-1)
  else:
    with open(DEFAULT_CALENDAR_FILE, 'rb') as f:
      calendar_id = pickle.load(f)

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

  service = build('calendar', 'v3', credentials=creds, cache_discovery=False)
  created_event = service.events().quickAdd(
      calendarId=calendar_id, text=' '.join(sys.argv[1:])).execute()

  if created_event['status'] != 'confirmed':
    logging.info('Error creating event: %s', created_event['status'])
  else:
    logging.info('Event successfuly created %s', created_event['htmlLink'])


if __name__ == '__main__':
  app.run(main)

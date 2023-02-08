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

load(
    "@pypi//:requirements.bzl",
    "data_requirement",
    "dist_info_requirement",
    "entry_point",
)
load("@subpar//:subpar.bzl", "par_binary")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)

py_binary(
    name = "gcal",
    srcs = ["gcal.py"],
    visibility = ["//visibility:public"],
    deps = [
        "@pypi_absl_py//:pkg",
        "@pypi_google_api_python_client//:pkg",
        "@pypi_google_auth_oauthlib//:pkg",
        "@pypi_protobuf//:pkg",
    ],
)

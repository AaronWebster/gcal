workspace(name = "com_webster_gcal")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_python",
    commit = "cd552725122fdfe06a72864e21a92b5093a1857d",
    remote = "https://github.com/bazelbuild/rules_python.git",
    shallow_since = "1593046824 -0700",
)

git_repository(
    name = "com_google_absl",
    branch = "master",
    remote = "https://github.com/abseil/abseil-py",
)

git_repository(
    name = "subpar",
    commit = "9fae6b63cfeace2e0fb93c9c1ebdc28d3991b16f",
    remote = "https://github.com/google/subpar",
    shallow_since = "1565833028 -0400",
)

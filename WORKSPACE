workspace(name = "com_webster_gcal")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "cd552725122fdfe06a72864e21a92b5093a1857d", 
    shallow_since = "1593046824 -0700"
)

git_repository(
    name = "com_google_absl",
    branch = "master",
    remote = "https://github.com/abseil/abseil-py",
)

git_repository(
    name = "subpar",
    branch = "master",
    remote = "https://github.com/google/subpar",
)

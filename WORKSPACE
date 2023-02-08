workspace(name = "com_webster_gcal")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "subpar",
    branch = "master",
    remote = "https://github.com/google/subpar",
)

git_repository(
    name = "rules_python",
    commit = "6c8ae765564b27f202b12700e4cc91ed494bd82c",
    remote = "https://github.com/bazelbuild/rules_python.git",
    shallow_since = "1675874017 -0800",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")

py_repositories()

python_register_toolchains(
    name = "python310",
    python_version = "3.10",
)

load("@python310//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pypi",
    python_interpreter_target = interpreter,
    requirements_lock = "//:requirements_lock.txt",
)

load("@pypi//:requirements.bzl", "install_deps")

install_deps()

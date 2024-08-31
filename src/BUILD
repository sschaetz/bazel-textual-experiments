load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")

py_binary(
    name = "example",
    srcs = ["example.py"],
    deps = [
        "@pip//textual",
    ],
)

pkg_tar(
    name = "example_tar",
    srcs = [
        ":example",
    ],
    include_runfiles = True,
)

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

py_binary(
    name = "example_no_ui",
    srcs = ["example_no_ui.py"],
    deps = [
        "@pip//numpy",
        "@rules_python//python/runfiles",
    ],
    data = [
        "data.txt",
    ]
)

pkg_tar(
    name = "example_no_ui_tar",
    srcs = [
        ":example_no_ui",
    ],
    include_runfiles = True,
)

load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@rules_proto//proto:defs.bzl", "proto_library")
load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_python//python:proto.bzl", "py_proto_library")

load("@rules_python//python/entry_points:py_console_script_binary.bzl", "py_console_script_binary")

# This is how you can define a `pylint` entrypoint which uses the default python version.
py_console_script_binary(
    name = "textual",
    pkg = "@pip//textual_dev",
    visibility = ["//entry_points:__subpackages__"],
)

proto_library(
    name = "api_proto",
    srcs = ["api.proto"],
)

py_proto_library(
    name = "api_py_proto",
    visibility = ["//visibility:public"],
    deps = [":api_proto"],
)

py_binary(
    name = "example",
    srcs = ["example.py"],
    deps = [
        "@pip//textual",
        "@pip//textual_dev",
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
        ":api_py_proto",
    ],
    data = [
        "data.txt",
        "api_example.pb.txt",
    ]
)

pkg_tar(
    name = "example_no_ui_tar",
    srcs = [
        ":example_no_ui",
    ],
    include_runfiles = True,
)

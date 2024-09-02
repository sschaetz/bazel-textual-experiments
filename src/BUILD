load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@rules_proto//proto:defs.bzl", "proto_library")
load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_python//python:proto.bzl", "py_proto_library")
load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")
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

pybind_extension(
    name = "cpp_example",
    srcs = ["cpp_example.cc"],
)

sh_binary(
    name = "sh_example",
    srcs = ["sh_example.sh"],
)

EXAMPLE_DATA_DEPS = [
    "example.tcss",
    ":cpp_example",
    "data.txt",
    "api_example.pb.txt",
    "sh_example",
]

py_console_script_binary(
    name = "example_dev",
    pkg = "@pip//textual_dev",
    script = "textual",
    visibility = ["//entry_points:__subpackages__"],
    data = EXAMPLE_DATA_DEPS,
)

py_binary(
    name = "example",
    srcs = ["example.py"],
    deps = [
        "@pip//textual",
        "@pip//textual_dev",
        "@rules_python//python/runfiles",
    ],
    data = EXAMPLE_DATA_DEPS,
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
    data = EXAMPLE_DATA_DEPS, 
)

pkg_tar(
    name = "example_no_ui_tar",
    srcs = [
        ":example_no_ui",
    ],
    include_runfiles = True,
)

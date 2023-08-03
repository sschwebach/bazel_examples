load("@rules_python//python:py_library.bzl", "py_library")
load("@rules_python//python:py_binary.bzl", "py_binary")

py_library(
    name = "dino",
    srcs = ["dino.py"],
    srcs_version = "PY3",
)

py_binary(
    name = "dino_roar",
    srcs = ["dino_roar.py"],
    srcs_version = "PY3",
    deps = [":dino"],
)

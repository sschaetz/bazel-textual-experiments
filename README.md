# Experiments with Bazel and Textual 💚 💻

[Textual](https://github.com/Textualize/textual) is a nice TUI library for Python. Maybe we can convince [bazel](https://bazel.build/)
to work with it and maybe we can even generate executable packages for different platforms.

## Requirements

The only thing needed should be [bazelisk](https://github.com/bazelbuild/bazelisk) and a system Python (which is used for bootstraping only).

## How to Run

```bash
bazel run //src:example  
```

## How to Debug

Run in 2 terminals, in the debug terminal we see the app events, in the app
terminal we see the app itself and can interact with it:

```bash
# debug terminal:
bazel run //src:textual -- console
```

```bash
# app terminal:
bazel run //src:example --run_under "//src:textual -- run --dev"
```

## TODO 

- [x] use bzlmod to install python and python deps
- [x ] textual dev flow
- [x] platforms
  - [x] Linux
  - [x] Mac
  - [x] Windows
- [x] cross-platform
  - [x] update requirements 
  - [x] build cross platform
- [x] packaging

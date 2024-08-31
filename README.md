# Experiments with Bazel and Textual 💚 💻

## Requirements

The only thing needed should be [bazelisk](https://github.com/bazelbuild/bazelisk) and a system Python (which is used for bootstraping only).

## How to Run

```bash
bazel run //src:example  
```

## TODO 

- [x] use bzlmod to install python and python deps
- [ ] textual dev flow
- [ ] platforms
  - [ ] Linux
  - [x] Mac
  - [ ] Windows
- [ ] cross-platform
  - [ ] update requirements 
  - [ ] build cross platform
- [ ] packaging

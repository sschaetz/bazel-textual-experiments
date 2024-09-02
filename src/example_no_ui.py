import sys
import numpy as np
from pathlib import Path
from src.api_pb2 import ExampleMessage
from google.protobuf import text_format

# This should really be 
# `from rules_python.python.runfiles import runfiles`
# but: https://github.com/bazelbuild/rules_python/issues/1679
from python.runfiles import runfiles
from src.cpp_example import mul as cpp_mul

def run():
    interpreter_path = sys.executable
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"Python Interpreter: {interpreter_path}\nPython Version: {python_version}")

    # Make sure numpy is working.
    assert np.isclose(1.0 + 41.0, 42.0)
    
    # Load a runfile:
    r = runfiles.Create()
    rfile = Path(r.Rlocation("_main/src/data.txt"))
    assert "Test File" == rfile.read_text()

    # Load a text protobuf:
    proto_file_path = r.Rlocation("_main/src/api_example.pb.txt")
    with open(proto_file_path, 'r') as proto_file:
        proto_content = proto_file.read()
    
    example_message = ExampleMessage()
    text_format.Parse(proto_content, example_message)
    assert example_message.index == 42

    # Test pybind11
    assert cpp_mul(3, 11) == 33

    # Test running shell script
    import subprocess

    # Get the path to the shell script using runfiles
    sh_script_path = r.Rlocation("_main/src/sh_example.sh")

    # Run the shell script using subprocess
    result = subprocess.run([sh_script_path], capture_output=True, text=True)

    # Check if the script ran successfully
    if result.returncode != 0:
        print(f"Shell script failed with return code {result.returncode}")
        print(f"Error output: {result.stderr}")
        return False

    print(f"Shell script output: {result.stdout}")

    return True

if __name__ == "__main__":
    if not run():
        print("Failed to run example!")
        exit(1)
    print("Success!")
    exit(0)
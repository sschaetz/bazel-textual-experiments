import sys
import numpy as np
from pathlib import Path

# This should really be 
# `from rules_python.python.runfiles import runfiles`
# but: https://github.com/bazelbuild/rules_python/issues/1679
from python.runfiles import runfiles

def run():
    # Make sure numpy is working.
    assert np.isclose(1.0 + 41.0, 42.0)
    
    # Load a runfile:
    r = runfiles.Create()
    rfile = Path(r.Rlocation("_main/src/data.txt"))
    assert "Test File" == rfile.read_text()

    interpreter_path = sys.executable
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"Python Interpreter: {interpreter_path}\nPython Version: {python_version}")
    return True
    
if __name__ == "__main__":
    if not run():
        print("Failed to run example!")
        exit(1)
    print("Success!")
    exit(0)
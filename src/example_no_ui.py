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


if __name__ == "__main__":
    if not run():
        exit(1)
    exit(0)
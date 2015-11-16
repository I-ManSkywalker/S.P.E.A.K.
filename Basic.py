import os
import sys
import runpy
script_path = os.path.join(os.path.dirname(__file__), os.pardir, "jasper.py")
sys.path.remove(os.path.dirname(__file__))
sys.path.insert(0, os.path.dirname(script_path))
runpy.run_path(script_path, run_name="__main__")

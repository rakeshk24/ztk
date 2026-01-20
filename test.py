import sys

def is_in_venv():
    # sys.prefix points to the venv, sys.base_prefix points to the system Python
    return sys.prefix != sys.base_prefix

if is_in_venv():
    print("Running in a virtual environment!")
else:
    print("Running at the global level.")
import sys
from pathlib import Path


def run_core():
    rute_absolute = str(Path(__file__).resolve().parent)

    if str(rute_absolute) not in sys.path:
        sys.path.insert(0, str(rute_absolute))

    from .manage import main

    main()


if __name__ == "__main__":
    run_core()

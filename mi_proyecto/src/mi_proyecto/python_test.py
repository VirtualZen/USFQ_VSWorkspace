import sys


def main():
    print()
    print("START PROGRAM RUN")
    print("Python is running")
    print("Version:", sys.version.replace("\n", " "))
    print("Executable:", sys.executable)
    # simple sanity check
    if 1 + 1 != 2:
        raise SystemExit("Basic arithmetic failed")
    else:
        print("Basic arithmetic passed")
    print("END PROGRAM RUN")
    print()


if __name__ == "__main__":
    main()

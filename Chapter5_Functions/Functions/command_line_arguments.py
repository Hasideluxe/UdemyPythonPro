import sys


def main():
    print(len(sys.argv))
    print(sys.argv)
    # User-defined command-line arguments
    for arg in sys.argv[1:]:
        print(arg, type(arg))

    for arg in sys.argv[1:]:
        arg_name, arg_val = arg.split('=')
        is_number = arg_val.isdigit()
        if is_number:
            arg_val = int(arg_val)
        print(arg_name, arg_val, type(arg_val))


if __name__ == "__main__":
    main()

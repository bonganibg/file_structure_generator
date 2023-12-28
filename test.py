import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default='input.txt')
    parser.add_argument("-n", "--name", help="Name of the person")

    args = parser.parse_args()

    print(args.input)
    print(args.name)


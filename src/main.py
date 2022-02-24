from parsing import Parsing
import sys

def main() -> int:
    parsing = Parsing(sys.argv[1])

    parsing.parse()
    return 0

if __name__ == '__main__':
    main()
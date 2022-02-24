from parsing import Parsing
from algo import sort, algo
import sys

def main() -> int:
    parsing = Parsing(sys.argv[1])

    parsing.parse()

    algo(parsing.projects, parsing.contributors)

    return 0

if __name__ == '__main__':
    main()
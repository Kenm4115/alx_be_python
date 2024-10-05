
import sys
from robust_division_calculator import safe_divide


def main():
    # Check if there are enough command line arguments
    if len(sys.argv) != 3:
        print("Usage: main.py <numerator> <denominator>")
        return

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function and print the result
    result = safe_divide(numerator, denominator)
    print(result)


if __name__ == "__main__":
    main()

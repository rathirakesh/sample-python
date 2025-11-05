#!/usr/bin/env python3
"""
Example script with simple logic.
"""

from utils import add_two_numbers


def main():
    """Add two numbers example."""
    num1 = 10
    num2 = 20
    result = add_two_numbers(num1, num2)
    print(f"{num1} + {num2} = {result}")


if __name__ == "__main__":
    main()


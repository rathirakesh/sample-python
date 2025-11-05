#!/usr/bin/env python3
"""
Main entry point for the sample Python project.
"""

from utils import add_two_numbers


def main():
    """Main function to add two numbers."""
    num1 = 5
    num2 = 3
    result = add_two_numbers(num1, num2)
    print(f"{num1} + {num2} = {result}")


if __name__ == "__main__":
    main()


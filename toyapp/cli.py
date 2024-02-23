"""Console script for toyapp."""

import sys

import click

from toyapp.toyapp import math_func


@click.command()
@click.argument("num1", type=click.FLOAT)
@click.argument("num2", type=click.FLOAT)
@click.argument("operation", default="+", type=click.STRING)
def main(num1: float, num2: float, operation: str):
    """Perform simple arithmetic operations given two numbers and an operator.

    If operator is ommited, the default is addition.
    To prevent * being interpreted as a wildcard, use quotes around the operator.

    num1: float - The first number
    num2: float - The second number
    operation: str - The operation to perform on the two numbers

    Evaluates the expression num1 operation num2 and prints the result.
    """
    answer = math_func(num1, num2, operation)
    print(f"\n\tThe answer to {num1} {operation} {num2} = {answer:.2f}\n")

    return float(answer)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

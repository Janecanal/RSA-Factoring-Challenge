#!/usr/bin/python3

import sys

def factors(n):
  """Factors the given number n into a product of two smaller numbers.

  Args:
    n: The number to factor.

  Returns:
    A tuple of two numbers (p, q) such that n = p * q, or None if n is prime.
  """

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return (i, n // i)
  return None

def main():
  """Reads the numbers from the given file and factors them."""

  file_name = sys.argv[1]
  with open(file_name, "r") as f:
    for line in f:
      n = int(line)
      factorization = factors(n)
      if factorization is not None:
        print(f"{n}={factorization[0]}*{factorization[1]}")

if __name__ == "__main__":
  main()

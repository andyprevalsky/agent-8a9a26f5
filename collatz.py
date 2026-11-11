"""Compute and print the Collatz sequence starting at 27."""

START = 27
MAX_ITERATIONS = 10_000  # safety bound so the loop is guaranteed to terminate


def collatz(n):
    """Return the Collatz sequence from n down to 1, inclusive."""
    if n < 1:
        raise ValueError("start must be a positive integer")
    sequence = [n]
    while n != 1:
        if len(sequence) > MAX_ITERATIONS:
            raise RuntimeError("sequence did not reach 1 within the iteration bound")
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(START)
    steps = len(sequence) - 1  # transitions between terms, not the number of terms
    for value in sequence:
        print(value)
    print(f"Total steps: {steps}")


if __name__ == "__main__":
    main()

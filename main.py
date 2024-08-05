from typing import Dict


def print_substituted_numbers(start: int, end: int, mappings: Dict[int, str]) -> None:
    """
    Print substituted numbers with substitutions based on the given mappings.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
        mappings (Dict[int, str]): A dictionary where keys are divisors and values are the corresponding substitution strings.

    Example:
        >>> mappings = {2: "Two", 3: "Three"}
        >>> print_substituted_numbers(1, 6, mappings)
        1 Two Three Two 5 TwoThree
    """
    for i in range(start, end + 1):
        output = ""
        for divisor, word in mappings.items():
            if i % divisor == 0:
                output += word
        print(output if output else i)


if __name__ == "__main__":
    print_substituted_numbers(start=1, end=100, mappings={3: "Three", 5: "Five"})

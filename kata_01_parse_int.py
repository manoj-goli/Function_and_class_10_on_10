"""
kata_01_parse_int.py

Goal:
- Implement parse_int(s: str, *, base: int = 10) -> int
- Run this file and make the tests pass.

How to run (PowerShell):
  python .\kata_01_parse_int.py

Notes:
- Type hints like `-> int` or `s: str` are NOT enforced automatically by Python.
  They help humans + IDEs, and tools like mypy.
- The `*` in the function signature means `base` is keyword-only:
    parse_int("ff", 16)   ❌ (not allowed)
    parse_int("ff", base=16) ✅
"""

# -----------------------------
# Exercise 1: parse_int
# -----------------------------

def parse_int(s: str, *, base: int = 10) -> int:


    if base < 2 or base > 36:
        raise ValueError("base must be between 2 and 36 inclusive")

    s2= s.strip()
    if s2 == "":
        raise ValueError("input string is empty or whitespace only")
    return int(s2, base)
    """
    Parse s into an int with the given base.

    Requirements:
    1) Leading/trailing whitespace allowed
       - "  42 " -> 42

    2) '+' and '-' allowed
       - "-17" -> -17
       - "+17" -> 17

    3) Raise ValueError for invalid strings
       - "12.3", "abc", "", "   " must raise ValueError

    4) base must be between 2 and 36 inclusive
       - otherwise raise ValueError

    Hints (not the answer):
    - Use s.strip()
    - int("ff", 16) == 255
    - int() already handles + and -
    """

    # TODO 1: Validate base range (2..36). If invalid, raise ValueError.

    # TODO 2: Strip whitespace: s2 = s.strip()

    # TODO 3: If s2 is empty after stripping, raise ValueError.

    # TODO 4: Convert using int(s2, base). If it's invalid, int() will raise ValueError.

    raise NotImplementedError  # remove this after implementing


# -----------------------------
# Tiny test helper
# -----------------------------

class TestFailure(Exception):
    pass

def test_1() -> None:
    assert parse_int("  42 ") == 42
    assert parse_int("-17") == -17
    assert parse_int("+17") == 17
    assert parse_int("ff", base=16) == 255

    try:
        parse_int("12.3")
        raise TestFailure("expected ValueError for '12.3'")
    except ValueError:
        pass

    try:
        parse_int("   ")
        raise TestFailure("expected ValueError for whitespace-only string")
    except ValueError:
        pass

    try:
        parse_int("10", base=1)
        raise TestFailure("expected ValueError for base=1")
    except ValueError:
        pass


def main() -> None:
    print("Running kata 01...")
    test_1()
    print("✅ All tests passed for kata 01!")


if __name__ == "__main__":
    main()

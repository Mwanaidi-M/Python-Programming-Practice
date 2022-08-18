def number(lines):
    """
    Your team is writing a fancy new text editor, and you've been tasked with
    implementing the line numbering.

    Write a function which takes a list of strings and returns each line prepended by the correct number.

    The numbering starts at 1. The format is n: string. Notice the colon and space in between.

    Examples: (Input --> Output)

    [] --> []
    ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
    Args:
        lines: <list>

    Returns:
        new_lines: <list>
    """

    new_lines = []

    for line in range(len(lines)):
        new_lines.append(f"{line + 1}: {lines[line]}")

    print(new_lines)


number([" ", "b", " ", " ", " "])

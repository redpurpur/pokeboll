from typing import List


def levenshtein_distance(s1: str, s2: str):
    """
    Count distance between two strings with two matrix rows, which swapped one by one
    """
    if s1 == s2:
        return 0

    if len(s1) == 0:
        return len(s2)

    if len(s2) == 0:
        return len(s1)

    row_calculated: List[int] = list()
    row_current: List[int] = list()
    for i in range(len(s2) + 1):
        row_calculated.append(i)  # cost of insertion symbol
        row_current.append(0)

    for i in range(len(s1)):
        row_current[0] = i + 1  # cost of deletion symbol

        for j in range(len(s2)):
            row_current[j + 1] = min(
                row_current[j] + 1,  # cost of deletion
                row_calculated[j + 1] + 1,  # cost of insertion
                row_calculated[j] + int(bool(s1[i] != s2[j])),  # cost of replacement
            )

        row_calculated = list(row_current)

    distance = row_current[len(s2)]
    return distance

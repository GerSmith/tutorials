#! python
# -*- coding: utf-8 -*-

"""Task from Codewars."""


def number(lines):
    """Test 1-2-3."""
    # return [(str(i + 1) + ': ' + v) for i, v in enumerate(lines)]
    return ['%d: %s' % v for v in enumerate(lines, 1)]


print(number([]))  # []
print(number(["a", "b", "c"]))  # ["1: a", "2: b", "3: c"]

#! python
# -*- coding: utf-8 -*-

"""Task from Codewars."""


def solution(s: str):
    """Break CamelCase."""
    # ans = ''
    # for i in s:
    #     if i.isupper():
    #         ans = ans + ' ' + i
    #     else:
    #         ans += i
    # return ans
    return ''.join(i if i.islower() else (' ' + i) for i in s)


print(solution("helloWorld"))  # "hello World"
print(solution("camelCase"))  # "camel Case"
print(solution("breakCamelCase"))  # "break Camel Case"

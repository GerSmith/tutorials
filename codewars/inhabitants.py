#! python
# -*- coding: utf-8 -*-

"""Task from Codewars."""


def nb_year(p0, percent, aug, p):
    """Growth of a Population."""
    count, inhabitants = 0, p0
    while inhabitants < p:
        inhabitants = int(inhabitants + inhabitants * percent * 0.01 + aug)
        count += 1
        print(inhabitants, count)
    # print(count)
    return count


nb_year(1000, 2, 50, 1200)
# nb_year(1500, 5, 100, 5000)
# nb_year(1500000, 2.5, 10000, 2000000)
# nb_year(1500000, 0.25, 1000, 2000000)

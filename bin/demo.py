#!/usr/bin/env python3
"""
    fields=None,
    title=None,
    date_fmt=None,
    cols=80,
    prefix_every_line=True,
    orientation='horizontal'):
"""
import re
import os
import sys

from barchart import BarChart


def demo_a(size):

    bc = BarChart()

    print('-' * size.columns)
    print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))


def demo_b(size):

    bc = BarChart(
        fields = ['a', 'b'],
    )

    print('-' * size.columns)
    print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))


def main():

    size = os.get_terminal_size()

    demo_a(size)

    demo_b(size)

    return 0


if __name__ == '__main__':
    sys.exit(main())

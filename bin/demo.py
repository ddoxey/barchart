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


def demo(size):

    bc = BarChart()

    print('-' * size.columns)
    print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))


def demo_fields(size):

    bc = BarChart(
        fields = ['a', 'b']
    )

    print('-' * size.columns)
    print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))


def demo_title(size):

    bc = BarChart(
        title = 'Example'
    )

    print('-' * size.columns)
    print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))


def demo_date(size):

    bc = BarChart(
        date_fmt = '[%D]'
    )

    print('-' * size.columns)
    print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))


def demo_prefix(size):

    bc = BarChart(
        date_fmt = '[%D]',
        prefix_every_line = False
    )

    print('-' * size.columns)
    print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))


def demo_cols(size):

    bc = BarChart(
        cols = 60
    )

    print('-' * size.columns)
    print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))


def demo_orientation(size):

    bc = BarChart(
        orientation = 'vertical',
        cols = 20
    )

    print('-' * size.columns)
    print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))


def main():

    size = os.get_terminal_size()

    demo(size)

    demo_fields(size)

    demo_title(size)

    demo_date(size)

    demo_prefix(size)

    demo_cols(size)

    demo_orientation(size)

    return 0


if __name__ == '__main__':
    sys.exit(main())

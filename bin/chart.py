#!/usr/bin/env python3
"""
    Reads lines from STDIN and makes a horizontal bar chart.

    Example:

        echo -e "a 1\nb 2.3\nc 4\na 3\nb 2\n c 1" | chart.py
"""
import re
import os
import sys

from barchart import BarChart


def chart_out(data, size):

    print('-' * size.columns)

    lc = BarChart(
        cols = size.columns,
        fields = list(data.keys()),
    )
    print(lc.pformat(data))


def parse_line(line, key_regex, val_regex):

    key, val = None, None
    key_m = key_regex.match(line)
    if key_m:
        key = key_m.group(1)

    val_m = val_regex.match(line)
    if val_m:
        val = float(val_m.group(1))

    return key, val


def main():

    key_regex = re.compile(r'^([A-Za-z0-9_]+)')
    val_regex = re.compile(r'^.+?([0-9]+([.][0-9]+)?)$')
    size = os.get_terminal_size()

    data = {}

    for line in sys.stdin:
        key, val = parse_line(line.strip(), key_regex, val_regex)
        if key is not None and val is not None:
            if key in data:
                chart_out(data, size)
                data = {}
            data[key] = val

    if len(data):
        chart_out(data, size)

    return 0


if __name__ == '__main__':
    sys.exit(main())

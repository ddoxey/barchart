import sys
from datetime import date
from pprint import pformat,  pprint


class BarChart:

    fields = None
    title = None
    date_fmt = None
    cols = 0
    prefix_every_line = False
    orientation = None

    def __init__(self,
                 fields=None,
                 title=None,
                 date_fmt=None,
                 cols=30,
                 prefix_every_line=True,
                 orientation='horizontal'):

        if orientation != 'horizontal' and orientation != 'vertical':
            raise Exception('orientation must be either vertical or horizontal')

        if date_fmt is not None and not isinstance(date_fmt, str):
            raise Exception('date_fmt must be a str')

        if title is not None and not isinstance(title, str):
            raise Exception('title must be a string')

        self.fields            = fields
        self.title             = title
        self.date_fmt          = date_fmt
        self.cols              = int(cols)
        self.prefix_every_line = prefix_every_line
        self.orientation       = orientation


    def pformat(self, data_for):
        format_for = {
            'vertical': self.vertical_format,
            'horizontal': self.horizontal_format,
        }
        fields = self.fields
        if fields is None:
            fields = list(data_for.keys())
        return format_for[self.orientation](data_for, fields)


    def make_bar(self, min_value, value, max_value, max_size, zero):

        if min_value == 0 and max_value == 0:
            return ""

        if min_value > max_value:
            raise Exception(f'Nonsense: min_value({min_value}), max_value({max_value})')

        total_magnitude = max_value

        if min_value <= 0:
            if max_value <= 0:
                total_magnitude = abs(min_value)
            else:
                total_magnitude = abs(min_value) + max_value

        reduction_ratio = max_size / total_magnitude

        sub_negative, negative, positive, scaling_factor = 0, 0, 0, 0

        max_negative_size, max_positive_size = 0, 0

        if min_value < 0:
            max_negative_size = round(reduction_ratio * abs(min_value))
            if max_value <= 0:
                max_positive_size = 0
            else:
                max_positive_size = max_size - max_negative_size - 1
        else:
            max_negative_size = 0
            max_positive_size = round(reduction_ratio * abs(max_value))
            zero = ""

        if value < 0:
            scaling_factor = value / min_value
            negative = round(scaling_factor * max_negative_size)
            sub_negative = max_negative_size - negative
        elif value == 0:
            sub_negative = max_negative_size
            positive = 0
        elif value > 0:
            sub_negative = max_negative_size
            scaling_factor = value / max_value
            positive = round(scaling_factor * max_positive_size)

        sub_negative = (' ') * round(sub_negative)

        if value < 0:
            negative = 'o' + ('*') * (negative - 1)
            positive = ""
        elif value == 0:
            positive = ""
            negative = ""
        elif value > 0:
            negative = ""
            if positive > 0:
                positive = ('*') * (positive - 1) + 'o'
            else:
                positive = ""

        return f'{sub_negative}{negative}{zero}{positive}'


    def vertical_format(self, data_for, fields):
        out = []
        bars = []
        labels = []
        height = 0
        prefix = ""

        if self.date_fmt is not None:
            prefix = date.today().strftime(self.date_fmt)
            if len(prefix) > 0 and prefix[-1] != ' ':
                prefix += ' '

        title = None
        if self.title is not None:
            title = f'{prefix}{self.title}'
            if not self.prefix_every_line:
                prefix = (' ') * len(prefix)

        label_w = 1
        label_for = {}
        min_value = sys.maxsize
        max_value = 1

        for name in fields:
            if name not in data_for:
                continue
            value = data_for[name]
            if isinstance(value, str):
                if '.' in value:
                    if all([n.isnumeric() for n in value.split('.', 1)]):
                        value = float(value)
                elif value.isnumeric():
                    value = int(value)
            if isinstance(value, int) or isinstance(value, float):
                label = f'{name}[{value}]:'
                min_value = min(min_value, value)
                max_value = max(max_value, value)
            else:
                label = f'{name}:'
            label_for[name] = label
            label_w = max(label_w, len(label))

        for i, name in enumerate(fields):

            if name not in label_for:
                continue
            label = ('{}{:>' + str(label_w) + '} ').format(prefix, label_for[name])
            value = data_for[name]

            if isinstance(value, int) or isinstance(value, float):
                text = self.make_bar(min_value, value, max_value, self.cols, zero='-')
            else:
                text = pformat(value)

            extension = ''
            extension += ('-') * (2 * i)
            extension += '+'
            extension += (' |') * (len(fields) - 1 - i)
            labels.append(f'{label}{extension}')

            bars.append(text)
            height = max(height, len(text))

            if not self.prefix_every_line:
                prefix = (' ') * len(prefix)

        for row_n in range(height):
            line = prefix + (' ') * label_w
            for bar in bars:
                if row_n >= len(bar):
                     line += '  '
                else:
                     line += f' {bar[row_n]}'
            out.insert(0, line)

        if title is not None:
            out.insert(0, title)

        out.extend(labels)

        return '\n'.join(out)


    def horizontal_format(self, data_for, fields):
        out = []
        prefix = ""

        if self.date_fmt is not None:
            prefix = date.today().strftime(self.date_fmt)
            if len(prefix) > 0 and prefix[-1] != ' ':
                prefix += ' '

        if self.title is not None:
            out.append(f'{prefix}{self.title}')
            if not self.prefix_every_line:
                prefix = (' ') * len(prefix)

        label_w = 1
        label_for = {}
        min_value = sys.maxsize
        max_value = 1

        for name in fields:
            if name not in data_for:
                continue

            value = data_for[name]

            if isinstance(value, str):
                if '.' in value:
                    if all([n.isnumeric() for n in value.split('.', 1)]):
                        value = float(value)
                elif value.isnumeric():
                    value = int(value)
            if isinstance(value, int) or isinstance(value, float):
                label = f'{name}[{value}]:'
                min_value = min(min_value, value)
                max_value = max(max_value, abs(value))
            else:
                label = f'{name}:'

            label_for[name] = label
            label_w = max(label_w, len(label))

        for name in fields:
            if name not in label_for:
                continue

            label = ('{}{:>' + str(label_w) + '} ').format(prefix, label_for[name])

            max_bar_w = self.cols - len(label)

            if max_bar_w < 0:
                max_bar_w = self.cols

            value = data_for[name]

            if isinstance(value, int) or isinstance(value, float):
                text = self.make_bar(min_value, value, max_value, self.cols - len(label), zero='|')
            else:
                text = pformat(value)

            out.append(f'{label}{text}')

            if not self.prefix_every_line:
                prefix = (' ') * len(prefix)

        return '\n'.join(out)

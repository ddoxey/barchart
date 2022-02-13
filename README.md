# BarChart

**basic**
```Python3
bc = BarChart()

print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))
```
```text
a[1]: *******o
b[2]: ***************o
c[3]: ***********************o
```

**fields**
```Python3
bc = BarChart(
    fields = ['a', 'b'],
)   

print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))
```
```text
a[1]: *******o
b[2]: ***************o
```

**title**
```Python3
bc = BarChart(
    title = 'Example'
)

print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))
```
```text
Example
a[1]: *******o
b[2]: ***************o
c[3]: ***********************o
```

**date_fmt**
```Python3
bc = BarChart(
    date_fmt = '[%D]'   
)

print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))
```
```text
[02/13/22] a[1]: ***o
[02/13/22] b[2]: ********o
[02/13/22] c[3]: ************o
```

**prefix_every_line**
```Python3
bc = BarChart(
    date_fmt = '[%D]',
    prefix_every_line = False
)

print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))
```
```text
[02/13/22] a[1]: ***o
           b[2]: ********o
           c[3]: ************o
```

**cols**
```Python3
bc = BarChart(
    cols = 60 
)

print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))
```
```text
a[1]: *****************o
b[2]: ***********************************o
c[3]: *****************************************************o
```

**orientation**
```Python3
bc = BarChart(
    orientation = 'vertical',
    cols = 20
)

print(bc.pformat({'a': 1, 'b': 2, 'c': 3}))
```
```text
          o
          *
          *
          *
          *
          *
          *
        o *
        * *
        * *
        * *
        * *
        * *
      o * *
      * * *
      * * *
      * * *
      * * *
      * * *
      * * *
a[1]: + | |
b[2]: --+ |
c[3]: ----+
```

# chart.py

```Shell
$ echo -e "a 1\nb 2.5\nc 5\na 5\nb 2.5\n c 1" | bin/chart.py
```
```text
---------------------------------------------------------------------
a[1.0]: ***********o
b[2.5]: *****************************o
c[5.0]: ************************************************************o
---------------------------------------------------------------------
a[5.0]: ************************************************************o
b[2.5]: *****************************o
c[1.0]: ***********o
```

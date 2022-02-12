import unittest
from datetime import date

from barchart import BarChart


class TestBarChart(unittest.TestCase):

    def test_one_int_field(self):

        lc = BarChart(
            title    = 'One Int',
            date_fmt = '[%Y-%m-%d %T]',
            cols     = 50,
            fields   = ['x'],
        )

        data = {'x': 20}

        # Expect: a line 50 columns for len(label) and len(bar)
        #         w/ 20% of available bar space used.
        d = date.today().strftime('[%Y-%m-%d %T]')
        expect = ""
        expect += f'{d} One Int\n'
        expect += f'{d} x[20]: ********************o'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'one-int-field')


    def test_deltas_positive(self):

        lc = BarChart(
            cols        = 10,
            fields      = ['time', 'link_cost', 'disjunct_cost'],
            orientation = 'vertical',
        )

        data = {
            'time': 100,
            'link_cost': 600,
            'disjunct_cost': 300,
        }

        expect = ""
        expect += f'                      o  \n'
        expect += f'                      *  \n'
        expect += f'                      *  \n'
        expect += f'                      *  \n'
        expect += f'                      *  \n'
        expect += f'                      * o\n'
        expect += f'                      * *\n'
        expect += f'                      * *\n'
        expect += f'                    o * *\n'
        expect += f'                    * * *\n'
        expect += f'         time[100]: + | |\n'
        expect += f'    link_cost[600]: --+ |\n'
        expect += f'disjunct_cost[300]: ----+'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'deltas')


    def test_deltas_negative(self):

        lc = BarChart(
            cols        = 10,
            fields      = ['time', 'link_cost', 'disjunct_cost'],
            orientation = 'vertical',
        )

        data = {
            'time': -100,
            'link_cost': 600,
            'disjunct_cost': -300,
        }

        expect = ""
        expect += f'                       o  \n'
        expect += f'                       *  \n'
        expect += f'                       *  \n'
        expect += f'                       *  \n'
        expect += f'                       *  \n'
        expect += f'                       *  \n'
        expect += f'                     - - -\n'
        expect += f'                     o   *\n'
        expect += f'                         *\n'
        expect += f'                         o\n'
        expect += f'         time[-100]: + | |\n'
        expect += f'     link_cost[600]: --+ |\n'
        expect += f'disjunct_cost[-300]: ----+'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'deltas')


    def test_several_int_fields(self):

        lc = BarChart(
            date_fmt = '[%Y-%m-%d %T]',
            fields = ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff']
        )

        data = {
            'a': 10,
            'bb': 25,
            'ccc': 50,
            'dddd': 65,
            'eeeee': 75,
            'ffffff': 99,
            'ggggggg': 20,
        }

        d = date.today().strftime('[%Y-%m-%d %T]')
        expect = ""
        expect += f'{d}      a[10]: ****o\n'
        expect += f'{d}     bb[25]: ***********o\n'
        expect += f'{d}    ccc[50]: **********************o\n'
        expect += f'{d}   dddd[65]: *****************************o\n'
        expect += f'{d}  eeeee[75]: **********************************o\n'
        expect += f'{d} ffffff[99]: *********************************************o'


        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'several-int-fields')


    def test_negative_to_positive_spread(self):

        lc = BarChart(
            date_fmt = '[%Y-%m-%d %T]',
            cols = 51,
            fields = [
                'a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k',
                'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u'
            ]
        )

        data = {
            'a': -10, 'b': -9, 'c': -8, 'd': -7, 'e': -6,
            'f': -5, 'g': -4, 'h': -3, 'i': -2, 'j': -1,
            'k': 0,
            'l': 1, 'm': 2, 'n': 3, 'o': 4, 'p': 5,
            'q': 6, 'r': 7, 's': 8, 't': 9, 'u': 10,
        }

        d = date.today().strftime('[%Y-%m-%d %T]')
        expect = ""
        expect += f'{d} a[-10]: o*********|\n'
        expect += f'{d}  b[-9]:  o********|\n'
        expect += f'{d}  c[-8]:   o*******|\n'
        expect += f'{d}  d[-7]:    o******|\n'
        expect += f'{d}  e[-6]:     o*****|\n'
        expect += f'{d}  f[-5]:      o****|\n'
        expect += f'{d}  g[-4]:       o***|\n'
        expect += f'{d}  h[-3]:        o**|\n'
        expect += f'{d}  i[-2]:         o*|\n'
        expect += f'{d}  j[-1]:          o|\n'
        expect += f'{d}   k[0]:           |\n'
        expect += f'{d}   l[1]:           |o\n'
        expect += f'{d}   m[2]:           |*o\n'
        expect += f'{d}   n[3]:           |**o\n'
        expect += f'{d}   o[4]:           |***o\n'
        expect += f'{d}   p[5]:           |****o\n'
        expect += f'{d}   q[6]:           |*****o\n'
        expect += f'{d}   r[7]:           |******o\n'
        expect += f'{d}   s[8]:           |*******o\n'
        expect += f'{d}   t[9]:           |********o\n'
        expect += f'{d}  u[10]:           |*********o'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'negative-to-positive-spread')


    def test_several_float_fields(self):

        lc = BarChart(
            date_fmt = '[%Y-%m-%d %T]',
            cols = 80,
            fields = ['a', 'b', 'c', 'd', 'e', 'f']
        )

        data = {
            'a': 10.1,
            'b': 25.2,
            'c': 50.3,
            'd': 65.4,
            'e': 75.5,
            'f': 99.6,
            'g': 20,
        }

        d = date.today().strftime('[%Y-%m-%d %T]')
        expect = ""
        expect += f'{d} a[10.1]: ****o\n'
        expect += f'{d} b[25.2]: ***********o\n'
        expect += f'{d} c[50.3]: ************************o\n'
        expect += f'{d} d[65.4]: *******************************o\n'
        expect += f'{d} e[75.5]: ************************************o\n'
        expect += f'{d} f[99.6]: ************************************************o'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'several-float-fields')


    def test_several_float_fields_vertical_100(self):

        lc = BarChart(
            date_fmt = '[%Y-%m-%d %T]',
            cols = 100 + 7,
            fields = ['a', 'b', 'c', 'd', 'e', 'f'],
            orientation='vertical',
        )

        data = {
            'a': 10.1,
            'b': 25.2,
            'c': 50.3,
            'd': 65.4,
            'e': 75.5,
            'f': 99.6,
            'g': 20,
        }

        d = date.today().strftime('[%Y-%m-%d %T]')
        expect = ""
        expect += f'{d}                    o\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                  o *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                o * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}              o * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}            o * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}          o * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d} a[10.1]: + | | | | |\n'
        expect += f'{d} b[25.2]: --+ | | | |\n'
        expect += f'{d} c[50.3]: ----+ | | |\n'
        expect += f'{d} d[65.4]: ------+ | |\n'
        expect += f'{d} e[75.5]: --------+ |\n'
        expect += f'{d} f[99.6]: ----------+'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'several-float-fields-vertical-100')


    def test_several_float_fields_vertical_50(self):

        lc = BarChart(
            date_fmt = '[%Y-%m-%d %T]',
            cols = 50 + 7,
            fields = ['a', 'b', 'c', 'd', 'e', 'f'],
            orientation='vertical',
        )

        data = {
            'a': 10.1,
            'b': 25.2,
            'c': 50.3,
            'd': 65.4,
            'e': 75.5,
            'f': 99.6,
            'g': 20,
        }

        d = date.today().strftime('[%Y-%m-%d %T]')
        expect = ""
        expect += f'{d}                    o\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                  o *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                o * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}              o * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}            o * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}          o * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d} a[10.1]: + | | | | |\n'
        expect += f'{d} b[25.2]: --+ | | | |\n'
        expect += f'{d} c[50.3]: ----+ | | |\n'
        expect += f'{d} d[65.4]: ------+ | |\n'
        expect += f'{d} e[75.5]: --------+ |\n'
        expect += f'{d} f[99.6]: ----------+'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'several-float-fields-vertical-50')


    def test_several_float_fields_vertical_10(self):

        lc = BarChart(
            date_fmt = '[%Y-%m-%d %T]',
            cols = 10,
            fields = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
            orientation='vertical',
        )

        data = {
            'a': 0.1,
            'b': 10.1,
            'c': 20.1,
            'd': 30.1,
            'e': 40.1,
            'f': 50.1,
            'g': 60.1,
            'h': 70.1,
            'i': 80.1,
            'j': 90.1,
            'k': 100.1,
        }

        d = date.today().strftime('[%Y-%m-%d %T]')
        expect = ""
        expect += f'{d}                               o\n'
        expect += f'{d}                             o *\n'
        expect += f'{d}                           o * *\n'
        expect += f'{d}                         o * * *\n'
        expect += f'{d}                       o * * * *\n'
        expect += f'{d}                     o * * * * *\n'
        expect += f'{d}                   o * * * * * *\n'
        expect += f'{d}                 o * * * * * * *\n'
        expect += f'{d}               o * * * * * * * *\n'
        expect += f'{d}             o * * * * * * * * *\n'
        expect += f'{d}   a[0.1]: + | | | | | | | | | |\n'
        expect += f'{d}  b[10.1]: --+ | | | | | | | | |\n'
        expect += f'{d}  c[20.1]: ----+ | | | | | | | |\n'
        expect += f'{d}  d[30.1]: ------+ | | | | | | |\n'
        expect += f'{d}  e[40.1]: --------+ | | | | | |\n'
        expect += f'{d}  f[50.1]: ----------+ | | | | |\n'
        expect += f'{d}  g[60.1]: ------------+ | | | |\n'
        expect += f'{d}  h[70.1]: --------------+ | | |\n'
        expect += f'{d}  i[80.1]: ----------------+ | |\n'
        expect += f'{d}  j[90.1]: ------------------+ |\n'
        expect += f'{d} k[100.1]: --------------------+'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'several-float-fields-vertical-10')


    def test_several_float_fields_vertical(self):

        lc = BarChart(
            date_fmt = '[%Y-%m-%d %T]',
            cols = 80,
            fields = ['a', 'b', 'c', 'd', 'e', 'f'],
            orientation='vertical',
        )

        data = {
            'a': 10.1,
            'b': 25.2,
            'c': 50.3,
            'd': 65.4,
            'e': 75.5,
            'f': 99.6,
            'g': 20,
        }

        d = date.today().strftime('[%Y-%m-%d %T]')
        expect = ""
        expect += f'{d}                    o\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                    *\n'
        expect += f'{d}                  o *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                  * *\n'
        expect += f'{d}                o * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}                * * *\n'
        expect += f'{d}              o * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}              * * * *\n'
        expect += f'{d}            o * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}            * * * * *\n'
        expect += f'{d}          o * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d}          * * * * * *\n'
        expect += f'{d} a[10.1]: + | | | | |\n'
        expect += f'{d} b[25.2]: --+ | | | |\n'
        expect += f'{d} c[50.3]: ----+ | | |\n'
        expect += f'{d} d[65.4]: ------+ | |\n'
        expect += f'{d} e[75.5]: --------+ |\n'
        expect += f'{d} f[99.6]: ----------+'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'several-float-fields-vertical')


    def test_mixed_bag(self):

        lc = BarChart(
            title             = 'Mixed Bag!',
            date_fmt          = '[%Y-%m-%d %T]',
            cols              = 80,
            fields            = ['a', 'b', 'c', 'd', 'e'],
            prefix_every_line = False,
        )

        data = {
            'a': 10,
            'b': 25.2,
            'c': { 'x': 50.3, 'y': 10 },
            'd': -17,
            'e': -9,
        }

        d = date.today().strftime('[%Y-%m-%d %T]')
        expect = ""
        expect += f'{d} Mixed Bag!\n'
        expect += '                        a[10]:                     |**********o\n'
        expect += '                      b[25.2]:                     |***************************o\n'
        expect += "                            c: {'x': 50.3, 'y': 10}\n"
        expect += '                       d[-17]: o*******************|\n'
        expect += '                        e[-9]:          o**********|'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'mixed-bag')


    def test_link_cost(self):

        lc = BarChart(
            cols = 25,
            fields = [
                '1.The',
                '2.FBI',
                '3.headquarters',
                '4.is',
                '5.the',
                '6.J.',
                '7.Edgar',
                '8.Hoover',
                '9.Building,',
                '10.located',
                '11.in',
                '12.Washington,',
                '13.DC.',
                '14.The',
                '15.mission'
            ],
            prefix_every_line = False,
            orientation = 'vertical',
        )

        data = {
            '1.The': 0,
            '2.FBI': 300,
            '3.headquarters': 600,
            '4.is': 700,
            '5.the': 800,
            '6.J.': 1000,
            '7.Edgar': 1300,
            '8.Hoover': 1600,
            '9.Building,': 2000,
            '10.located': 3000,
            '11.in': 3100,
            '12.Washington,': 3200,
            '13.DC.': 3300,
            '14.The': 3400,
            '15.mission': 3900,
        }


        expect = ""
        expect += f'                                                  o\n'
        expect += f'                                                  *\n'
        expect += f'                                                  *\n'
        expect += f'                                                o *\n'
        expect += f'                                            o o * *\n'
        expect += f'                                          o * * * *\n'
        expect += f'                                        o * * * * *\n'
        expect += f'                                        * * * * * *\n'
        expect += f'                                        * * * * * *\n'
        expect += f'                                        * * * * * *\n'
        expect += f'                                        * * * * * *\n'
        expect += f'                                        * * * * * *\n'
        expect += f'                                      o * * * * * *\n'
        expect += f'                                      * * * * * * *\n'
        expect += f'                                      * * * * * * *\n'
        expect += f'                                    o * * * * * * *\n'
        expect += f'                                    * * * * * * * *\n'
        expect += f'                                  o * * * * * * * *\n'
        expect += f'                                  * * * * * * * * *\n'
        expect += f'                                o * * * * * * * * *\n'
        expect += f'                              o * * * * * * * * * *\n'
        expect += f'                          o o * * * * * * * * * * *\n'
        expect += f'                          * * * * * * * * * * * * *\n'
        expect += f'                        o * * * * * * * * * * * * *\n'
        expect += f'                        * * * * * * * * * * * * * *\n'
        expect += f'            1.The[0]: + | | | | | | | | | | | | | |\n'
        expect += f'          2.FBI[300]: --+ | | | | | | | | | | | | |\n'
        expect += f' 3.headquarters[600]: ----+ | | | | | | | | | | | |\n'
        expect += f'           4.is[700]: ------+ | | | | | | | | | | |\n'
        expect += f'          5.the[800]: --------+ | | | | | | | | | |\n'
        expect += f'          6.J.[1000]: ----------+ | | | | | | | | |\n'
        expect += f'       7.Edgar[1300]: ------------+ | | | | | | | |\n'
        expect += f'      8.Hoover[1600]: --------------+ | | | | | | |\n'
        expect += f'   9.Building,[2000]: ----------------+ | | | | | |\n'
        expect += f'    10.located[3000]: ------------------+ | | | | |\n'
        expect += f'         11.in[3100]: --------------------+ | | | |\n'
        expect += f'12.Washington,[3200]: ----------------------+ | | |\n'
        expect += f'        13.DC.[3300]: ------------------------+ | |\n'
        expect += f'        14.The[3400]: --------------------------+ |\n'
        expect += f'    15.mission[3900]: ----------------------------+'

        got = lc.pformat(data)

        print(f'EXP[\n{expect}]')
        print(f'GOT[\n{got}]')

        self.assertEqual(got, expect, 'link-cost')


if __name__ == '__main__':
    unittest.main()

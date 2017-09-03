# 유닛테스트에서 예외 조건 시험하기

import unittest

def parse_int(s):
    return int(s)



class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')   # 예외여부 테스팅




class TestConvenersion(unittest.TestCase):
    def test_bed_int(self):
        try:
            r = parse_int('N/A')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'N/A')
        else:
            self.fail('ValueError not raised')


# 위의 기능을 콘텍스트매니저로 사용가능


class TestConvenersion2(unittest.TestCase):
    def test_bed_int(self):
        with self.assertRaisesRegex(ValueError, 'invalid litral .*'):
            r = parse_int('N/A')


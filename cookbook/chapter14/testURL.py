
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from cookbook.chapter14.mymodule import urlprint

class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'

        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)



test = TestURLPrint()
print(test.test_url_gets_to_stdout())

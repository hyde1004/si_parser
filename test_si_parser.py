import unittest
import si_parser;

class TestSIParser(unittest.TestCase):
	def test_create(self):
		client = si_parser.si_parser('20130912_P30_546000KHz_ArteHD_short.ts');
		self.assertEqual('20130912_P30_546000KHz_ArteHD_short.ts', client.filename)

	def test_destroy(self):
		pass

if __name__== '__main__':
	unittest.main()

import unittest
from Adder import Adder

class MyTestCase(unittest.TestCase):
  def test_default_greeting_set(self):
    ad = Adder()
    self.assertEqual(ad.sum, 10)

if __name__ == '__main__':
  unittest.main()

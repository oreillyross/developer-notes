import unittest

class Testing(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('beta'.upper(), 'BETA')
    
    def test_boolean(self):
        x = True
        y = True

        self.assertEqual(x, y)
    
    def test_isupper(self):
        self.assertTrue('BETA'.isupper())
        self.assertFalse('beta'.isupper())

# run the tests
unittest.main()
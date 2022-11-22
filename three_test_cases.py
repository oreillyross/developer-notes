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

# Using fixtures in the form of setup and tearDown classes

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('\nsetup')
    
    @classmethod
    def tearDownClass(cls) -> None:
        print('\nteardown')

    def setup(self):
        pass
    
    def tearDown(self):
        pass

# Running test classes in a test runner

class TestString(unittest.TestCase):

    def runTest(self):
        self.assertEqual('a'* 4, 'aaaa')
    
class TestUCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual('gama'.upper(), 'GAMA')

if __name__ == '__main__':
    suite = unittest.TestSuite([TestString, TestUCase])
    unittest.TextTestRunner().run(suite)


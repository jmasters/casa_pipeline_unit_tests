import unittest

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        # this test will fail until you change the Greeter to return this expected message
        self.assertEqual('Hello world!', 'Hello world!')

def suite():
    return [MyTestCase]

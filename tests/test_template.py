import unittest
    
class MyTestCase(unittest.TestCase):
    def test_failure(self):
        self.assertTrue(False)
    
def suite():
    return [MyTestCase]

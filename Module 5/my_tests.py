import unittest
import my_mod

class RandomTesting(unittest.TestCase):
    #setup function runs before each test
    def setUp(self):
        pass
    #teardown runs after each test is executed
    def tearDown(self):
        pass

    def test_random(self):
        rand_num = my_mod.my_num()
        self.assertTrue(0 < rand_num < 1)

    def test_random_wrong(self):
        rand_num = my_mod.my_num()
        self.assertTrue(rand_num == int(rand_num))

    def test_int(self):
        rand_int = my_mod.my_int()
        self.assertEquals(rand_int,int(rand_int))
    
if __name__ == '__main__':
    unittest.main()    
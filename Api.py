# -*- coding: utf-8 -*-

import requests,json,unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print ('fixture setup')
    def tearDown(self):
         print('fixtrre tearDown')
    def test_upper(self):
        """
        测试是否大小写正常
        ：:return;
        """
        self.assertTrue('F00'.isupper())
        self.assertFalse('foo'.isupper())
    def test_split(self):
         """
         测试hello world
         :return:
         """
         s='hello world'
         self.asserEqual(s.split(),['hello','world'])
         with self.assertRaises(TypeError):
             s.split(2)
if __name__=='__main__':
    unittest.main()

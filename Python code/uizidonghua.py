import unittest
from selenium import webdriver
import unittest

class ItestInfoTestCase(unittest.TestCase):
    def test_interface_test_calss_should_have_correct_date(self):
        dr = webdriver.Chrome(r'D:\chromedriver.exe')
        # dr.get('http://www.itest.info')
        dr.get('http://www.itest.info/courses/6')#管理员视角
        date_dom = dr.find_element_by_css_selector('strong.text-danger')
        # print(date_dom.text)
        self.assertEqual(date_dom.text,'2021年2月28日（预计）')


if __name__ == '__main__':
    unittest.main()
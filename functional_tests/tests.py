#python3

#from django.test import LiveServerTestCase
import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url='http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """ If there are no exceptions, close the browser windows when you're done."""
        self.browser.quit()

    #helper method (used at least twice)

    def check_for_row_in_table(self, row_text):
        table=self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])









   

#not needed b/c running with python3 manage.py test functional_tests command through django

#if __name__=='__main__':
    #unittest.main(warnings='ignore')
#    unittest.main()


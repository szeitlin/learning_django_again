#python3

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def test_can_start_a_list_and_retrieve_later(self):
        """ A user visits the site"""
        self.browser.get('http://localhost:8000')

        #User notices the header and title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

#enter a to-do item

#type into a text box

#check that it appears on the site

#add another item

#check that both items appear

#check that there's now a unique URL

#visit that URL again and make sure the items are still there

    def tearDown(self):
        """ If there are no exceptions, close the browser windows when you're done."""
        browser.quit()

if __name__=='__main__':
    #unittest.main(warnings='ignore')
    unittest.main()


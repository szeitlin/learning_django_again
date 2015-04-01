#python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        #enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #type into a text box
        inputbox.send_keys('buy peacock feathers')


        #check that it appears on the site
        inputbox.send_keys(Keys.ENTER)

        table=self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])	

        #add another item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('use peacock feathers to make bait for fly fishing')
        inputbox.send_keys(Keys.ENTER)


        #check that both items appear
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('2: use peacock feathers to make bait for fly fishing',[row.text for row in rows])

    #check that there's now a unique URL
        self.fail('Finish the test!')

    #visit that URL again and make sure the items are still there

    def tearDown(self):
        """ If there are no exceptions, close the browser windows when you're done."""
        browser.quit()

if __name__=='__main__':
    #unittest.main(warnings='ignore')
    unittest.main()


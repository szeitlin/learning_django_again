__author__ = 'szeitlin'

from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_later(self):
        """ Two users visit the site. Edith first, then Francis.
        Takes advantage of the LiveServerTestCase module"""

        self.browser.get(self.server_url)

        #self.browser.get('http://localhost:8000')

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
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        #check that it appears on the site
        edith_list_url = self.browser.current_url
        print(edith_list_url)
        self.assertRegex(edith_list_url,'/lists/.+')
        self.check_for_row_in_table('1: Buy peacock feathers')

        table=self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        #add another item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('use peacock feathers to make bait for fly fishing')
        inputbox.send_keys(Keys.ENTER)

        #check that both items appear in Edith's list (refactored)
        self.check_for_row_in_table('1: Buy peacock feathers')
        self.check_for_row_in_table('2: use peacock feathers to make bait for fly fishing')

        #now a new user, Francis, comes along.

        ## using a new browser session to make sure Edith's list doesn't cross-contaminate
        self.browser.quit()
        self.browser=webdriver.Firefox()

        #Francis visits the page. Make sure Edith's stuff is gone.
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make bait for fly', page_text)

        #Francis starts his own list. His list is boring.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #Francis gets his own url
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #check again for overlap with Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
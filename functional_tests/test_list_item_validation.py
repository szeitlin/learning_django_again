__author__ = 'szeitlin'

from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):
        #hit enter on an empty input box
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #get an error message saying the item can't be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "List items cannot be empty")

        #try again with actual text
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_table('1: Buy milk')

        #now try to submit another blank item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #get same warning
        self.check_for_row_in_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "List items cannot be empty")

        #fill in some text
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_table('1: Buy milk')
        self.check_for_row_in_table('2: Make tea')


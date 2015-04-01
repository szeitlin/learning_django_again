from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_url_is_home_page(self):
         found=resolve('/')
         self.assertEqual(found.func, home_page)

#class SmokeTest(TestCase):
#    def test_bad_math(self):
#        self.assertEqual(1+1,3)



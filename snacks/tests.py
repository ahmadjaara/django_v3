from multiprocessing import set_forkserver_preload
from sys import setdlopenflags
from urllib import response
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SnakTest(TestCase):
    def test_list_page_status_code(self):
        url=reverse("snack_list")
        response= self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_list_page_template(self):
        url=reverse("snack_list")
        response=self.client.get(url)
        self.assertTemplateUsed(response,"snack_list.html")
        self.assertTemplateUsed(response,"base1.html")
    
    def test_detail_page_status_code(self):
        url=reverse('snack_detail', kwargs={'pk': 7})
        response= self.client.get(url)
        self.assertEqual(response.status_code,200)
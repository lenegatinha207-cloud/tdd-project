from django.test import TestCase
from lists.models import List, Item


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'lists/home.html')


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        list_ = List.objects.create()

        response = self.client.get(f'/lists/{list_.id}/')

        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_all_list_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='Primeiro item', list=list_)
        Item.objects.create(text='Segundo item', list=list_)

        response = self.client.get(f'/lists/{list_.id}/')

        self.assertContains(response, 'Primeiro item')
        self.assertContains(response, 'Segundo item')
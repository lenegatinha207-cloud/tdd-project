from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Lista de tarefas', self.browser.title)

        self.browser.find_element('name', 'item_text').send_keys('Comprar leite')
        self.browser.find_element('name', 'item_text').submit()

        print(self.browser.title)
        print(self.browser.page_source)

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Lista de tarefas', self.browser.title)
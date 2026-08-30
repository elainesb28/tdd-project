from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def test_can_start_a_list_and_retrieve_it_later(self): 
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
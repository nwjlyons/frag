from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from pyvirtualdisplay import Display


class TestSelenium(LiveServerTestCase):

    show_browser = False

    @classmethod
    def setUpClass(cls):
        if cls.show_browser is False:
            cls.display = Display(visible=False)
            cls.display.start()
        cls.selenium = WebDriver()
        super(TestSelenium, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestSelenium, cls).tearDownClass()

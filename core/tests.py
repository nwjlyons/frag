from test_utils import TestSelenium


class TestAUser(TestSelenium):

    # show_browser = True

    def test_can_frag_a_webpage_and_update_the_url_fragment_by_clicking(self):
        self.selenium.get(self.live_server_url)

        self.selenium.find_element_by_css_selector("[type=submit]").click()
        self.assertIn("This field is required.", self.selenium.page_source)

        url_input = self.selenium.find_element_by_name("url")
        url_input.send_keys('this is not a url')

        self.selenium.find_element_by_css_selector("[type=submit]").click()
        self.assertIn("Enter a valid URL.", self.selenium.page_source)

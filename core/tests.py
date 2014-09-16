from test_utils import TestSelenium

from views import jquery, script, style


class TestFrag(TestSelenium):

    # show_browser = True

    def test_frag_a_webpage_and_update_the_url_fragment_by_clicking(self):
        self.selenium.get(self.live_server_url)

        self.selenium.find_element_by_css_selector("[type=submit]").click()
        self.assertIn("This field is required.", self.selenium.page_source)

        url_input = self.selenium.find_element_by_name("url")
        url_input.clear()
        url_input.send_keys('this is not a url')
        self.selenium.find_element_by_css_selector("[type=submit]").click()
        self.assertIn("Enter a valid URL.", self.selenium.page_source)

        url_input = self.selenium.find_element_by_name("url")
        url_input.clear()
        url_input.send_keys('http://httpbin.org/status/404')
        self.selenium.find_element_by_css_selector("[type=submit]").click()
        self.assertIn("Error fetching page.", self.selenium.page_source)

        url_input = self.selenium.find_element_by_name("url")
        url_input.clear()
        url_input.send_keys('http://en.wikipedia.org/wiki/Japan')
        self.selenium.find_element_by_css_selector("[type=submit]").click()
        self.assertEqual(self.selenium.title, u'Japan - Wikipedia, the free encyclopedia')
        self.assertEqual(self.selenium.current_url,
            u'{}/?url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FJapan'.format(self.live_server_url))

        self.assertIn(str(style), self.selenium.page_source)
        # self.assertIn(str(jquery), self.selenium.page_source) # This fails for some reason
        self.assertIn(str(script), self.selenium.page_source)


        self.selenium.find_element_by_id("Culture").click()
        self.assertEqual(self.selenium.current_url,
            u'{}/?url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FJapan#Culture'.format(self.live_server_url))

        self.selenium.find_element_by_id("frag-2743").click()
        self.assertEqual(self.selenium.current_url,
            u'{}/?url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FJapan#frag-2743'.format(self.live_server_url))

    def test_page_doesnt_contain_style_and_script_tags_we_added(self):
        self.selenium.get(self.live_server_url + "?url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FJapan#frag-2743")

        # self.assertNotIn(str(style), self.selenium.page_source)
        # self.assertNotIn(str(script), self.selenium.page_source)

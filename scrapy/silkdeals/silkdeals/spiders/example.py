import scrapy
# 導入插件
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys


class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com/',
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):

        driver = response.meta['driver']
        search_input = driver.find_element_by_xpath(
            '//input[@id = "search_form_input_homepage"]')
        search_input.send_keys('Hello World')

        search_input.send_keys(Keys.ENTER)

        # 注意：如果 links = response.xpath...respons e會是 start_requests 的 url
        html = driver.page_source
        response_obj = Selector(text=html)

        links = response_obj.xpath('//h2/a')
        for link in links:
            yield {
                'URL': link.xpath('.//@href').get()
            }

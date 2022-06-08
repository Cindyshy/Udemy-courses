import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = [
        'web.archive.org/web/20200116052415/https://www.livecoin.net/en']
    # 添加 start_urls
    start_urls = [
        'https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/']

    # 初始化
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("./chromedriver")

        driver = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get(
            "https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/")

        rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        rur_tab[4].click()

        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        currencies = resp.xpath("//div[contains(@class, 'tableRow___3EtiS ')]")
        for currency in currencies:
            yield {
                'name': currency.xpath(".//div[contains(@class, 'tableRowColumn___rDsl0')]/div[1]/text()").get(),
                'v 24h': currency.xpath(".//div[contains(@class, 'tableRowColumn___rDsl0')][5]//text()").get()
            }

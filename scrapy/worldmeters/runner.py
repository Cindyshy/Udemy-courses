import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from worldmeters.spiders.countries import CountriesSpider

# settings.py獲取所有設定
process = CrawlerProcess(settings=get_project_settings())
# 等同於從 terminal 中呼叫 scrapy crawl countries
process.crawl(CountriesSpider)


process.start()

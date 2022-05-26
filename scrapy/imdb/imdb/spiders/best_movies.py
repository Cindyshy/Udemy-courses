import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = [
        'web.archive.org']
    # start_urls = [
    #     'http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    # 新增 user_agent 並貼上
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'

    # 新增 start_requests，並將 start_urls 註解/刪除
    def start_requests(self):
        yield scrapy.Request(url='http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', headers={'User-Agent': self.user_agent})

    # 加入 process_request='set_user_agent'
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True, process_request='set_user_agent'), Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), process_request='set_user_agent'))

    # 定義 set_user_agent
    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield{
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
            'duration': response.xpath("normalize-space((//time)[1]/text())").get(),
            'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'rating': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'movie_url': response.url,
            'user-agent': response.request.headers['User-Agent']
        }

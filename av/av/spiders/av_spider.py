from ..items import FhItem, ActItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class AvSpider(CrawlSpider):
    name = 'av'
    allowed_domains = ['icpmp.com']
    start_urls = [
        # 'http://www.icpmp.com/fanhao/',
        'http://www.icpmp.com/fanhao/avLAF39.html',
    ]

    rules = (
        Rule(LinkExtractor(deny=(
            r'fanhao/avtiantang\S*\.html',
        ), allow=(r'\S*fanhao/av\S+\d*\.html',)), callback='parse_fh', follow=True),

        Rule(LinkExtractor(allow='fanhao/\S+\.html', deny=(
            r'fanhao/daquan\S*\.html',
            r'fanhao/liebiao\S*\.html',
            r'fanhao/sousuo\S*\.html',
            r'fanhao/nvyou\S*\.html',
        )), callback='parse_ny', follow=True,),

        Rule(LinkExtractor(allow=(
            r'fanhao/avtiantang\S*\.html',
            r'fanhao/daquan\S*\.html',
            r'fanhao/liebiao\S*\.html',
            r'fanhao/sousuo\S*\.html',
            r'fanhao/nvyou\S*\.html',
        ))),
    )

    def parse_fh(self, resp):
        info = resp.xpath('//div[@class="intro_inner"]')

        title = info.xpath('.//h3[@class="title_inner"]/text()').extract()[0]
        score = \
            info.xpath('.//span[@class="title_inner mod_score"]/strong/text()').extract()[0] + \
            info.xpath('.//span[@class="title_inner mod_score"]/text()').extract()[0]
        date = info.xpath('.//li[@class="list_item list_itema"]//a/text()').extract()[0]
        act = info.xpath('.//li[@class="list_item list_itemm"]//a/text()').extract()[:-1]
        item = FhItem(title=title, score=score, date=date, act=act)
        return item

    def parse_ny(self, resp):
        info = resp.xpath('//div[@class="intro_inner"]')

        name = info.xpath('//h3[@class="title_inner"]/text()').extract()[0]
        note = info.xpath('//span[@class="inner"]/text()').extract()[0]

        info_list = info\
            .xpath('//ul[@class="info_list"]/*//div[@class="mod_name"]/text()').extract()
        if len(info_list) is 5:
            other = info_list[0]
            birth = info_list[1]
            date = info_list[2]
            sanwei = info_list[3]
        else:
            other = info_list[0]
            birth = ''
            date = info_list[1]
            sanwei = info_list[2]
        item = ActItem(
            name=name, note=note,
            other=other, birth=birth,
            date=date, sanwei=sanwei)
        return item

import datetime
import urllib.parse
import socket
import scrapy

from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from scrapy.http import Request

from properties.items import PropertiesItem

# Run with C:>  scrapy crawl finesseSpider -o all_finesse_tools.json

class BasicSpider(scrapy.Spider):
    name = "finesseSpider"
    # custom_settings = {
    #     'FEED_EXPORT_ENCODING': 'utf-8', # FEED_EXPORT_ENCODING = 'utf-8'
    # }
    # For more info see Built-in settings reference:  https://doc.scrapy.org/en/latest/topics/settings.html#topics-settings-ref
    # For a list:  https://docs.scrapy.org/en/latest/topics/feed-exports.html#std:setting-FEED_EXPORT_ENCODING 
     
    download_delay = 2
    allowed_domains = ["pdrfinessetools.com"]

    # Start on the first index page
    # response.xpath('//*[@id="content"]//div/div[1]/ul/li//a/@href').extract()
    start_urls = ['http://pdrfinessetools.com/index.php?route=product/category&path=229',
                'http://pdrfinessetools.com/By Design',
                'http://pdrfinessetools.com/By Design/flat bars',
                'http://pdrfinessetools.com/By Design/aluminum products',
                'http://pdrfinessetools.com/By Design/Rods Tools',
                'http://pdrfinessetools.com/By Design/Roof Tools',
                'http://pdrfinessetools.com/By Design/Single Bend',
                'http://pdrfinessetools.com/By Design/Double Bend',
                'http://pdrfinessetools.com/By Design/Triple Bend',
                'http://pdrfinessetools.com/By Design/small hand tools',
                'http://pdrfinessetools.com/By Design/Flag Sets',
                'http://pdrfinessetools.com/By Design/shavedaccess1',
                'http://pdrfinessetools.com/By Design/shavedaccess1/Hand Tools',
                'http://pdrfinessetools.com/By Design/shavedaccess1/Long Rods',
                'http://pdrfinessetools.com/By Design/Door Tools',
                'http://pdrfinessetools.com/By Design/Whale Tails',
                'http://pdrfinessetools.com/By Design/Whale Tails/12" Head Whale Tail',
                'http://pdrfinessetools.com/By Design/Whale Tails/34" Head Whale Tail',
                'http://pdrfinessetools.com/By Design/Whale Tails/118" Head Whale Tail',
                'http://pdrfinessetools.com/By Design/Whale Tails/1 38" Head Whale Tail',
                'http://pdrfinessetools.com/By Design/Whale Tails/2" Head Whale Tail',
                'http://pdrfinessetools.com/By Design/Whale Tails/Up to 10 inches',
                'http://pdrfinessetools.com/By Design/Whale Tails/11to20incheswhailtails',
                'http://pdrfinessetools.com/By Design/Whale Tails/21 to 30 inches',
                'http://pdrfinessetools.com/By Design/Whale Tails/31 Inches And Up',
                'http://pdrfinessetools.com/By Design/Changable Tips',
                'http://pdrfinessetools.com/By Design/Changable Tips/Tools',
                'http://pdrfinessetools.com/By Design/Changable Tips/Tips',
                'http://pdrfinessetools.com/By Design/Adjustable Handled Tools',
                'http://pdrfinessetools.com/By Design/Specialty Tools',
                'http://pdrfinessetools.com/By Design/Tools Sets',
                'http://pdrfinessetools.com/By Design/Tools Sets/Complete Tool Sets',
                'http://pdrfinessetools.com/By Design/Tools Sets/Rod Sets',
                'http://pdrfinessetools.com/By Design/Tools Sets/Whail Tail Sets',
                'http://pdrfinessetools.com/by diamtre',
                'http://pdrfinessetools.com/by diamtre/316 inch ',
                'http://pdrfinessetools.com/by diamtre/14 inch',
                'http://pdrfinessetools.com/by diamtre/516 inch ',
                'http://pdrfinessetools.com/by diamtre/38 inch',
                'http://pdrfinessetools.com/by diamtre/716 inch',
                'http://pdrfinessetools.com/by diamtre/12 inch',
                'http://pdrfinessetools.com/by diamtre/916 inch',
                'http://pdrfinessetools.com/by diamtre/58 inch',
                'http://pdrfinessetools.com/by diamtre/34 inch',
                'http://pdrfinessetools.com/By Length',
                'http://pdrfinessetools.com/By Length/up to 5 inches',
                'http://pdrfinessetools.com/By Length/6 to 10 inches',
                'http://pdrfinessetools.com/By Length/11 to 20 inches',
                'http://pdrfinessetools.com/By Length/21 to 30 inches rod',
                'http://pdrfinessetools.com/By Length/31 to 40 inches',
                'http://pdrfinessetools.com/By Length/41 inches plus',
                'http://pdrfinessetools.com/Other Stuff',
                'http://pdrfinessetools.com/Other Stuff/hammers-knockdowns',
                'http://pdrfinessetools.com/Other Stuff/dooraccessories',
                'http://pdrfinessetools.com/Other Stuff/hood-accessories',
                'http://pdrfinessetools.com/index.php?route=product/category&path=40_228',
                'http://pdrfinessetools.com/Other Stuff/glue-pulling',
                'http://pdrfinessetools.com/Other Stuff/hood stand',
                'http://pdrfinessetools.com/tool videos',
                'http://pdrfinessetools.com/index.php?route=extension/list/featured',
                'http://pdrfinessetools.com/index.php?route=extension/list/latest'
                ]

    def parse(self, response):
        # Get the next index URLs and yield Requests
        next_selector = response.xpath('//li[@class="active"]/following-sibling::*[1]/a/@href')
        for url in next_selector.extract():
            yield Request(urllib.parse.urljoin(response.url, url))

        # Get item URLs and yield Requests
        item_selector = response.xpath('//*[@class="product-thumb"]/div/a/@href')
        for url in item_selector.extract():
            yield Request(urllib.parse.urljoin(response.url, url),
                          callback=self.parse_item)

    def parse_item(self, response):
        """ This function parses a property page.

        @url http://pdrfinessetools.com/index.php?route=extension/list/latest
        @returns items 1
        @scrapes product_title price description product_code image_urls
        @scrapes url project spider server date
        """

        # Create the loader using the response
        l = ItemLoader(item=PropertiesItem(), response=response)

        # Load fields using XPath expressions
        l.add_xpath('product_title', '//*[@id="content"]//h1/text()', MapCompose(str.strip, str.title))
        l.add_xpath('price', '//*[@class="list-unstyled"]//h2/text()')
        l.add_xpath('description', '//*[@id="tab-description"]//text()', MapCompose(str.strip), Join())
        l.add_xpath('product_code', '//*[@id="content"]//*[@class="list-unstyled"]//li[2]/text()', MapCompose(str.strip))
        l.add_xpath('image_urls', '//*[@id="content"]//a[@class="thumbnail"]//img/@src', MapCompose(lambda i: urllib.parse.urljoin(response.url, i)))

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())

        return l.load_item()

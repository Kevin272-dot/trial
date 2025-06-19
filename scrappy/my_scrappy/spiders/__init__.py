import scrapy


class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["https://www.yahoo.com/"]

    def parse(self, response):
        title = response.css('title::text').get()
        paragraphs = response.css('p::text').getall()
        print("Title:", title)
        print("paragraphs:", paragraphs)

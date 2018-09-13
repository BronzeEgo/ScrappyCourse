# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # name must be unique within the project. Two spiders in same project cannot have same name!
    # allowed_domains. Domains that are allowed. Good for sites with ads. Scrapy will not follow anything that does not have this url
    allowed_domains = ['http://quotes.toscrape.com/']
    # start_urls. tuple or list (default list). It will add http://, SO BE CAREFUL (I had to remove second instance)!
    start_urls = ['http://quotes.toscrape.com//']
    # parse is default callback method in scrapy.Spider subclass.
    # parse is called for requests without explicitly assigned callback.
    # it has self because it is in a class, and respond becasue it will get the response object or HTML nodes or source code from start page

    def parse(self, response):
        # pass #this will be there by default.
        # Below is the code I found to work to get the H1 text. It is assigned to a variable:
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        # Below is the code I found to work to get the tags on the right of the page. It is assigned to a variable:
        top_tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        # I then need to yield the items above.
        # By yielding these two data points, I will print it out in Scrapy output, and then I can get data to a usable for (CSV, JSON, etc.)
        # I am creating a dict with key value pairs for the data I want
        yield {
            'H1 Tag': h1_tag,
            'Tags': top_tags
        }
# at about 4:00, I save and open a new terminal with scrapy

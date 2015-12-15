import scrapy


class Listing(scrapy.Item):
    price = scrapy.Field()
    currency = scrapy.Field()
    listing_type = scrapy.Field()
    surface = scrapy.Field()
    rooms = scrapy.Field()
    address = scrapy.Field()

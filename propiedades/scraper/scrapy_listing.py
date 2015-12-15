""" Scrapy Items.

Each scraper generates a Listing item. This is in a separated file for reuse.

The Normalizer modifies this object and the Store Manager creates a SaleListing
or a RentListing depending on the listing_type and store the listing in the DB.

"""
import scrapy


class Listing(scrapy.Item):
    price = scrapy.Field()
    currency = scrapy.Field()
    listing_type = scrapy.Field()
    surface = scrapy.Field()
    rooms = scrapy.Field()
    address = scrapy.Field()

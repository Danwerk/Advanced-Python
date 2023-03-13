"""
Creating a WEB Scraper
Start your scraper with the following console command:
$ scrapy runspider scraper1.py
"""
import scrapy


class BrickSetSpider(scrapy.Spider):
    """Brick spider class."""
    name = "brickset_spider"  # just a name for the spider.

    def start_requests(self):
        # a list of URLs that you start to crawl from. We'll start with one URL.
        url = "https://www.1a.ee/c/arvutitehnika-burootarbed/sulearvutid-ja-tarvikud/sulearvutid/373"

        # Set the headers here.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
        }

        yield scrapy.http.Request(url, headers=headers, encoding='utf8', )

    def parse(self, response):
        """
        Parser method for getting all laptops.

        Parser finds laptop name, price and image.
        """
        SET_SELECTOR = '.catalog-taxons-product__hover'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.catalog-taxons-product__name ::text'
            PRICE_SELECTOR = '.catalog-taxons-product-price__item-price span ::text'
            IMAGE_SELECTOR = '.catalog-taxons-product__image-anchor img ::attr(src)'
            yield {
                'Product name': string_cleaner(
                    (brickset.css(NAME_SELECTOR).extract_first()).strip().rstrip('"').strip()),
                'Price': brickset.css(PRICE_SELECTOR).extract_first(),
                'Picture href': brickset.css(IMAGE_SELECTOR).extract_first(),
            }
            NEXT_PAGE_SELECTOR = ".paginator__next ::attr(href)"
            next_page = response.css(NEXT_PAGE_SELECTOR).get()

            # Recursive call to find computers from next page
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )


def string_cleaner(rouge_text):
    """Format string."""
    return "".join(rouge_text.strip()).encode('windows-1252', 'ignore').decode("windows-1252")

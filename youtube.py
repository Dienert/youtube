import scrapy

class YotubeSpider(scrapy.Spider):
    name = "Youtube"

    canal = 'portadosfundos'

    start_urls = {
        'https://www.youtube.com/user/{}/videos'.format(canal)
    }

    def parse(self, response):
        divs = response.xpath('.//div[contains(@class, "yt-lockup-video")]')
        for div in divs:
            div_content = div.xpath('.//div[contains(@class, "yt-lockup-content")]')
            yield {
                'titulo' : div_content.xpath('.//a/text()').extract_first(),
                'link' : 'https://youtube.com/'+div_content.xpath('.//a/@href').extract_first()
            }
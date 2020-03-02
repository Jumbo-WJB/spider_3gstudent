import scrapy
from scrapy.http.request import Request

class ThreegstudentSpider(scrapy.Spider):
    name = "threegstudent"
    allowed_domains = ["3gstudent.github.io"]

    start_urls = (
        'https://3gstudent.github.io',
    )

    def parse(self, response):
        all_urls = response.xpath("//a/@href").getall()
        for url in all_urls:
            if url.startswith('/3gstudent.git'):
                url = response.urljoin(url)
                yield Request(url=url,callback=self.parse_content)

    def parse_content(self,response):
        yield {
            "title": response.xpath('//title/text()').get(),
            "content":response.xpath('//*[@id="main"]/article').get()
        }
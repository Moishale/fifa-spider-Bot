import scrapy
import json

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['www.futwiz.com']
    start_urls = ['https://www.futwiz.com/en/fifa22/players?page=1&order=bin&s=desc']

    def parse(self, response):
        for players in response.xpath("//tr[@class='table-row']") :
                    
                yield {
               "name" :  players.xpath(".//p[@class='name']//a//b/text()").get(),
               "rating" : players.css("div.otherversion22-txt::text").get(),
               "link" :"https://www.futwiz.com" +  players.xpath(".//p[@class='name']//a").attrib['href']
                }
        next_page = response.xpath("//div[@class='col-2 next']//a").attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

# link : players.xpath("//p[@class='name']//a").attrib['href']
# name : players.xpath("//p[@class='name']//a//b/text()")
# overoll : players.css("div.otherversion22-txt::text").get()

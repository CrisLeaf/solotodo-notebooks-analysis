import scrapy

class NBSpider(scrapy.Spider):
	name = "notebooks"
	start_urls = ["https://www.solotodo.cl/notebooks?ordering=offer_price_usd&"]

	def parse(self, response):
		for nb in response.xpath("//div[@class='d-flex flex-column category-browse-result']"):
			try:
				yield {
					"name": nb.xpath(".//h3/a/text()").get(),
					"price": nb.xpath(".//div[@class='d-flex flex-row justify-content-between align-items-center mt-auto pt-2']/div/a/text()").get(),
					"processor": nb.xpath(".//div[@class='description-container']/dl/dd[1]/text()").get(),
					"ram": nb.xpath(".//div[@class='description-container']/dl/dd[2]/text()").get(),
					"monitor": nb.xpath(".//div[@class='description-container']/dl/dd[3]/text()").get(),
					"storage": nb.xpath(".//div[@class='description-container']/dl/dd[4]/ul/li/text()").get(),
					"video-card": nb.xpath(".//div[@class='description-container']/dl/dd[5]/ul/li/text()").get(),
				}
			except:
				yield {
					"name": nb.xpath(".//h3/a/text()").get(),
					"price": nb.xpath(".//div[@class='d-flex flex-row justify-content-between align-items-center mt-auto pt-2']/div/a/text()").get(),
					"processor": nb.xpath(".//div[@class='description-container']/dl/dd[1]/text()").get(),
					"ram": nb.xpath(".//div[@class='description-container']/dl/dd[2]/text()").get(),
					"monitor": nb.xpath(".//div[@class='description-container']/dl/dd[3]/text()").get(),
					"storage": nb.xpath(".//div[@class='description-container']/dl/dd[4]/ul/li/text()").get(),
					"video-card": "NA",
				}
#		next_page = "https://www.solotodo.cl/notebooks" + response.css("a.page-link::attr(href)").getall()[-1]
#		if next_page is not None:
#			yield response.follow(next_page, callback=self.parse)

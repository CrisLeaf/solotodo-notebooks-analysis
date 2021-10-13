import scrapy
from nbscraper.items import NbscraperItem
from scrapy.loader import ItemLoader

class NBSpider(scrapy.Spider):
	name = "notebooks"
	start_urls = ["https://www.solotodo.cl/notebooks?ordering=offer_price_usd&"]

	def parse(self, response):
		for nb in response.xpath("//div[@class='d-flex flex-column category-browse-result']"):
			loader = ItemLoader(item=NbscraperItem(), selector=nb)
			loader.add_xpath("name", ".//h3/a/text()")
			loader.add_xpath("price", ".//div[@class='d-flex flex-row justify-content-between align-items-center mt-auto pt-2']/div/a")
			loader.add_xpath("processor", ".//div[@class='description-container']/dl/dd[1]")
			loader.add_xpath("ram", ".//div[@class='description-container']/dl/dd[2]")
			loader.add_xpath("screen", ".//div[@class='description-container']/dl/dd[3]")
			loader.add_xpath("storage", ".//div[@class='description-container']/dl/dd[4]/ul/li")
			loader.add_xpath("video_card", ".//div[@class='description-container']/dl/dd[5]/ul/li")
			loader.add_xpath("dedicated_video_card", ".//div[@class='description-container']/dl/dd[5]/ul/li[2]")
			yield loader.load_item()
		try:
			next_page = "https://www.solotodo.cl/notebooks" + response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
		except:
			next_page = None
		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)

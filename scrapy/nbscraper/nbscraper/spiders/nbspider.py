import scrapy

class NBSpider(scrapy.Spider):
	name = "notebooks"
	start_urls = ["https://www.solotodo.cl/notebooks?ordering=offer_price_usd&"]

	def parse(self, response):
		for products in response.css("div.d-flex.flex-column.category-browse-result"):
			try:
				yield {
					"name": products.css("div.d-flex.flex-column.category-browse-result a::text").get(),
					"price": products.css("div.d-flex.flex-column.category-browse-result div.price.flex-grow a::text").get(),
					"processor": products.css("div.d-flex.flex-column.category-browse-result div.description-container dd::text").getall()[0],
					"ram": products.css("div.d-flex.flex-column.category-browse-result div.description-container dd::text").getall()[1],
					"monitor": products.css("div.d-flex.flex-column.category-browse-result div.description-container dd::text").getall()[2],
					"storage": products.css("div.d-flex.flex-column.category-browse-result div.description-container li::text").getall()[0],
					"video-card": products.css("div.d-flex.flex-column.category-browse-result div.description-container li::text").getall()[1],
				}
			except:
				yield {
					"name": products.css("div.d-flex.flex-column.category-browse-result a::text").get(),
					"price": products.css("div.d-flex.flex-column.category-browse-result div.price.flex-grow a::text").get(),
					"processor": products.css("div.d-flex.flex-column.category-browse-result div.description-container dd::text").getall()[0],
					"ram": products.css("div.d-flex.flex-column.category-browse-result div.description-container dd::text").getall()[1],
					"monitor": products.css("div.d-flex.flex-column.category-browse-result div.description-container dd::text").getall()[2],
					"storage": products.css("div.d-flex.flex-column.category-browse-result div.description-container li::text").getall()[0],
					"video-card": "NA",
				}
		next_page = "https://www.solotodo.cl/notebooks" + response.css("a.page-link::attr(href)").getall()[-1]
		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)


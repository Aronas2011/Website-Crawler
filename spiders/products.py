import scrapy
import pandas as pd

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["sandbox.oxylabs.io"]

    start_urls = [
        f"https://sandbox.oxylabs.io/products?page={page}" for page in range(1, 10)
        ] 
    
    #some sites require you to extract the link for the next page button to move on to the next page


    def parse(self, response):
        for product in response.css("div.product-card"):
            yield{
                "Title" : product.css("h4.title::text").get(),
                "Price" : product.css("div.price-wrapper::text").get()
            }
  
#to run go to terminal and enter "scrapy crawl products -O {fileName}.csv
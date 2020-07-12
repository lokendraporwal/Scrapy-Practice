import scrapy


class CompanyDetailsSpider(scrapy.Spider):
    name = 'company_details'
    allowed_domains = ['in.finance.yahoo.com']
    start_urls = ['https://in.finance.yahoo.com/most-active//']

    def parse(self, response):
        company_names_list = response.xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[2]/text()'
            ).extract()
        company_price_list = response.xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[3]/text()'
            ).extract()

        count = len(company_names_list)

        for i in range(0,count):
            print(company_names_list[i], company_price_list[i])

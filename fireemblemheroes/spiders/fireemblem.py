import scrapy
from .urls import UrlSpider
from scrapy_splash import SplashRequest
import json

class FEHSpider(scrapy.Spider):
    name = "feh"

    def start_requests(self):
        with open('../../feed_exports/heroes.json', 'r') as f:
            data = json.load(f)
            for url in data:
                yield SplashRequest(url=url['urls'], callback=self.parse)
    
    def parse(self, response):
        yield {
            'Name': self.fullname(response),
            'Tier Rating': self.tier(response),
            'Movement Type': self.movement(response),
            "Weapon": self.weapon(response),
            "Total Stats": self.BST(response),
            "Recommended Builds": self.recommended_build(response),
            "Recommended IVs": self.recommended_IV(response),
            "Stats": self.five_star_hero_stats(response)
        }
    def fullname(self, response):
        return response.selector.xpath('//h1[@class="page-title"]/span/span/text()').get()

    def tier(self, response):
        path = response.selector.xpath("//div[@class='hero-rating']/a/img/@src").get()
        return path.split("/")[-1][0]

    def movement(self, response):
        return response.selector.xpath('//div[@id="hero-atts"]/div[1]/div/h2/a/div/span/text()').get()

    def weapon(self, response):
        return response.selector.xpath('//div[@id="hero-atts"]/div[2]/div/h2/a/div/span/text()').get()
    
    def BST(self, response):
        return response.selector.xpath('//div[@id="max-stats"]/span[2]/text()').get()

    def recommended_build(self, response):
        # Only returns optimal builds chosen by Gamepress
        skillset = []
        for table in response.selector.xpath('(//div[@class="optimal-build"])'):
            skillset.append({
                "Weapon": table.xpath('.//following-sibling::table/tbody/tr[1]/td[1]/a/text()').get(),
                "Assist": table.xpath('.//following-sibling::table/tbody/tr[2]/td[1]/a/text()').get(),
                "Special": table.xpath('.//following-sibling::table/tbody/tr[3]/td[1]/a/text()').get(),
                "A Skill": table.xpath('.//following-sibling::table/tbody/tr[1]/td[2]/a/text()').get(),
                "B Skill": table.xpath('.//following-sibling::table/tbody/tr[2]/td[2]/a/text()').get(),
                "C Skill": table.xpath('.//following-sibling::table/tbody/tr[3]/td[2]/a/text()').get(),
                "S Skill": table.xpath('.//following-sibling::table/tbody/tr[4]/td/a/text()').get(),
                "SP": table.xpath('.//following-sibling::table/tbody/tr[4]/td/text()').get()
            })
        return skillset

    def recommended_IV(self, response):
        # Returns the ratings worst, average, or best for each stat
        IVs = []
        for iv in response.selector.xpath('//table[@id="iv-set-table"]/tbody/tr[2]'):
            IVs.append({
                "HP": iv.xpath('.//td[1]/div/div/h2/a/div/span/text()').get(),
                "ATK": iv.xpath('.//td[2]/div/div/h2/a/div/span/text()').get(),
                "SPD": iv.xpath('.//td[3]/div/div/h2/a/div/span/text()').get(),
                "DEF": iv.xpath('.//td[4]/div/div/h2/a/div/span/text()').get(),
                "RES": iv.xpath('.//td[5]/div/div/h2/a/div/span/text()').get()
            })
        return IVs
    
    def five_star_hero_stats(self,response):
        stats = []
        for stat in response.selector.xpath('//div[@id="stats-iv"]'):
            stats.append({
                # Lv1 Stats
                "1": {
                    "No Weapon": {
                        # Format is [Low, Medium, High]. If only Medium exists (i.e. Alfonse), then null is returned for Low and High.
                        "HP": [stat.xpath('.//table[1]/tbody/tr[2]/td[1]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[1]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[4]/td[1]/span[1]/text()').get()],
                        "ATK": [stat.xpath('.//table[1]/tbody/tr[2]/td[2]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[2]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[4]/td[2]/span[1]/text()').get()],
                        "SPD": [stat.xpath('.//table[1]/tbody/tr[2]/td[3]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[3]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[4]/td[3]/span[1]/text()').get()],
                        "DEF": [stat.xpath('.//table[1]/tbody/tr[2]/td[4]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[4]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[4]/td[4]/span[1]/text()').get()],
                        "RES": [stat.xpath('.//table[1]/tbody/tr[2]/td[5]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[5]/span[1]/text()').get(), stat.xpath('.//table[1]/tbody/tr[4]/td[5]/span[1]/text()').get()]
                    },
                    "Weapon" : {
                        "HP": [stat.xpath('.//table[1]/tbody/tr[2]/td[1]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[1]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/tr[4]/td[1]/span[2]/text()').get()],
                        "ATK": [stat.xpath('.//table[1]/tbody/tr[2]/td[2]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[2]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/tr[4]/td[2]/span[2]/text()').get()],
                        "SPD": [stat.xpath('.//table[1]/tbody/tr[2]/td[3]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[3]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/tr[4]/td[3]/span[2]/text()').get()],
                        "DEF": [stat.xpath('.//table[1]/tbody/tr[2]/td[4]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[4]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/r[4]/td[4]/span[2]/text()').get()],
                        "RES": [stat.xpath('.//table[1]/tbody/tr[2]/td[5]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/tr[3]/td[5]/span[2]/text()').get(), stat.xpath('.//table[1]/tbody/tr[4]/td[5]/span[2]/text()').get()]
                    }
                },
                # Lv40 Stats
                "40": {
                    "No Weapon": {
                        "HP": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[1]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[1]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[4]/td[1]/span[1]/text()').get()],
                        "ATK": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[2]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[2]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[4]/td[2]/span[1]/text()').get()],
                        "SPD": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[3]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[3]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[4]/td[3]/span[1]/text()').get()],
                        "DEF": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[4]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[4]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[4]/td[4]/span[1]/text()').get()],
                        "RES": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[5]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[5]/span[1]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[4]/td[5]/span[1]/text()').get()]
                    },
                    "Weapon" : {
                        "HP": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[1]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[1]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[4]/td[1]/span[2]/text()').get()],
                        "ATK": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[2]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[2]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[4]/td[2]/span[2]/text()').get()],
                        "SPD": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[3]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[3]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[4]/td[3]/span[2]/text()').get()],
                        "DEF": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[4]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[4]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/r[4]/td[4]/span[2]/text()').get()],
                        "RES": [stat.xpath('.//table[contains(@id, "max")]/tbody/tr[2]/td[5]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[3]/td[5]/span[2]/text()').get(), stat.xpath('.//table[contains(@id, "max")]/tbody/tr[4]/td[5]/span[2]/text()').get()]
                    }
                }
            })
        return stats
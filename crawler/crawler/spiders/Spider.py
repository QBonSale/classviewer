from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from crawler.items import CourseItem

class MySpider(Spider):
	name = 'UCLA'
	allowed_domains = ['ucla.edu']
	#start_urls = ['http://www.registrar.ucla.edu/']
	start_urls = ['http://www.registrar.ucla.edu/schedule/detselect.aspx?termsel=15S&subareasel=COM+SCI&idxcrs=0111++++']
	def parse(self, response):
		self.log('Scraped: %s' % response.url)
		sel = Selector(response)
		BodyContent = sel.xpath('//*[@id="ctl00_BodyContentPlaceHolder_detselect_pnlBodyContent"]')
		# general information
		Semester = BodyContent.xpath('table[1]/tr[1]/td/span/text()').extract()
		Subarea = BodyContent.xpath('table[1]/tr[2]/td/span/text()').extract()
		GeneralNotes = BodyContent.xpath('table[1]/tr[3]/td/span/text()').extract()
		ClassNotes = BodyContent.xpath('table[1]/tr[4]/td/span/text()').extract()
		Title = sel.xpath('//*[@id="ctl00_BodyContentPlaceHolder_detselect_pnlBodyContent"]/table[2]').re(r'"coursehead">([^<]*)')    # no idea why normal way won't work
		
        # section specified information
		sections = sel.xpath('//*[@class="dgdClassDataHeader"]/..')
		for section in sections:
			lecture = section.xpath('tr[2]')
			item = CourseItem()
			item['Semester'] = Semester
			item['Subarea'] = Subarea
			item['GeneralNotes'] = GeneralNotes
			item['ClassNotes'] = ClassNotes
			item['Title'] = Title
			#item['Instructor'] = response.xpath(
			item['IDNumber'] = lecture.xpath('td[@class="dgdClassDataColumnIDNumber"]/span/span/a/text()').extract()
			item['ActType'] = lecture.xpath('td[@class="dgdClassDataActType"]/span/span/text()').extract()
			item['Section'] = lecture.xpath('td[@class="dgdClassDataSectionNumber"]/span/span/text()').extract()
			item['Days'] = lecture.xpath('td[@class="dgdClassDataDays"]/span/span/text()').extract()
			item['TimeStart'] = lecture.xpath('td[@class="dgdClassDataTimeStart"]/span/span/text()').extract()
			item['TimeStop'] = lecture.xpath('td[@class="dgdClassDataTimeEnd"]/span/span/text()').extract()
			item['Building'] = lecture.xpath('td[@class="dgdClassDataBuilding"]/span/span/text()').extract()
			item['Room'] = lecture.xpath('td[@class="dgdClassDataRoom"]/span/span/text()').extract()
			item['Restrict'] = lecture.xpath('td[@class="dgdClassDataRestrict"]/span/span/text()').extract()
			item['EnrollTotal'] = lecture.xpath('td[@class="dgdClassDataEnrollTotal"]/span/span/text()').extract()
			item['EnrollCap'] = lecture.xpath('td[@class="dgdClassDataEnrollCap"]/span/span/text()').extract()
			item['WaitlistTotal'] = lecture.xpath('td[@class="dgdClassDataWaitListTotal"]/span/span/text()').extract()
			item['WaitlistCap'] = lecture.xpath('td[@class="dgdClassDataWaitListCap"]/span/span/text()').extract()
			item['Status'] = lecture.xpath('td[@class="dgdClassDataStatus"]/span/span/span/text()').extract()
			yield item

			labs = section.xpath('tr[position()>2]')   # first one is header, second is main session

			for lab in labs:
				item = CourseItem()
				item['Semester'] = Semester
				item['Subarea'] = Subarea
				item['GeneralNotes'] = GeneralNotes
				item['ClassNotes'] = ClassNotes
				item['Title'] = Title
				#item['Instructor'] = response.xpath(
				item['IDNumber'] = lab.xpath('td[@class="dgdClassDataColumnIDNumber"]/span[1]/a[1]/text()').extract()
				item['ActType'] = lab.xpath('td[@class="dgdClassDataActType"]/span/text()').extract()
				item['Section'] = lab.xpath('td[@class="dgdClassDataSectionNumber"]/span/text()').extract()
				item['Days'] = lab.xpath('td[@class="dgdClassDataDays"]/span/text()').extract()
				item['TimeStart'] = lab.xpath('td[@class="dgdClassDataTimeStart"]/span/text()').extract()
				item['TimeStop'] = lab.xpath('td[@class="dgdClassDataTimeEnd"]/span/text()').extract()
				item['Building'] = lab.xpath('td[@class="dgdClassDataBuilding"]/span/text()').extract()
				item['Room'] = lab.xpath('td[@class="dgdClassDataRoom"]/span/text()').extract()
				item['Restrict'] = lab.xpath('td[@class="dgdClassDataRestrict"]/span/text()').extract()
				item['EnrollTotal'] = lab.xpath('td[@class="dgdClassDataEnrollTotal"]/span/text()').extract()
				item['EnrollCap'] = lab.xpath('td[@class="dgdClassDataEnrollCap"]/span/text()').extract()
				item['WaitlistTotal'] = lab.xpath('td[@class="dgdClassDataWaitListTotal"]/span/text()').extract()
				item['WaitlistCap'] = lab.xpath('td[@class="dgdClassDataWaitListCap"]/span/text()').extract()
				item['Status'] = lab.xpath('td[@class="dgdClassDataStatus"]/span/span/text()').extract()    #two span for red/green
				yield item


# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
	Semester = scrapy.Field()
	Subarea  = scrapy.Field()
	GeneralNotes = scrapy.Field()
	ClassNotes = scrapy.Field()
	Title = scrapy.Field()
	Instructor = scrapy.Field()
	IDNumber = scrapy.Field()
	ActType = scrapy.Field()
	Section = scrapy.Field()
	Days = scrapy.Field()
	TimeStart = scrapy.Field()
	TimeStop = scrapy.Field()
	Building = scrapy.Field()
	Room = scrapy.Field()
	Restrict = scrapy.Field()
	EnrollTotal = scrapy.Field()
	EnrollCap = scrapy.Field()
	WaitlistTotal = scrapy.Field()
	WaitlistCap = scrapy.Field()
	Status = scrapy.Field()


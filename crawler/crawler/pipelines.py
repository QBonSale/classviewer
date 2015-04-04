# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

""" 
Cleans newlines and linefeeds from all fields in the item 
""" 
class SpacePipeline(object): 
	def process_item(self, item, spider): 
		# process Instructor garbage
		p = re.compile(u'(\\xa0)+ ') 
		item['Instructor'] = map(lambda x: p.sub('', x), item['Instructor']) 
		p = re.compile(r'( )+/') 
		item['Instructor'] = map(lambda x: p.sub(' /', x), item['Instructor']) 
		p = re.compile('\s+$') 

		# general remove trailing spaces
		for k in item.fields.iterkeys(): 
			item[k] = map(lambda x: p.sub('', x), item[k]) 
		return item 

'''
Store into mysql
'''
class SQLStore(object):
  def __init__(self):
	self.conn = pymssql.connect(host='', user='', password='', database='')
	self.cursor = self.conn.cursor()


	def process_item(self, item, spider): 
		try:
			self.cursor.execute("INSERT INTO Movie(Description, Location,Title) VALUES (%s, %s, %s)", (item['Description'], item['Location'], item['Title']))
			self.conn.commit()

		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		return item
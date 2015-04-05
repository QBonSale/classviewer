# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import time
import MySQLdb

def convertTimestampToSQLDateTime(value):
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(value))

def convertSQLDateTimeToTimestamp(value):
	return time.mktime(time.strptime(value, '%Y-%m-%d %H:%M:%S'))

def check_none(l):
	if not l:
		return None
	else:
		return l[0]

# format to %H:%M:00
def process_time(value):
	if value:
		value = value.split(':')
		if value[1][-1]=='P' and value[0]!='12':
			value[0] = str(int(value[0])+12)
		value[1] = value[1][:-1]
		value = ':'.join(value)
		print value
	return value+":00"

""" 
Cleans newlines and linefeeds from all fields in the item 
""" 
class SpacePipeline(object): 
	def process_item(self, item, spider): 
		# process Instructor garbage
		p = re.compile(u'(\\xa0)+ ?') 
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
		self.conn = MySQLdb.connect(host='localhost', user='root', passwd='lahacks2015', db='classviewer')
		self.cursor = self.conn.cursor()
	
	def process_item(self, item, spider): 
		try:
			# quarter & year
			Term = item['Semester'][0].split(' ')
			quarter = Term[0]	# char(1) 
			year = int(Term[1])	# int(11)
			print 'year: '+str(year)  

			if quarter == 'Summer':
				quarter = '1'
			else:
				quarter = quarter[0]
			print 'quarter: '+quarter  

			section_id_number= int(item['IDNumber'][0])
			print 'section_id_number: '+str(id_number)

			major = item['Subarea'][0]	# varchar(10) 
			course_number = item['Title'][0]
			course_number = course_number[len(major):] # get rid of major and following space
			while course_number[0]==' ':
				course_number = course_number[1:]
			course_number = course_number.split(' ')[0] 
			print 'major: '+major
			print 'course_number: '+course_number

			#possibly null
			professor = check_none(item['Instructor'])	# varchar(100)
			course_type = check_none(item['ActType'])	# varchar(5)
			building = check_none(item['Building'])	# varchar(100) 
			room = check_none(item['Room'])	# varchar(10)
			days = check_none(item['Days']) # varchar(7) 
			
			if professor:
				print 'professor: '+professor
			if course_type:
				print 'course_type: '+course_type
			if building:
				print 'building: '+building
			if room:
				print 'room: '+room
			if days:
				print 'days: '+days

			# TODO: convert during insertion using sql
			start = check_none(item['TimeStart'])
			start = process_time(start)
			stop = check_none(item['TimeStop'])  
			stop = process_time(stop)

			if not item['Restrict']:
				rest = None
			elif item['Restrict'][0]=='Yes':
				rest = 1
			else:
				rest = 0

			Section = item['Section'][0]
			sec =  re.search('[A-Za-z]+', Section)
	  		if section_id_number:
	  			sec = sec.group() # get first group
	  			print 'sec: '+sec
			lecture_number = re.search('[0-9]+', Section)
			if lecture_number:
				lecture_number = int(lecture_number.group())
				print 'lecture_number: '+str(lecture_number)

			course_title = item['Title'][0] # varchar(255)

			snapshot_time = item['TimeStamp'][0] #string

			num_en = check_none(item['EnrollTotal'])
			if num_en:
				num_en = int(num_en)
			en_cap = check_none(item['EnrollCap'])
			if en_cap:
				en_cap = int(en_cap)
			num_wl = check_none(item['WaitlistTotal'])
			if num_wl:
				num_wl = int(num_wl)
			wl_cap = check_none(item['WaitlistCap'])
			if wl_cap:
				wl_cap = int(wl_cap)

			status = check_none(item['Status'])

			cmd = "INSERT INTO class(year, quarter,major,course_number,professor,type,building,room,days,start,stop,rest,lecture_number,course_title) VALUES (%d, '%s', '%s','%s', '%s','%s', '%s','%s', '%s','%s','%s',%d,%d,'%s');"% (year,quarter,major,course_number,professor,course_type,building,room,days,start,stop,rest,lecture_number,course_title)
			self.cursor.execute(cmd)

			cmd = "INSERT INTO class_over_time(snapshot_time,num_en,en_cap,num_wl,wl_cap,status,year,quarter,course_number,lecture_number) VALUES ('%s',%d,%d,%d,%d,'%s',%d,'%s','%s',%d);"%(snapshot_time,num_en,en_cap,num_wl,wl_cap,status,year,quarter,course_number,lecture_number)
			self.cursor.execute(cmd)

			cmd = "INSERT INTO section(section_id_number,type,building,room,days,start,stop,rest,lecture_number,year) VALUES (%d,'%s', '%s','%s', '%s','%s','%s',%d,%d,%d);"% (section_id_number,course_type,building,room,days,start,stop,rest,lecture_number,year)
			self.cursor.execute(cmd)

			cmd = "INSERT INTO section_over_time(snapshot_time,num_en,en_cap,num_wl,wl_cap,status,year,quarter,course_number,lecture_number) VALUES ('%s',%d,%d,%d,%d,'%s',%d,'%s','%s',%d,'%s');"%(snapshot_time,num_en,en_cap,num_wl,wl_cap,status,year,quarter,course_number,lecture_number,sec)
			self.cursor.execute(cmd)

			self.conn.commit()

		except MySQLdb.Error, e:
			try:
				print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
			except IndexError:
				print "MySQL Error: %s" % str(e)
		except AttributeError:
			print "!!!!!!!!!!!Entry Dropped!!!!!!!!!!!!!!!!!"

		return item


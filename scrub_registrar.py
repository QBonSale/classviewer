#!/usr/bin/env python2

from selenium import webdriver


def get_major_list():
    driver = webdriver.Firefox()
    driver.get("http://www.registrar.ucla.edu/schedule/schedulehome.aspx")
    options = driver.find_element_by_id("ctl00_BodyContentPlaceHolder_SOCmain_lstSubjectArea")
    options_list = []
    for element in options.find_elements_by_tag_name("option"):
        options_list.append(element.get_attribute("value"))
    driver.close()
    driver.quit()
    return options_list

def get_term_list():
    term_list=[]
    #TODO: verify this range
    for year in range(1999,2015):
        #TODO: add summer
        for term in ['F','W','S']:
            term_list.append(str(year)[2:]+term)
    return term_list

def print_url(major, term):
    #TODO: handle spaces in the url
    print "http://www.registrar.ucla.edu/schedule/crsredir.aspx?termsel=" + term + "&subareasel="+ major
    return


majors = get_major_list()
terms = get_term_list()
for major in majors:
    for term in terms:
        print_url(major,term)

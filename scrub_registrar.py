#!/usr/bin/env python2

from selenium import webdriver


def major_list():
    driver = webdriver.Firefox()
    driver.get("http://www.registrar.ucla.edu/schedule/schedulehome.aspx")
    options = driver.find_element_by_id("ctl00_BodyContentPlaceHolder_SOCmain_lstSubjectArea")
    options_list = []
    for element in options.find_elements_by_tag_name("option"):
        options_list.append(element.get_attribute("value"))
    driver.close()
    driver.quit()
    return options_list

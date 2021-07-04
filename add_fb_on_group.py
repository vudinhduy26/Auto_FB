# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:21:30 2021

@author: duy
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 09:22:58 2021

@author: duy
"""

from selenium import webdriver
import time

email = '0388832737'
password = 'DUONGTHOI)^'

#bat chrome vs selenium
chrome = webdriver.Chrome(executable_path=r"C:\Users\duy\Desktop\instagram\InstagramBot\chromedriver.exe")
time.sleep(2)

#maximize the window size  
chrome.maximize_window()
#navigate to the url
chrome.get("https://www.facebook.com/")
time.sleep(4)

user = chrome.find_element_by_name("email")
user.send_keys(email)

passw = chrome.find_element_by_name("pass")
passw.send_keys(password)
time.sleep(3)

log_fb = chrome.find_element_by_name("login")
log_fb.click()
time.sleep(4)
a = 516
group_member = input("members_things_in_common of group : ")
chrome.get(group_member)
time.sleep(10)
for i in range(1,100):
    if i%2==0:
        chrome.execute_script("window.scrollTo(0,{});".format(a))
        a+=160
    time.sleep(2)
    try:
        add_friend = chrome.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div[{}]/div/div/div[2]/div[2]/div/div/div/div".format(i))
        add_friend.click()
    except:
        continue
    time.sleep(1)
    if i == 99:
        break
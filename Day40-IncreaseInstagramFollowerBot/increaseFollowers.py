from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint, choice
import pandas as pd

prev_user_list = [] 
new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0
f = 0
fail_Ip = 0 

chromedriver_path = 'F:/Projrct/hobby/python_repo/ProjectInsta/chromedriver.exe' # Change this to your own chromedriver path! I have included the exe file in this project folder

webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('dhairyashil_patil09')#Follow me at https://www.instagram.com/dhairyashil_patil09/
password = webdriver.find_element_by_name('password')
password.send_keys('<Password>')

#Click login
button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(3)

#Click Not Now !! comment these last 2 lines out, if you don't get a pop up ask !!
notnow = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
notnow.click() 

#notification not now !! comment these last 2 lines out, if you don't get a pop up ask !!
notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() 

hashtag_list = ['newtoinstagram','life', 'follow', 'follow4follow','instalike', 'f4f', 'ootd','photooftheday', 'travel', 'cute', 'night', 'friends', 'sunset','happiness', 'apni_duniya', 'sunset','mast',]
Comment_list = ['Oh Mah Gosh!!', 'This Pic is awesome', 'Great', 'Your Galary is amazing.' , 'So cool! :)', 'Nice gallery!!', 'Nice :)', 'Really cool!', 'Awesome',]

# If running on the same day. It will use the user list to check and skip to like and follow
prev_user_list = pd.read_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d")), delimiter=',').iloc[:,1:2] # useful to build a user log
prev_user_list = list(prev_user_list['0'])


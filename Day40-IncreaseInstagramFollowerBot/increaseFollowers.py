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


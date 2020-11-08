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

for hashtag in hashtag_list:
    f = 0
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(randint(1,2))    
    try:        
        for x in range(1,200):
            try:
                username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[1]/span/a').text
                if username not in prev_user_list:
                    # If we already follow, do not unfollow
                    if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[2]/button').click()
                        new_followed.append(username)
                        followed += 1
                        # Liking the picture
                        button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[1]/button')
                        button_like.click()
                        likes += 1
                        sleep(randint(18,25))
                        # Comments and tracker
                        comm_prob = randint(1,10)
                        print('{}_{}: {}'.format(hashtag, x,comm_prob))
                        if comm_prob > 8:
                            comments += 1
                            webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[2]/button').click()
                            comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/div[3]/section[3]/div/form/textarea')

                            comment_box.send_keys(choice(Comment_list))
                            sleep(1)
                            # Enter to post comment
                            comment_box.send_keys(Keys.ENTER)
                            sleep(randint(22,28))
                    # Next picture
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(25,29))
                else:
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(20,26))    
            except:
                if f < 10:
                    print("Failed:",f)
                    f += 1
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(25,29))
                    continue
                else:
                    fail_Ip = int(input("Continue?(1/0):"))
                    if fail_Ip == 1:
                        print("User Continued")
                        f = 0
                        continue
                    else:
                        print("Finaly Failed")
                        break
            
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        print("next Tag")
        continue


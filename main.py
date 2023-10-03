from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time


PASSWORD_INS = "YOUR INSTAGRAM PASSWORD"
NAME = "EMAIL"


#this bot is very usefull to those who want more followers just you need to find famous page show stuff like your page

#the name of famous instagram page show stuff like your page
SEARCH = "benny_productions"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = None

class InstaFollower:



    def login(self):
        global driver
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.instagram.com/")
        time.sleep(2)

        username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(NAME)

        time.sleep(2)

        password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD_INS)

        time.sleep(2)

        login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(5)

    def find_followers(self):
        driver.get(f"https://www.instagram.com/{SEARCH}/followers/")
        time.sleep(10)
        modal = driver.find_element(By.CSS_SELECTOR, 'div._aano')
        for i in range(5):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_butons = driver.find_elements(By.CSS_SELECTOR, 'div._aano button')
        #you can change number 20 to anynumber it's all about you how many people you want follow
        for item in all_butons[:20]:
            try:
                item.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                unfollow = driver.find_element(By.CSS_SELECTOR, 'button._a9--._a9-_')
                unfollow.click()






instafollower = InstaFollower()
instafollower.login()
instafollower.find_followers()
instafollower.follow()





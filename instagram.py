from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        usernameInput = self.browser.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def getInstagramFollowers(self):
        self.browser.get(f'https://www.instagram.com/{username}/followers/')
        time.sleep(10)

        followers = []
        items = self.browser.find_elements(By.CSS_SELECTOR, 'div.x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1'
                                           )
        for i in items:
            followers.append(i.text)

        print(followers)
        print(len(followers))


instagram = Instagram(username, password)
instagram.signIn()
instagram.getInstagramFollowers()

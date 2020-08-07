from selenium import webdriver
import time


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        time.sleep(10)

    def login(self):
        self.driver.get('https://tinder.com')
        time.sleep(30)
        while True:
            try:
                login_btn = self.driver.find_element_by_xpath(
                    '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div/div/button')
                login_btn.click()
            except:
                try:
                    login_btn = self.driver.find_element_by_id(
                        '//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div[1]/span/div[1]/div/button')
                    login_btn.click()
                except:
                    break
                else:
                    break
            else:
                break
        time.sleep(10)
        while True:
            try:
                self.driver.switch_to_window(self.driver.window_handles[1])
                email_id = self.driver.find_element_by_xpath(
                    '//*[@id="identifierId"]')
                email_id.send_keys('kshitizsareen709@gmail.com')
                nextemailbtn = self.driver.find_element_by_xpath(
                    '//*[@id="identifierNext"]/div/button')
                nextemailbtn.click()
            except:
                continue
            else:
                break

        time.sleep(10)
        while True:
            try:
                password = self.driver.find_element_by_xpath(
                    '//*[@id="password"]/div[1]/div/div[1]/input')
                password.send_keys('0756454835')
                password_btn = self.driver.find_element_by_xpath(
                    '//*[@id="passwordNext"]/div/button')
                password_btn.click()
            except:
                continue
            else:
                break
        time.sleep(10)

    def OperateTinder(self):
        self.driver.switch_to_window(self.driver.window_handles[0])
        while True:
            try:
                AllowButton = self.driver.find_element_by_xpath(
                    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                AllowButton.click()
                time.sleep(5)
                EnableButton = self.driver.find_element_by_xpath(
                    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                EnableButton.click()
                time.sleep(5)
            except:
                continue
            else:
                break

    def like(self):
        self.driver.switch_to_window(self.driver.window_handles[0])
        while True:
            try:
                Acceptbtn = self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
                Acceptbtn.click()
            except:
                continue
            else:
                break
        count = 0
        while True:
            try:
                time.sleep(3)
                likeButton = self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
                likeButton.click()
                count += 1
                print(count)

            except:
                continue
            else:
                if count == 10:
                    break


bot = TinderBot()
bot.login()
bot.OperateTinder()
bot.like()

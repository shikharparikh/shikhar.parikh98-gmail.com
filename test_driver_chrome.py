from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import os
from time import sleep


email = 'shikhar.p@somaiya.edu'
password = 'xHFT2020@'
stock_name = 'Axis Bank'
class TradeBot():
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/aadit/Downloads/chromedriver')

    def login(self):

        self.driver.get('https://moneybhai.moneycontrol.com')

        sleep(2)

        continue_btn = self.driver.find_element_by_xpath('//*[@id="myButton"]')
        continue_btn.click()

        skip_btn = self.driver.find_element_by_xpath('//*[@id="intro4"]/a')
        skip_btn.click()

        play_btn = self.driver.find_element_by_xpath('//*[@id="loginbtn"]')
        play_btn.click()

        self.driver.switch_to.frame("myframe")
        sleep(2)

        email_in = self.driver.find_element_by_xpath("//input[@form-name='login_form' and @name='email']")
        email_in.send_keys(email)

        pwd_in = self.driver.find_element_by_xpath("//input[@form-name='login_form' and @name='pwd']")
        pwd_in.send_keys(password)

        new_login = self.driver.find_element_by_xpath("//button[@id='ACCT_LOGIN_SUBMIT']")
        new_login.click()
        sleep(2)

        transact_link = link = self.driver.find_element_by_link_text('Transact')
        
        transact_link.click()
        sleep(1)

        email_in = self.driver.find_element_by_class_name('search-input')
        email_in.send_keys(stock_name)
        sleep(3)
       

        add_btn = self.driver.find_element_by_xpath('//*[@id="auto-suggest"]/ul/li/button')
        add_btn.click()
        sleep(3)

        buy_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]')
        buy_button.click()

        quantity = self.driver.find_element_by_xpath('//*[@id="AS-BSE"]/div[2]/div[1]/label/input')
        quantity.send_keys("100")

        current_price = self.driver.find_element_by_xpath('//*[@id="txt_mktprice"]').get_attribute('value')
        print(current_price,"and ",type(current_price))
        current_price = float(current_price)
        target = current_price + 15
        stop_loss = current_price - 15 

        investment_amount = self.driver.find_element_by_id('invest_amt')
        investment_amount.click()

        target_input = self.driver.find_element_by_xpath('//*[@id="target"]')
        target_input.send_keys(str(target))

        stoploss_input = self.driver.find_element_by_xpath('//*[@id="stop_loss"]')
        stoploss_input.send_keys(str(stop_loss))

        submit_butn =  self.driver.find_element_by_xpath('//*[@id="btn_submit"]')
        submit_butn.click()       



obj= TradeBot()
obj.login()
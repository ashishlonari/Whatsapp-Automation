from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
# To get Whattsapp URL

name = input("Enter the name of user or group : ")
msg = input("Enter your Message :")
count = int(input("Enter the Count How many times you want to send msg :"))
delay = int(input("Enter the delay between the messages to be sent  in seconds:"))

input("Enter anything after Scanning The QR Code")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3uMse')

for i in range(count):
    msg_box.send_keys(msg)
    btn = driver.find_element_by_class_name('_1U1xa')
    btn.click()
    time.sleep(delay)

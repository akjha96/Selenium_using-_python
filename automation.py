from selenium import webdriver


chrome_browser = webdriver.Chrome('./chromedriver')
# print(chrome_browser)
chrome_browser.maximize_window()

chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button .get_attribute('innerHTML'))

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am very happy! Yippi ;-)')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')
print(output_message.text)

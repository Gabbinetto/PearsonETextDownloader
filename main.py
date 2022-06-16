from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import webbrowser as wb

path = 'C:\msedgedriver.exe'

user = input('Username: ')
password = input('Password: ')
print('''
╒=================================╕
| NOTE: The pages start from zero |
╘=================================╛
''')
start_page = int(input('Starting page: '))
pages = [i for i in range(2, int(input('Number of pages: ')))]
pages_num = int(input('Number of pages to save: '))


clear = lambda: os.system('cls')
clear()

driver = webdriver.Edge(path)

print('Open the product and take the url, then close the browser and paste the link here:')
driver.get(input())

sleep(5)

user_box = driver.find_element_by_id('username')
user_box.send_keys(user)

password_box = driver.find_element_by_id('password')
password_box.send_keys(password)
password_box.send_keys(Keys.RETURN)
print('LOGGED IN')
sleep(15)

image_element = driver.find_element_by_id('docViewer_ViewContainer_BG_0')
image_url : str = image_element.get_attribute('src')

print(image_url)

driver.quit()

links = []
for i in range(start_page, start_page + pages_num):
    links.append(
        image_url.replace('page0', f'page{i}')
    )
delay = float(input('Loading delay (leave blank for default 1.5 seconds): '))
for i in range(len(links)):
    wb.open(links[i], new=2)
    sleep(delay)

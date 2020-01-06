#BASIC ONLINE CHECKER

import selenium
from time import sleep

user_name = 'Mom'

options = selenium.webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Sohail21400\\Desktop\\x")
driver = selenium.webdriver.Chrome(
    executable_path='C:\\Users\\Sohail21400\\Downloads\\chromedriver_win32\\chromedriver.exe',
    options=options)

driver.get("https://web.whatsapp.com/")

sleep(15)

# searc_box is the text area to search user
search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')
# typing the name to search
search_box.send_keys(user_name)

user_icon = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[2]')
sleep(3)
user_icon.click()
sleep(4)

while True:
    # if the user is offline the element won't be visible so trial and error
    try:
        is_online = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span').text
        if is_online == 'online':
            print(f'{user_name} is online')
        else:
            print(f'{user_name} is offline')
        sleep(10)

    except selenium.common.exceptions.NoSuchElementException:
        print(f'{user_name} is offline')
        sleep(10)

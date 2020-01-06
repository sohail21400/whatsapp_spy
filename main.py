# ONLINE CHECKER WITH CSV DATABASE


import selenium
from selenium import webdriver
from time import sleep
import csv
from datetime import datetime
# NOTE: Timezone is not added
# least count is 10 seconds

user_name = 'Mom'

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Sohail21400\\Desktop\\x")
driver = webdriver.Chrome(
    executable_path='C:\\Users\\Sohail21400\\Downloads\\chromedriver_win32\\chromedriver.exe',
    options=options)

driver.get("https://web.whatsapp.com/")
is_main_page_loaded = False

sleep(10)
try_time = 3
i = 0
while not is_main_page_loaded and try_time > i:
    try:
        search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')
        search_box.send_keys(user_name)
        sleep(2)  # time to search user WE CAN ALSO IMPLEMENT A TRY EXCEPT BLOCK HERE BECAUSE THE SEARCH TIME MAY VARY
        user_icon = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[2]')
        user_icon.click()
        sleep(4)  # time to load user chat

        is_main_page_loaded = True

    except selenium.common.exceptions.NoSuchElementException:
        # this means the main WhatsApp page is not even loaded
        print('Something went wrong.. trying again')
        sleep(7)  # extended time to load the main page

if not is_main_page_loaded:
    print("Couldn't load the website, check your connection and try again.")
    exit()


online_status = False
old_status = False

with open('online_status.csv', 'a') as csv_file:
    # 'a' stands for append mode other wise it will rewrite the data
    writer = csv.writer(csv_file)

    while True:  # Loop to continuously check the status
        try:  # if the user is offline the element won't be visible so trial and error
            is_online = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span').text
            if is_online == 'online':
                online_status = True
            sleep(10)
        except selenium.common.exceptions.NoSuchElementException:
            online_status = False
            sleep(10)

        if old_status != online_status:
            current_time = datetime.now().strftime("%H:%M:%S")
            current_date = datetime.now().strftime("%d:%m:%y")
            current_day = datetime.now().strftime("%a")

            writer.writerow([current_date, current_day, current_time, online_status])
            old_status = online_status

        if online_status:
            print(f'{user_name} is online')
        else:
            print(f'{user_name} is offline')


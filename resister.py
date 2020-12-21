import time
import pytz
import datetime
from selenium import webdriver
import random
from ifttt import *
import os

username = os.environ["USER_ID"]
password = os.environ["PASSWORD"]
url = "https://apdb.gifu-nct.ac.jp/shc/index.php"


def resister():
    temperatur = "0"

    try:
        driver_path = "/app/.chromedriver/bin/chromedriver"
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.get(url)

        driver.find_element_by_name("username").send_keys(username)

        driver.find_element_by_name("password").send_keys(password)

        driver.find_element_by_xpath("//form/input").click()

        while driver.current_url != "https://apdb.gifu-nct.ac.jp/shc/index.php":
            time.sleep(1)
        print("logined.")

        now = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
        driver.find_element_by_id(now.date()).find_elements_by_class_name("status_yellow")[1].click()
        driver.switch_to.window(driver.window_handles[1])
        temperatur = "36." + str(random.randint(0, 9))
        
        for e in driver.find_elements_by_tag_name("input"):
            if e.get_attribute("name") == "question:1_answer":
                e.send_keys(temperatur)
            elif e.get_attribute("name") == "question:2_choice0" and e.get_attribute("value") == "1":
                e.click()
        driver.find_element_by_name("next").click()
    except:
        ifttt_ng()
        return
    ifttt_ok(temperatur)
    
    print("resisted.")
    



if __name__ == "__main__":
    resister()

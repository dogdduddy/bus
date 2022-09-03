import datetime
import private
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import schedule
import time


### 입력 정보
url = private.url
my_id = private.id
my_pw = private.pw
goto = private.goto
bustime = private.bustime
startTime = private.startTime


### 기본 셋팅
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    drive = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    # 로딩 최대 기다리는 시간, n초 안에 로딩 완료시 바로 실행
    drive.implicitly_wait(2)
    drive.get(url)
    return drive

def login():
    driver.find_element(By.ID, "id").send_keys(my_id)
    driver.find_element(By.ID, "pass").send_keys(my_pw)
    # 로그인 버튼 클릭
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/ng-view/div/div/div/form/fieldset/button").click()

def alert():
    ### Alert 처리
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    Alert(driver).accept()

def bus():
    ### 버스예약
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/ng-view/div/div/div/a[1]").click()
    # 등하교
    if goto == "등교":
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/ng-view/div/div/div/div/div[1]/div[1]/button").click()

    # Select Box 처리
    se = Select(driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/ng-view/div/div/div/div/div[2]/select"))
    #se.select_by_visible_text(bustime)

    # 바로 꺼짐 방지
    while True:
        pass

def main():
    global driver
    driver = set_chrome_driver()
    login()
    alert()
    bus()

### 특정 시간에 실행
schedule.every().day.at(startTime).do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
    print(datetime.datetime.now())


"""
### Select Box 처리
# (추가) 등하교 선택 넣기
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/a[5]").click()
# select Box XPATH
se = Select(driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/ng-view/div/div/div/div/div[1]/select"))
# 버스 시간 설정
se.select_by_visible_text(bustime)
"""

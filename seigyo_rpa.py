
# coding:utf-8
import time
import datetime
import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


# chromedriverのディレクトリ設定
DRIVER_PATH = '/Users/kanhyon/chromedriver'
number = input('学籍番号を入力してください:')
pas= input('パスワードを入力してください:')

#出席自動化の関数
def job():
        # ブラウザを開く
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        # CoursePowerの画面を開く
        driver.get("https://study.ns.kogakuin.ac.jp/lms/lginLgir/;SID=s174d65cb830698d6fa75a44d231#")
        # ログインIDを入力
        login_id = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div[1]/div[2]/input')
        login_id.send_keys("number")
        # パスワードを入力
        password = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div[2]/div[2]/input')
        password.send_keys("pas")
        # ログインボタンをクリックする
        login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/button')
        login_btn.click()
        # システム制御をクリックする
        seigyo_btn = driver.find_element_by_xpath('//*[@id="homeHomlForm"]/div[4]/div[12]/div[2]/div[1]/div[2]/div[1]/a')
        seigyo_btn.click()
        # 出席ボタンを押す
        syusseki_btn= driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[3]/div[2]/input')
        syusseki_btn.click()
        # iframe切替
        iframe = driver.find_element_by_id('dispCosa')
        driver.switch_to.frame(iframe) 
        time.sleep(3)
        # OKを押す
        ok_btn = driver.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/p/input[2]')
        ok_btn.click()
        # 3秒待機
        time.sleep(3)
        # ブラウザを終了する
        driver.close()

# 授業開始時間に関数を実行する設定
schedule.every().thursday.at("09:10").do(job)
schedule.every().thursday.at("13:40").do(job)
while True:
  schedule.run_pending()
  time.sleep(60)
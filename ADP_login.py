from typing import Literal
from selenium import webdriver
from datetime import date
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.webdriver import WebDriver
driver = webdriver.Chrome("chromedriver")


########### read credientials form ADP_login_detail.json #########
    # key ( "companyCode", "employeeCode", "password" )

file_data = open("ADP_login_detail.json")
login_json = json.load(file_data)
client_ID = login_json["companyCode"]
user_ID = login_json["employeeCode"]
password = login_json["password"]
file_data.close()


# ADP login url
driver.get("https://www.vista.adp.com/vista/index.html?TYPE=33554433&REALMOID=06-00056349-5d04-1f8a-bae3-1b780aca0000&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-2PZcgxfasaByM85o0PQjgCdeNLFKO0bt1Cvh2QNqwbwSryAKScVMsAtmoh9wl%2Fbh&TARGET=-SM-https:%2F%2Fwww.vista.adp.com%2FESS4%2FESSV5%2Fdashboard")

# client ID
driver.find_element_by_xpath("/html/body/app-root/div/app-login/div/div/div/div/form/adp-form-group[1]/adp-textbox/div/input").send_keys(client_ID)

# user ID
driver.find_element_by_xpath("/html/body/app-root/div/app-login/div/div/div/div/form/adp-form-group[2]/adp-textbox/div/input").send_keys(user_ID)

# password
driver.find_element_by_xpath("/html/body/app-root/div/app-login/div/div/div/div/form/adp-form-group[3]/adp-textbox/div/input").send_keys(password)

# submit
driver.find_element_by_xpath("/html/body/app-root/div/app-login/div/div/div/div/form/div[1]/button").click()
driver.implicitly_wait(0)

# leave
driver.find_element_by_xpath("//*[@id='mainNav']/div/div/div[1]/adp-sidebar/div/ul/adp-sidebar-item[6]/li/a").click()

# apply leave
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='adp-tile-20']/div[2]/app-my-leave/div[2]/div[2]/div/div[2]/adp-button"))).click()

# waiting for loading element disappear
WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, '//*[@id="mainNav"]/div/div/div[2]/div/div/app-leave-dashboard/app-apply-leave/adp-busy-indicator/div')))

# calender dropdown
driver.find_element_by_xpath("//*[@id='mainNav']/div/div/div[2]/div/div/app-leave-dashboard/app-apply-leave/adp-slidein/adp-overlay/div[2]/div/div/slidein-body/form/div/div[1]/adp-form-group/adp-date-picker/div/span").click()

# today date
today = date.today().strftime("%b %d, %Y") ####  20%d May%b 2021%Y ("%d %b %Y")

# date select
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table[1]/tbody/tr/td[@title='"+today+"']"))).click()

# leave type dropdown
driver.find_element_by_xpath("//*[@id='mainNav']/div/div/div[2]/div/div/app-leave-dashboard/app-apply-leave/adp-slidein/adp-overlay/div[2]/div/div/slidein-body/form/div/div[3]/adp-form-group/adp-dropdown-list/div").click()

# work from home
driver.find_element_by_xpath("//*[@id='mainNav']/div/div/div[2]/div/div/app-leave-dashboard/app-apply-leave/adp-slidein/adp-overlay/div[2]/div/div/slidein-body/form/div/div[3]/adp-form-group/adp-dropdown-list/div/div[2]/div/div/ul/li[13]").click()

# add leave details
driver.find_element_by_xpath("//*[@id='mainNav']/div/div/div[2]/div/div/app-leave-dashboard/app-apply-leave/adp-slidein/adp-overlay/div[2]/div/div/slidein-body/form/div/div[4]/adp-button").click()

# reason for leave
driver.find_element_by_xpath("//*[@id='mainNav']/div/div/div[2]/div/div/app-leave-dashboard/app-apply-leave/adp-slidein/adp-overlay/div[2]/div/div/slidein-body/form[2]/div/div[1]/div/div/adp-form-group/adp-textarea/textarea").send_keys("COVID-BCP")

# apply
driver.find_element_by_xpath("//*[@id='mainNav']/div/div/div[2]/div/div/app-leave-dashboard/app-apply-leave/adp-slidein/adp-overlay/div[2]/div/footer/slidein-footer/div/div/span[1]/adp-button").click()

time.sleep(10)  




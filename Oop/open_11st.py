from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()

driver.maximize_window()

driver.get('https://login.11st.co.kr/auth/front/login.tmall?xfrom=&returnURL=https%3A%2F%2Fwww.11st.co.kr%2Fhtml%2Fmain.html')
#driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Fwww.daum.net%2F')
sleep(1)

userid_ele = driver.find_element_by_id("loginName")
userid_ele.clear()
userid_ele.send_keys("gus1514")
sleep(1)

userpw_ele = driver.find_element_by_id("loginPw")
userpw_ele.clear()
userpw_ele.send_keys("damiao131312#")
sleep(3)

#loginbtn = driver.find_element_by_css_selector("form input[type='button']")
loginbtn = driver.find_element_by_css_selector("form button[type='submit']")

loginbtn.click()

sleep(5)


driver.get('')  #원하는 사이트로 이동


# html body 테그 내용 읽어오기
content = driver.find_element_by_tag_name("body")
html = content.text



driver.close()
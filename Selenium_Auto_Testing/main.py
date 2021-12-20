from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://coldsteels.ru/'

driver = webdriver.Chrome(executable_path='/Users/aleksandrtulakov/Documents/Selenium_Auto_Testing/chromedriver/chromedriver')


# ТК-1 проверка ввода на сайте ( ввод в input поиска товара )

try:
    driver.get( url = url ) 
    time.sleep(5)
    data_input  = driver.find_element_by_tag_name('input')
    data = 'Ti Light 6'
    data_input.send_keys(data + Keys.ENTER)
    driver.save_screenshot("tk1.png")
    time.sleep(5)
    print( 'Sucsess! ТК-01' )
except Exception as Ex:
    print(Ex)


# ТК-2 проверка работоспособности сортировки товаров ( например по ножам )
try:
    choose  = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div[2]/select')
    
    choose.click()
    choose_2  = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/div/div[2]/select/option[3]')
    choose_2.click()
    driver.save_screenshot("tk2.png")
    print( 'Sucsess! ТК-02' )
    time.sleep(5)
except Exception as Ex:
    print(Ex)


# ТК-3 проверка работоспособности выбора товара для ознакомления 

try:
    choose  = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[10]/div/div[1]/a/img')
    choose.click()
    driver.save_screenshot("tk3.png")
    print( 'Sucsess! ТК-03' )
    time.sleep(5)
except Exception as Ex:
    print(Ex)

# ТК-4 Проверка функционирования добавления выбраного товара в корзину

try:
    choose  = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div[1]/div/div[2]/button')
    choose.click()
    driver.save_screenshot("tk4.png")
    print( 'Sucsess! ТК-04' )
    time.sleep(5)
except Exception as Ex:
    print(Ex)


# ТК-5 Проверка перехода к оформлению заказа

try:
    choose  = driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div[2]/a[1]')
    choose.click()
    driver.save_screenshot("tk5.png")
    print( 'Sucsess! ТК-05' )
    time.sleep(5)
except Exception as Ex:
    print(Ex)

# ТК-6 Проверка функционала осуществления покупки ( ввод информации, затем нажатие на кнопку покупки и перекидывание на ожидания подтверждения заказа )

try:
    number = '8800553535'
    email = 'abobys@gmail.com'
    name =  'Aboba Abobysov'
    driver.save_screenshot("tk6_1.png")
    choose_1  = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/fieldset/div[1]/div/input')
    choose_1.send_keys(number)

    choose_2  = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/fieldset/div[2]/div/input')
    choose_2.send_keys( email )

    choose_3  = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/fieldset/div[3]/div/input')
    choose_3.send_keys( name )

    choose  = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/div/div[4]/div[1]/a')
    choose.click()
    driver.save_screenshot("tk6_2.png")
    print( 'Sucsess! ТК-06' )
    time.sleep(5)
except Exception as Ex:
    print(Ex)





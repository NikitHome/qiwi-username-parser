from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from settings.config import phone_number, password


# подключение веб-драйвера
exe_path = r'./driver/'
driver = webdriver.Chrome()
driver.get('https://qiwi.com/payment/form/870')
sleep(5)


# вход в учетную запись
def login():
    driver.maximize_window()
    driver.refresh()
    
    # тыкаем на кнопку войти
    WebDriverWait(driver, 4)
    driver.find_element(By.CLASS_NAME, 'button-content-45').click()
    
    # тыкаем на поле ввода номера
    WebDriverWait(driver, 4)
    driver.find_element(By.XPATH, "//input[@type='tel' and @value='+7']").click()
    
    # вводим номер
    WebDriverWait(driver, 4)
    driver.find_element(By.XPATH, "//input[@type='tel' and @value='+7']").send_keys(phone_number)
    
    # тыкаем на поле ввода пароля
    WebDriverWait(driver, 4)
    driver.find_element(By.XPATH, "//input[@type='password' and @value='']").click()
    
    # вводим пароль
    WebDriverWait(driver, 4)
    driver.find_element(By.XPATH, "//input[@type='password' and @value='']").send_keys(password)
    
    # кликаем войти
    WebDriverWait(driver, 4)
    driver.find_element(By.CLASS_NAME, 'button-content-text-47').click()
    

def get_name(only_num_mess):
    login()
    
    # кликаем на галочку 
    WebDriverWait(driver, 4)
    driver.find_element(By.CLASS_NAME, 'radio-form-field-control-option-check-345').click()
    
    # кликаем на поле ввода телефона
    WebDriverWait(driver, 4)
    driver.find_element(By.XPATH, "//input[@type='tel' and @value]").click()
    
    # вводим телефон
    WebDriverWait(driver, 4)
    driver.find_element(By.XPATH, "//input[@type='tel' and @value]").send_keys(only_num_mess)
    
    # сохраняем текст
    parent_element = driver.find_element(By.XPATH, "//div[@class='info-control-value-610']")
    name = driver.execute_script('return arguments[0].childNodes[1].textContent;', parent_element).strip()
    
    # закрываем браузер
    driver.close()
    
    return f'Имя: {name}'
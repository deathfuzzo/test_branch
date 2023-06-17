# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
try:
    browser.get(sbis_site)
    time.sleep(1)
    contacts_btn = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item.sbisru-Header__menu-item-1')
    contacts_btn.click() # нажатие на Контакты
    time.sleep(1)
    tensor_banner = browser.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor:not(.sbisru-link)')
    tensor_banner.click()  # нажатие на баннер Тензора
    time.sleep(1)
    handles = browser.window_handles  # получаем список всех вкладок
    browser.switch_to.window(handles[1])  # переключение на вторую вкладку
    # далее необязательный блок с скроллом до блока "Сила в людях" #
    body = browser.find_element(by=By.TAG_NAME, value='body')
    body.click()
    for i in range(30):
        body.send_keys(Keys.DOWN)
    time.sleep(1)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    power_banner = browser.find_element(By.CSS_SELECTOR, '.s-Grid-col.s-Grid-col--6.s-Grid-col--sm12:not(.s-Grid--show-sm)')
    assert power_banner.is_displayed()  # проверка отображения блока "Сила в людях"
    about_power = browser.find_element(By.XPATH, '// *[ @ id = "container"] / div[1] / div / div[5] / div / div / div[1] / div / p[4] / a')
    about_power.click()  # нажатие на кнопку подробнее в блоке "Сила в людях"
    about_tensor_site = 'https://tensor.ru/about'
    assert browser.current_url == about_tensor_site, 'Неверно открыт сайт'  # проверка адреса открытой страницы

finally:
    browser.quit()




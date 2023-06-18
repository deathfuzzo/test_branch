# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
fix_site = 'https://fix-online.sbis.ru/'
login = "orlov.ei"
password = "orlov.ei123"
user = "Орлов Фикс"
message = "О дивный новый мир!"


def test1():
    try:
        browser.get(fix_site)
        time.sleep(1)
        login_field = browser.find_element(By.CSS_SELECTOR, "[name='Login']")
        login_field.send_keys(login, Keys.ENTER)
        assert login_field.get_attribute('value') == login
        time.sleep(1)
        password_field = browser.find_element(By.CSS_SELECTOR, "[name='Password']")
        password_field.send_keys(password, Keys.ENTER)
        assert password_field.get_attribute('value') == password
        time.sleep(5)
        contacts_accord = browser.find_element(By.CSS_SELECTOR, "[data-qa='NavigationPanels-Accordion__title']")
        contacts_accord.click()
        time.sleep(3)
        contacts_menu = browser.find_element(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__headTitle")
        contacts_menu.click()
        time.sleep(2)
        add_btn = browser.find_element(By.CSS_SELECTOR, "[data-qa='sabyPage-addButton']")
        add_btn.click()
        time.sleep(3)
        search_field = browser.find_element(By.XPATH, "//*[@id='popup']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/input")
        search_field.send_keys(user)
        time.sleep(2)
        person_record = browser.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
        assert person_record.get_attribute('title') == user
        person_record.click()
        time.sleep(1)
        text_editor = browser.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
        text_editor.send_keys(message)
        time.sleep(1)
        text_editor.send_keys(Keys.LEFT_CONTROL + Keys.ENTER)
        time.sleep(1)
        messages_before = browser.find_elements(By.CSS_SELECTOR, ".msg-entity-text.msg-entity_font_croppless.richEditor_richContentRender_fontSize-m_theme-default")
        assert messages_before[0].text == message  # проверка наличия записи в реестре с текстом последнего отправленного сообщения
        actionChains = ActionChains(browser)
        actionChains.context_click(messages_before[0]).perform()  # открытие меню доп.опций по правому клику
        time.sleep(1)
        remove_btn = browser.find_element(By.CSS_SELECTOR, ".controls-icon_size-m.controls-icon_style-danger.icon-Erase.controls-icon.controls-Menu__icon")
        remove_btn.click()
        time.sleep(1)
        messages_after = browser.find_elements(By.CSS_SELECTOR, ".msg-entity-text.msg-entity_font_croppless.richEditor_richContentRender_fontSize-m_theme-default")
        assert messages_after[0].text != message  # проверка отсутствия записи в реестре с текстом последнего сообщения
    finally:
        browser.quit()

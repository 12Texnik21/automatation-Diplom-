
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait

def test_search_dostoevsky():
    chitai = webdriver.Firefox()
    wait = WebDriverWait(chitai, 40, 0.1)
    chitai.maximize_window()
    chitai.get("https://www.chitai-gorod.ru")
    chitai.implicitly_wait(2)
    button_name = chitai.find_element(By.CLASS_NAME,"header-search__input").send_keys("Достоевский")
    button_name = chitai.find_element(By.CLASS_NAME,"header-search__button-icon").click()
    chitai.implicitly_wait(2)
    chitai.quit()


def test_search_war_and_peace():
    chitai2 = webdriver.Firefox()
    wait = WebDriverWait(chitai2, 40, 0.1)
    chitai2.maximize_window()
    chitai2.get("https://www.chitai-gorod.ru")
    chitai2.implicitly_wait(2)
    button_name = chitai2.find_element(By.CLASS_NAME,"header-search__input").send_keys("Война и мир")
    chitai2.implicitly_wait(2)
    button_name = chitai2.find_element(By.CLASS_NAME,"header-search__button-icon").click()
    chitai2.implicitly_wait(2)
    chitai2.quit()


def test_read_school():
    chitai3 = webdriver.Firefox()
    wait = WebDriverWait(chitai3, 40, 0.1)
    chitai3.maximize_window()
    chitai3.get("https://www.chitai-gorod.ru")
    button_name = chitai3.find_element(By.CSS_SELECTOR, "div.change-city__button:nth-child(1)").click()
    button_name = chitai3.find_element(By.CSS_SELECTOR, "#__layout > div > nav > ul > a:nth-child(3)").click()
    chitai3.implicitly_wait(2)
    chitai3.quit()


def test_placing_a_new_order():
    chitai4 = webdriver.Firefox()
    chitai4.maximize_window()
    wait = WebDriverWait(chitai4, 40, 0.1)
    chitai4.get("https://www.chitai-gorod.ru")
    button_name = chitai4.find_element(By.CSS_SELECTOR, "div.change-city__button:nth-child(1)").click()
    button_name = chitai4.find_element(By.CLASS_NAME,"header-search__input").send_keys("игроки гоголь")
    button_name = chitai4.find_element(By.CSS_SELECTOR, "#__layout > div > header > div > div.sticky-header__catalog > div.header-search.header-search--opened > div.header-search__head > form > button > svg").click()
    chitai4.implicitly_wait(2)
    button_name = chitai4.find_element(By.CSS_SELECTOR, "#__layout > div > div.app-wrapper__content > div.search-page.js-catalog-container > div > div > div > section > section > div > article:nth-child(1) > div.product-card__text.product-card__row > a > div > div.product-title__head").click()
    chitai4.implicitly_wait(2)
    button_name = chitai4.find_element(By.CSS_SELECTOR, "#__layout > div > div.app-wrapper__content > main > div > div.detail-product__aside > div.product-offer.detail-product__offer > div > div.product-offer-header.product-offer__offer-header > div.product-offer-header__buttons > button.product-offer-button.chg-app-button.chg-app-button--primary.chg-app-button--extra-large.chg-app-button--brand-blue.chg-app-button--block").click()
    chitai4.implicitly_wait(2)
    button_name = chitai4.find_element(By.CSS_SELECTOR, "#__layout > div > div.app-wrapper__content > main > div > div.detail-product__aside > div.product-offer.detail-product__offer > div > div.product-offer-header.product-offer__offer-header > div.product-offer-header__buttons > button.product-offer-button.chg-app-button.chg-app-button--primary.chg-app-button--extra-large.chg-app-button--green.chg-app-button--block").click()
    chitai4.implicitly_wait(2)
    chitai4.quit()


def test_removing_a_book_from_the_trash():
    chitai5 = webdriver.Firefox()
    chitai5.maximize_window()
    wait = WebDriverWait(chitai5, 40, 0.1)
    chitai5.get("https://www.chitai-gorod.ru")
    button_name = chitai5.find_element(By.CSS_SELECTOR, "div.change-city__button:nth-child(1)").click()
    button_name = chitai5.find_element(By.CLASS_NAME,"header-search__input").send_keys("игроки гоголь")
    button_name = chitai5.find_element(By.CSS_SELECTOR, "#__layout > div > header > div > div.sticky-header__catalog > div.header-search.header-search--opened > div.header-search__head > form > button > svg").click()
    chitai5.implicitly_wait(2)
    button_name = chitai5.find_element(By.CSS_SELECTOR, "#__layout > div > div.app-wrapper__content > div.search-page.js-catalog-container > div > div > div > section > section > div > article:nth-child(1) > div.product-card__text.product-card__row > a > div > div.product-title__head").click()
    chitai5.implicitly_wait(2)
    button_name = chitai5.find_element(By.CSS_SELECTOR, "#__layout > div > div.app-wrapper__content > main > div > div.detail-product__aside > div.product-offer.detail-product__offer > div > div.product-offer-header.product-offer__offer-header > div.product-offer-header__buttons > button.product-offer-button.chg-app-button.chg-app-button--primary.chg-app-button--extra-large.chg-app-button--brand-blue.chg-app-button--block").click()
    chitai5.implicitly_wait(2)
    button_name = chitai5.find_element(By.CSS_SELECTOR, "#__layout > div > header > div > a > svg").click()
    chitai5.implicitly_wait(2)
    button_name = chitai5.find_element(By.CSS_SELECTOR, "#__layout > div > header > div > div.sticky-header__controls > a > svg.header-cart__icon.header-cart__icon--desktop").click()
    chitai5.implicitly_wait(2)
    button_name = chitai5.find_element(By.CSS_SELECTOR, "#__layout > div > div.app-wrapper__content > div.cart-page > div.head > div.delete-many").click()
    chitai5.quit()
    
test_search_dostoevsky()
test_search_war_and_peace()
test_read_school()
test_placing_a_new_order()
test_removing_a_book_from_the_trash()
from selene import browser, have
import allure
from appium.webdriver.common.appiumby import AppiumBy


@allure.tag("Mobile")
@allure.feature("Поиск")
@allure.story("Поиск текста 'Appium'")
def test_search():
    with allure.step("Ввод текста в поле поиска"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with allure.step('Проверка результата'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.tag("Mobile")
@allure.feature("Поиск")
@allure.story("Проверка результата поиска")
def test_open_first_article_in_result():
    with allure.step('Ввод текста в поле поиска "Python"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Python')

    with allure.step('Проверка результата поиска'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Python'))

    with allure.step('Клик по статье'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()

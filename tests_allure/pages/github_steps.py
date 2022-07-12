import allure
from selene import be, by
from selene.support.shared import browser


@allure.step('Открываем главную страницу {url}')
def open_page(url):
    browser.open(url)

@allure.step('Производим поиск {what_search}')
def search_text(what_search):
    browser.element('[name="q"]').click().type(what_search).submit()

@allure.step('Переходим в необходимый репозиторий {which_repository}')
def go_to_repository(which_repository):
    browser.element(by.link_text(which_repository)).click()

@allure.step('Нажимаем на Issues')
def search_issues():
    browser.element('#issues-tab').click()

@allure.step('Проверяем наличие Issues {number}')
def search_issues_number(number):
    browser.element(by.partial_text(number)).should(be.visible)
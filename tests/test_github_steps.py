import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from configuration import browser_config#browser_parametrs
from configuration.pages import github_steps
from allure_commons.types import AttachmentType


link = 'https://github.com/'

def test_git_with_steps():
    allure.dynamic.tag('GitHub')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.story('Проверка Issues через тест в 1 файле')
    allure.dynamic.link(link)
    allure.dynamic.label('owner','Sam')
    allure.dynamic.description('Описание для понимания')
    allure.dynamic.feature('Задачи Issues в репозитории')
    allure.dynamic.title('Проверка Issues через тест в 1 файле TITLE')
    browser_config.browser_parametrs()

    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Производим поиск'):
        browser.element('[name="q"]').click().type('SamEn-d/tests_allure').submit()

    with allure.step('Переходим в необходимый репозиторий'):
        browser.element(by.link_text('SamEn-d/tests_allure')).click()

    with allure.step('Нажимаем на Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issues №1'):
        browser.element(by.partial_text('#1')).should(be.visible)
    allure.attach(browser.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)



@allure.tag('GitHub')
@allure.severity(Severity.MINOR)
@allure.label('owner','Sam')
@allure.feature('Задачи Issues в репозитории')
@allure.story('Проверка Issues через PageObject')
@allure.title('Проверка Issues через PageObject Title')
@allure.link(link)
def test_git_allure_steps():
    browser_parametrs()
    github_steps.open_page(link)
    github_steps.search_text('SamEn-d/configuration')
    github_steps.go_to_repository('SamEn-d/configuration')
    github_steps.search_issues()
    github_steps.search_issues_number('#1')
    allure.attach(browser.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


from selene import by, be
from selene.support.shared import browser
from tests_allure.browser import browser_parametrs


def test_git():
    browser_parametrs()
    browser.open('https://github.com/')

    browser.element('[name="q"]').click().type('SamEn-d/tests_allure').submit()

    browser.element(by.link_text('SamEn-d/tests_allure')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#1')).should(be.visible)


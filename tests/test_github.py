from selene import by, be
from selene.support.shared import browser
from configuration.browser_config import browser_parametrs


def test_git():
    browser_parametrs()
    browser.open('https://github.com/')

    browser.element('[name="q"]').click().type('SamEn-d/configuration').submit()

    browser.element(by.link_text('SamEn-d/configuration')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#1')).should(be.visible)


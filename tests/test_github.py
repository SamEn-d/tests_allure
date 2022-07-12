from selene.support.shared import browser

def test_git():
    browser.open('https://github.com/')
    browser.element('[name="q"]').click
    browser.element('[name="q"]').click().type('SamEn-d')

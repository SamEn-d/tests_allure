import allure
from allure_commons.types import Severity

@allure.tag('GitHub')
@allure.severity(Severity.MINOR)
@allure.label('owner','Sam')
@allure.feature('Issues')
@allure.story('Issues PageObject')
@allure.title('Issues PageObject Title')
def test_git_allure_steps():
    pass
#s


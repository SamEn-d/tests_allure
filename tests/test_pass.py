import allure
from allure_commons.types import Severity

@allure.tag('GitHub')
@allure.severity(Severity.MINOR)
@allure.label('owner','Sam')
@allure.feature('Задачи Issues в репозитории')
@allure.story('Проверка Issues через PageObject')
@allure.title('Проверка Issues через PageObject Title')
def test_git_allure_steps():
    pass


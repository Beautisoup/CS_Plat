import allure
@allure.feature("nub1")
@allure.story("nub1")
def test():
    with allure.step("step1"):
        assert 1==1

@allure.feature("nub2")
@allure.story("nub2")
def test2():
    with allure.step("step2"):
        assert 1==1
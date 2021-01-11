from selenium import webdriver


def test_openbrowser():
    browser = webdriver.Chrome()
    browser.get('https://www.runoob.com/python/python-reg-expressions.html')
    print(browser.execute_script("return JSON.stringify(window.performance.timing)"))

test_openbrowser()
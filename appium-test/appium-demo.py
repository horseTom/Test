from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "Nexus"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/open")
el1.click()
el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el2.click()
el3 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el3.click()
driver.implicitly_wait(5)
el6 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el6.click()
driver.implicitly_wait(3)
el7 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el7.send_keys("alibaba")

driver.quit()
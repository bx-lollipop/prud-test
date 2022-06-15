import pytest,allure
import time
from selenium.webdriver.common.by import By
import re

@allure.feature("Task:Baidu Search")
class TestBaidu(object):
    @allure.story("case1:set result page_size=20")
    def test_01(self, wd):
        wd.find_element(by=By.ID, value="s-usersetting-top").click()
        setting_menu = wd.find_element(by=By.CLASS_NAME, value="s-user-setting-pfmenu")
        setting_menu.find_element(by=By.LINK_TEXT, value="搜索设置").click()
        time.sleep(2)
        wd.find_element(by=By.XPATH, value='//*[@id="nr_2"]').click()
        wd.find_element(by=By.ID, value="se-setting-7").find_element(by=By.LINK_TEXT, value="保存设置").click()
        time.sleep(2)
        wd.switch_to.alert.accept()
        time.sleep(2)

        # search "沉思录"
        wd.find_element(by=By.ID, value="kw").send_keys("沉思录")
        wd.find_element(by=By.ID, value="su").click()
        time.sleep(2)

        # check result count
        #result = self.wd.find_elements(by=By.XPATH, value='//h3[contains(@class,"c-title")]')
        #result = self.wd.find_elements(by=By.XPATH, value='//div[contains(@class,"c-container") and contains(@class,"xpath-log")]')
        result = wd.find_elements(by=By.XPATH,
                                       value='//div[contains(@class,"c-container") and not(contains(@class,"EC_result"))] //h3[contains(@class,"t")]')
        assert len(result) == 20
        time.sleep(2)

    @allure.story("case2:check ads")
    def test_02(self, wd):
        ads = wd.find_elements(by=By.CLASS_NAME, value="ec-tuiguang")
        assert len(ads) > 0
        print("There are %d advertisements." % len(ads))

    @allure.story("case3:search result within 1 day")
    def test_03(self, wd):
        wd.find_element(by=By.CLASS_NAME, value="tool_3HMbZ").click()
        time.sleep(2)
        wd.find_element(by=By.ID, value="timeRlt").click()
        time.sleep(2)
        wd.find_element(by=By.XPATH, value='//ul[@class="file_ul_2a1K5"]/li[2]').click()
        time.sleep(5)

        time_res = wd.find_elements(by=By.XPATH, value='//span[@class="c-color-gray2"]')
        for item in time_res:
            text = item.text
            hour = re.findall(r"\d+", text)
            if len(hour) > 0:
                assert int(hour[0]) < 25



from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    def test_first_temp(self):
        self.browser.get('https://weather.com/he-IL/weather/today/l/4365aa930f6209025385cfac862996d9a8f6167024e51f67b3e28b957b8f5462')
        # to maximize the browser window
        self.browser.maximize_window()
        # read temp from first website:
        result = self.browser.find_element(by=By.CLASS_NAME, value='CurrentConditions--tempValue--3a50n')
        self.temp_browser1 = int(result.text.split('°')[0])
        time.sleep(3)
        self.browser.close()
        time.sleep(3)
        # open second browser:
        self.browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.browser.get(
            'https://forecast.weather.gov/MapClick.php?lat=39.05589000000003&lon=-77.11347499999994#.YovwJ3ZBw2w')
        self.browser.maximize_window()
        result = self.browser.find_element(by=By.CLASS_NAME, value='myforecast-current-sm')
        self.temp_browser2 = int(result.text.split('°')[0])
        time.sleep(3)
        self.browser.close()
        time.sleep(3)
        # compare two results, raise exception if biger temp larger than the smallest on more than 10%
        min_temp = min(self.temp_browser1, self.temp_browser2)
        max_temp = max(self.temp_browser1, self.temp_browser2)
        if max_temp > (min_temp + (10 / 100 * min_temp)):
            raise ValueError("TEMP GAB BETWEEN {} AND {} IS LARGER THAN 10%".format(min_temp, max_temp))
        else:
            print("TEMP GAB BETWEEN {} AND {} IS LESS OR EQUAL TO 10%".format(min_temp, max_temp))


if __name__ == '__main__':
    unittest.main()





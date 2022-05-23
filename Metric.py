from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import random
import time


class MatrixTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    def test_temp_convertion(self):
        # randomize temp
        temp = random.randint(0, 1000)
        temp = str(temp)
        self.browser.get('https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm?val={}'.format(temp))
        # to maximize the browser window
        self.browser.maximize_window()
        # compare expected and received values:
        result = self.browser.find_element(by=By.ID, value='result')
        text = result.text
        received = float(text.split('\n')[0].split('=')[-1].split('°')[0])
        # use formula to convert C tp F
        expected = float(temp) * 9 / 5 + 32
        if received != expected:
            raise ValueError("TEMP CONVERTION INCORRECT, EXPECTED:{} BUT RECEIVED:{}".format(expected, received))
        else:
            print("TEMP CONVERTION IS CORRECT, EXPECTED:{} EQUAL TO RECEIVED:{}".format(expected, received))
        time.sleep(3)

        self.browser.close()

    def test_length_convertion(self):
        length = random.randint(0, 1000)
        length = str(length)
        self.browser.get('https://www.metric-conversions.org/length/meters-to-feet.htm?val={}'.format(length))
        self.browser.maximize_window()
        # compare expected and received values:
        result = self.browser.find_element(by=By.ID, value='result')
        text = result.text
        received = str(float(text.split('\n')[0].split('=')[-1].split(' ')[1][:-2])).split('.')[0]
        expected = str(float(length) * 3.28).split('.')[0]
        if int(received) != int(expected):
            raise ValueError("LENGTH CONVERTION INCORRECT, EXPECTED:{} BUT RECEIVED:{}".format(expected, received))
        else:
            print("LENGTH CONVERTION IS CORRECT, EXPECTED:{} EQUAL TO RECEIVED:{}".format(expected, received))

        def test_length_convertion(self):
            length = random.randint(0, 1000)
            length = str(length)
            self.browser.get('https://www.metric-conversions.org/length/meters-to-feet.htm?val={}'.format(length))
            self.browser.maximize_window()
            # compare expected and received values:
            result = self.browser.find_element(by=By.ID, value='result')
            text = result.text
            received = int(text.split('\n')[0].split('=')[-1].split(' ')[1][:-2])
            expected = int(float(length) * 3.28)
            if abs(received-expected) > 1:
                raise ValueError("LENGTH CONVERTION INCORRECT, EXPECTED:{} BUT RECEIVED:{}".format(expected, received))
            else:
                print("LENGTH CONVERTION IS CORRECT, EXPECTED:{} EQUAL TO RECEIVED:{}".format(expected, received))

        time.sleep(3)

        self.browser.close()

    def test_weight_convertion(self):
        weight = random.randint(0, 1000)
        weight = str(weight)
        self.browser.get('https://www.metric-conversions.org/weight/ounces-to-grams.htm?val={}'.format(weight))
        self.browser.maximize_window()
        # compare expected and received values:
        result = self.browser.find_element(by=By.ID, value='result')
        text = result.text
        received = str(float(text.split('\n')[0].split('=')[-1].split(' ')[1][:-2])).split('.')[0]
        expected = str(float(weight) * 28.34952).split('.')[0]
        if int(received) != int(expected):
            raise ValueError("WEIGHT CONVERTION INCORRECT, EXPECTED:{} BUT RECEIVED:{}".format(expected, received))
        else:
            print("WEIGHT CONVERTION IS CORRECT, EXPECTED:{} EQUAL TO RECEIVED:{}".format(expected, received))
        time.sleep(3)

        self.browser.close()


if __name__ == '__main__':
    unittest.main()



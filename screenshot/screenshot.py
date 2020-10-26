import unittest
from pyunitreport import HTMLTestRunner
from Screenshot import Screenshot_Clipping
from selenium import webdriver


class Screen(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def test_HelloWorld(self):
        driver = self.driver
        ob = Screenshot_Clipping.Screenshot()
        url = "https://www.larepublica.co/robots.txt."
        self.driver.get(url)
        img_url = ob.full_Screenshot(
            driver, save_path=r'.', image_name='ScreenShot.png')
        print(img_url)
        driver.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output="reportes", report_name='hello_world_report'))

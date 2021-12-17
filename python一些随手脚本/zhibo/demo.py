    from selenium import webdriver
import time

if __name__ == "__main__":

    browser = webdriver.Chrome('./chromedriver.exe')
    browser.get('https://live.douyin.com/1111111')
    time.sleep(10)
    a = 1
    while a < 999999999999:
        a += 1
        item = browser.find_element_by_xpath(
            '//*[@id="root"]/div/main/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span').text
        print(item)
        time.sleep(3)

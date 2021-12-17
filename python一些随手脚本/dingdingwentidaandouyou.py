import time
from selenium import webdriver


def saveText(issue):
    try:
        f = open('./答案.txt', 'a')  # 首先先创建一个文件对象
        f.writelines("问题:" + str(issue).replace(' ', ' ').replace('‟', '"')
                     )  # 写入数据
        f.writelines('\n')  # 增加换行符
    except BaseException:
        print("保存文本出问题了~", BaseException)


def getData(issue1, next_button1, browser):
    # 问题地址
    issue = browser.find_element_by_xpath(issue1).text
    # 下一题按钮
    next_button = browser.find_element_by_xpath(next_button1)
    next_button.click()
    print("问题:", issue)  # 打印控制台
    saveText(issue)  # 写入桌面文件


def getHtml(url, loadmore=False, waittime=5):
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    time.sleep(waittime)
    num = 0
    if loadmore:
        while num < 100:
            num += 1
            try:
                issue = '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]'
                next_button = '//*[@id="root"]/div/main/div/div/div[2]/div/div[1]/button[2]'
                getData(issue, next_button, browser)
            except BaseException:
                print("匹配标签出问题了", BaseException)
                break


url = input("输入要提取的地址:\n")
getHtml(url, True, 2)

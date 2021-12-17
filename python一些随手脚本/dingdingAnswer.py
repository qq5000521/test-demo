import time
from selenium import webdriver


def fileW(issue, answer):
    f = open('D:\desktop\物联网.txt', 'a')  # 首先先创建一个文件对象
    f.writelines("问题:" + str(issue) + "----" + str(answer))  # 写入数据
    f.writelines('\n')  # 增加换行符


def getHtml(url, loadmore=False, waittime=5):
    browser = webdriver.Chrome('D:\desktop\python3\chromedriver.exe')
    browser.get(url)
    time.sleep(waittime)
    num = 0
    if loadmore:
        while num <= 99:  # 执行99次下一题操作
            num += 1
            try:
                # 问题地址
                issue = browser.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]/div[2]/span[2]').text
                # 答案地址
                answer = browser.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]/div[4]/div[3]/div[2]/div[1]').text
                # 下一题按钮
                next_button = browser.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div[2]/div/div[1]/button[2]')
                next_button.click()
                print("问题:", issue, "答案:", answer)  # 打印控制台
                fileW(issue, answer)  # 写入桌面文件
            except:
                break


getHtml('https://alicert.taobao.com/exam/test?sid=_79429818015300&tenantName=ecpc_tenant_dingding&sst=CuHODFC2O1gVMMC05THcEWgmnv5LDww3zVITRdpLyuH72au5W%2FajsugkrIjRiFxn', True, 2)

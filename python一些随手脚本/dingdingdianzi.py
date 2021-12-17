import time
from selenium import webdriver


def fileW(issue, answer):
    f = open('D:\desktop\电子竞技.txt', 'a')  # 首先先创建一个文件对象
    f.writelines("问题:" + str(issue) + "----" + str(answer))  # 写入数据
    f.writelines('\n')  # 增加换行符


def getHtml(url, loadmore=False, waittime=5):
    browser = webdriver.Chrome('D:\desktop\python3\chromedriver.exe')
    browser.get(url)
    time.sleep(waittime)
    num = 0
    if loadmore:
        while num <= 9:
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
        while num <= 30:
            num += 1
            try:
                # 问题地址
                issue = browser.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]/div[2]/span[2]').text
                # 答案地址
                answer = browser.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]/div[4]/div[5]/div[2]/div[1]').text
                # 下一题按钮
                next_button = browser.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div[2]/div/div[1]/button[2]')
                next_button.click()
                print("问题:", issue, "答案:", answer)  # 打印控制台
                fileW(issue, answer)  # 写入桌面文件
            except:
                break
        while num <= 49:
            num += 1
            try:
                # 问题地址
                issue = browser.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]/div[2]/span[2]').text
                # 答案地址
                answer = browser.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]/div[4]/div[5]/div[2]/div[1]').text
                # 下一题按钮
                next_button = browser.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div/div/div[2]/div/div[1]/button[2]')
                next_button.click()
                print("问题:", issue, "答案:", answer)  # 打印控制台
                fileW(issue, answer)  # 写入桌面文件
            except:
                break


getHtml('https://alicert.taobao.com/exam/test?sid=_79428328011374&tenantName=ecpc_tenant_dingding&sst=rvit34%2F%2F%2BwY095EctuzYoYLFKpHBU04MLworfyT1UGnlB21%2FDbi86DuYR8e749Fa', True, 2)

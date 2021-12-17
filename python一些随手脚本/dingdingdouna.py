import time
from selenium import webdriver


def saveText(issue, answer):
    try:
        f = open('D:\desktop\农业经理人.txt', 'a')  # 首先先创建一个文件对象
        f.writelines("问题:" + str(issue).replace(' ', ' ').replace('‟', '"') +
                     "----" + str(answer))  # 写入数据
        f.writelines('\n')  # 增加换行符
    except BaseException:
        print("保存文本出问题了~", BaseException)


def getData(issue1, answer1, next_button1, browser):
    # 问题地址
    issue = browser.find_element_by_xpath(issue1).text
    # 答案地址
    answer = browser.find_element_by_xpath(answer1).text
    # 下一题按钮
    next_button = browser.find_element_by_xpath(next_button1)
    next_button.click()
    print("问题:", issue, "答案:", answer)  # 打印控制台
    saveText(issue, answer)  # 写入桌面文件


def getHtml(url, loadmore=False, waittime=5):
    browser = webdriver.Chrome('D:\desktop\python3\chromedriver.exe')
    browser.get(url)
    time.sleep(waittime)
    num = 0
    if loadmore:
        while num < 100:
            num += 1
            try:
                issue = '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]'
                next_button = '//*[@id="root"]/div/main/div/div/div[2]/div/div[1]/button[2]'
                if num <= 30:  # 判断题目数量
                    answer = '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]/div[4]/div[3]/div[2]/div[1]'
                else:  # 其余题目
                    answer = '//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[4]/div[4]/div[5]/div[2]/div[1]'
                getData(issue, answer, next_button, browser)
            except:
                print("匹配标签出问题了")
                break


getHtml('https://alicert.taobao.com/exam/test?sid=_79669989015153&tenantName=ecpc_tenant_dingding&sst=1HyPyNjYrVSyviO14d3qkMTn%2FmU3yU0s46uY8q4PBmtXeUkz9LAMaRthLU0WQ%2Bif', True, 2)

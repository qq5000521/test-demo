def fileW(zhi, daan):
    print("写入我执行开始了")
    f = open('保存题目.txt', 'w')  # 首先先创建一个文件对象，打开方式为w
    f.writelines("问题:" + str(zhi) + "答案" + str(daan))
    f.writelines('\n')
    print("写入文件执行完毕")


fileW(1, 2)

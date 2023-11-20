#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 老李企业签名包配置文件脚本

import datetime
import random
import os

qianzhui = "wz"  # 文件名前缀
shijian = datetime.datetime.now().strftime(
    '%Y%m%d')+str(random.randint(10, 99))
wenjianming = qianzhui+shijian

shuru = str(input("输入bundleID: "))
gamename = str(input("游戏名称: "))

print("文件名前缀: ", qianzhui, "文件名: ", wenjianming,
      "输入bundleID: ", shuru, "游戏名称: ", gamename)

f = open('setting.plist', 'r', encoding="utf8")
fa = open(wenjianming+".plist", 'w+', encoding="utf8")

# 默认名字和bundleid
if shuru == '' and gamename == '':
    a = f.read().replace("huandiao", wenjianming)
    fa.writelines(a)
# 查看是否更换bundleid
elif shuru != '' and gamename == '':
    a = f.read().replace("huandiao", wenjianming).replace("com.udcs.jplay", shuru)
    fa.writelines(a)
# 查看是否更换游戏名字
elif gamename != '' and shuru == '':
    a = f.read().replace("huandiao", wenjianming).replace("王者传奇", gamename)
    fa.writelines(a)
# 查看是否更换游戏名字和bundleid
elif gamename != ''and shuru != '':
    a = f.read().replace("huandiao", wenjianming).replace(
        "王者传奇", gamename).replace("com.udcs.jplay", shuru)
    fa.writelines(a)

fa.close()


def rename_func(name):
    os.rename(findAllFilesWithSpecifiedSuffix("./", "ipa"), "./"+name+".ipa")


# 查找指定扩展名文件
def findAllFilesWithSpecifiedSuffix(target_dir, target_suffix="ipa"):
    find_res = []
    target_suffix_dot = "." + target_suffix
    walk_generator = os.walk(target_dir)
    for root_path, dirs, files in walk_generator:
        if len(files) < 1:
            continue
        for file in files:
            file_name, suffix_name = os.path.splitext(file)
            if suffix_name == target_suffix_dot:
                find_res.append(os.path.join(root_path, file))
    return find_res[0]


rename_func(wenjianming)

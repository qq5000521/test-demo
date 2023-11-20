##推荐用这个版本20231120日更新
go版本go run .\godemo.go
也可以双击godemo.exe使用.
功能:go版本会自动读取CFBundleIdentifier,和CFBundleDisplayName的值,不用手动输入,自动替换ipa文件名,自动修改模板并且创建plist文件.
注意:setting.plist模板文件不要删除,可以改掉里面的url地址.替换字符huandiao这个不要改会自动替换新生成的文件名
用法:go全自动获取处理.exe和setting.plist的同级目录放签好名ipa包,然后双击执行.完成后上传两个文件到对应的url地址内即可.
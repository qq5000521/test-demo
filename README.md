
# Python脚本

## 双击python手动输入处理.exe

功能：手动输入BundleId和app名字，自动修改ipa名字和模板并且创建plist文件。

注意：setting.plist模板文件不要删除，不要改动。

用法：将签好名的ipa包放在与setting.plist同级目录下，双击执行python手动输入处理.exe。完成后上传两个文件到对应的url地址即可。

# Go脚本

## go run.\godemo.go

也可以双击godemo.exe使用。

功能：go版本会自动读取CFBundleIdentifier和CFBundleDisplayName的值，不用手动输入，自动替换ipa文件名，自动修改模板并且创建plist文件。

注意：setting.plist模板文件不要删除，可以改掉里面的url地址。替换字符huandiao这个不要改，会自动替换新生成的文件名。

用法：将签好名的ipa包放在与setting.plist同级目录下，双击执行go全自动获取处理.exe。完成后上传两个文件到对应的url地址即可。
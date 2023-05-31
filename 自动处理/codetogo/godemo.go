package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"path/filepath"
	"strings"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	wenjianming := fmt.Sprintf("wz%s%d", time.Now().Format("20060102"), rand.Intn(90)+10)

	fmt.Print("请输入bundleID：")
	shuru, _ := bufio.NewReader(os.Stdin).ReadString('\n')
	shuru = strings.TrimSpace(shuru)

	fmt.Print("请输入游戏名称：")
	gamename, _ := bufio.NewReader(os.Stdin).ReadString('\n')
	gamename = strings.TrimSpace(gamename)

	inputFile, err := os.Open("setting.plist")
	if err != nil {
		fmt.Println("打开文件失败:", err)
		return
	}
	defer inputFile.Close()

	content, err := ioutil.ReadAll(inputFile)
	if err != nil {
		fmt.Println("读取文件失败:", err)
		return
	}

	newContent := strings.Replace(string(content), "huandiao", wenjianming, -1)
	newContent = strings.Replace(newContent, "com.udcs.jplay", shuru, -1)
	newContent = strings.Replace(newContent, "王者传奇", gamename, -1)

	err = ioutil.WriteFile(wenjianming+".plist", []byte(newContent), 0644)
	if err != nil {
		fmt.Println("写入文件失败:", err)
		return
	}

	ipaFile, err := findIpaFile(".")
	if err != nil {
		fmt.Println("查找 .ipa 文件失败:", err)
		return
	}

	err = os.Rename(ipaFile, wenjianming+".ipa")
	if err != nil {
		fmt.Println("重命名文件失败:", err)
		return
	}

	fmt.Println("操作完成")
}

func findIpaFile(dir string) (string, error) {
	var ipaFile string
	err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if filepath.Ext(path) == ".ipa" {
			ipaFile = path
			return filepath.SkipDir
		}
		return nil
	})
	if err != nil {
		return "", err
	}
	if ipaFile == "" {
		return "", fmt.Errorf("未找到 .ipa 文件")
	}
	return ipaFile, nil
}

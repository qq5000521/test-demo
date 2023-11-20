package main

import (
	"archive/zip"
	"errors"
	"fmt"
	"howett.net/plist"
	"io"
	"math/rand"
	"os"
	"path/filepath"
	"strings"
	"time"
)

func main() {
	msTimestamp := time.Now().UnixNano() / int64(time.Millisecond)
	timeStr := time.Unix(0, msTimestamp*int64(time.Millisecond)).Format("20060102150405")
	fileName := fmt.Sprintf("%s%s", timeStr, generateRandomString(8))

	inputFile, err := os.Open("setting.plist")
	if err != nil {
		fmt.Println("打开文件失败:", err)
	}
	defer inputFile.Close()

	content, err := io.ReadAll(inputFile)
	if err != nil {
		fmt.Println("读取文件失败:", err)
	}

	ipaPath, err := getIPAFilePath()
	if err != nil {
		fmt.Println("获取 IPA 文件路径失败:", err)
	}

	infoMap, err := ParseInfoPlistFromIPA(ipaPath)
	if infoMap != nil {
		//换掉setting.plist模板的内容
		newContent := strings.Replace(string(content), "huandiao", fileName, -1)
		newContent = strings.Replace(newContent, "com.udcs.jplay", infoMap["CFBundleIdentifier"].(string), -1)
		fmt.Println("获取的BundleId:", infoMap["CFBundleIdentifier"].(string))
		newContent = strings.Replace(newContent, "王者传奇", infoMap["CFBundleDisplayName"].(string), -1)
		fmt.Println("获取的应用名字:", infoMap["CFBundleDisplayName"].(string))

		err = os.WriteFile(fileName+".plist", []byte(newContent), 0644)

		if err != nil {
			fmt.Println("写入文件失败:", err)

		}

		err = os.Rename(ipaPath, fileName+".ipa")
		if err != nil {
			fmt.Println("重命名文件失败:", err)
		}
	}

	fmt.Scanln()
}

func getIPAFilePath() (string, error) {
	dir, err := os.Getwd() // 获取当前工作目录
	if err != nil {
		return "", err
	}

	ipaFile, err := findIpaFile(dir) // 调用之前定义的 findIpaFile 函数查找 IPA 文件
	if err != nil {
		return "", err
	}

	return ipaFile, nil
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

// 生成随机字符串
func generateRandomString(length int) string {
	strS := "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	charsetLen := len(strS)

	// 创建字符池，初始状态为字符集中的所有字符
	pool := make([]byte, charsetLen)
	for i := 0; i < charsetLen; i++ {
		pool[i] = strS[i]
	}

	str := make([]byte, length)
	for i := 0; i < length; i++ {
		// 从字符池中随机选择一个字符
		index := rand.Intn(charsetLen)
		str[i] = pool[index]

		// 将已选择的字符从字符池中移除
		pool[index] = pool[charsetLen-1]
		charsetLen--
	}

	return string(str)
}

// ParseInfoPlistFromIPA 通过"howett.net/plist"解析ipa的info.plist内容
func ParseInfoPlistFromIPA(ipaFilePath string) (map[string]interface{}, error) {
	ipaFile, err := os.Open(ipaFilePath)
	if err != nil {
		return nil, err
	}
	defer ipaFile.Close()

	ipaFileStat, err := ipaFile.Stat()
	if err != nil {
		return nil, err
	}
	fileSize := ipaFileStat.Size()

	zipReader, err := zip.NewReader(ipaFile, fileSize)
	if err != nil {
		return nil, err
	}

	for _, file := range zipReader.File {
		filePath := file.Name
		if strings.HasPrefix(filePath, "Payload/") && strings.HasSuffix(filePath, ".app/Info.plist") {
			infoFile, err := file.Open()
			if err != nil {
				return nil, err
			}
			defer infoFile.Close()

			infoPlistBytes, err := io.ReadAll(infoFile)
			if err != nil {
				return nil, err
			}

			var infoMap map[string]interface{}
			_, err = plist.Unmarshal(infoPlistBytes, &infoMap)
			if err != nil {
				return nil, err
			}

			return infoMap, nil
		}
	}

	return nil, errors.New("在IPA文件中没有找到:Info.plist")
}

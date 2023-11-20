package main

import (
	"fmt"
	"log"
	"testing"
)

func Test_godemo(t *testing.T) {
	ipaFilePath := `F:\gittest\test\自动处理\codetogo\20231120090841dERHcOwf.ipa` // Replace with the actual IPA file path

	infoMap, err := ParseInfoPlistFromIPA(ipaFilePath)
	if err != nil {
		log.Fatal(err)
	}

	// Access the parsed Info.plist data
	fmt.Println("Bundle Identifier:", infoMap["CFBundleIdentifier"])
	fmt.Println("Bundle Display Name:", infoMap["CFBundleDisplayName"])
	// Access other extracted key-value pairs
}

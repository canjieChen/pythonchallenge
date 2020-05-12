# coding=utf-8

"""
hint:everybody thinks twice before solving this.

General tips:
Use the hints. They are helpful, most of the times.
Investigate the data given to you.
Avoid looking for spoilers.

solution:
Answer:i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
explanation:
1、get every letter's ascii code,and plus 2,and then U'll get a new letter
2、but while the ascii code is bigger than 121, it should minus 26 first, then plus 2,for coming back to the lower letter
3、what the answer said "now apply on the url", means apply this way to the url, and then U'll get the new query which is "ocr"
4、replace the "map" in the old url to "ocr",then the next challenge's url will come to U

"""


def solution():
    str_old = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    # str_old = "http://www.pythonchallenge.com/pc/def/map.html"
    str_new = ""

    for i in str_old:
        if i.islower():
            if ord(i) < 121:
                str_new += chr(ord(i) + 2)
            else:
                str_new += chr(ord(i) - 26 + 2)
        else:
            str_new += i
    print(str_new)


if __name__ == "__main__":
    solution()
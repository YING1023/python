import traceback
import re
def openTEXT():
    try:
        path = 'G:\Python\Douban\Japenese.txt'
        list = []
        with open(path, 'r',encoding='utf-8') as f:
            for line in f.readlines():
                print(line)
                list.append(line.strip('\n'))  # 用strip去掉结尾的\n
        opendict ={}

    except:
        print('错误')
        traceback.print_exc()


def main():
    openTEXT()

main()
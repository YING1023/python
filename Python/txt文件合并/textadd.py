
import chardet
f = open('G:\Python/txt文件合并\ok.txt', 'rb')
data = f.read()
print(chardet.detect(data))

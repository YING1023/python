#coding=utf8

import jieba
import jieba.analyse

path='G:\Python\jieba study/计网ok.txt'
with open(path,'r') as f:
    text=f.read()


fullMode = jieba.cut(text, cut_all=True)  # 全模式
defaultMode = jieba.cut(text, cut_all=False)  # 精确模式
searchMode = jieba.cut_for_search(text)  # 搜索引擎模式

#print('全模式： \n', ' '.join(fullMode))
print('精确模式： \n', ' '.join(defaultMode))
#print('搜索引擎模式： \n', ' '.join(searchMode))

sentence = '姚家沟是东北某个偏僻山沟里只有二十几户人家的小村子，偏僻到有时候人们忽略了它的存在。'

#词语的权重分析
findWord = jieba.analyse.extract_tags(text, topK=3000, withWeight=True)
for wd, weight in findWord:
    print(wd)
    path = 'G:\Python\jieba study/result.txt'
    with open(path, 'a', encoding='utf-8') as f:
        f.write(str(wd) + '\n')
    print('打印完毕')
from os import path
from wordcloud import WordCloud

d = path.dirname('G:\Python/text mining of woedcloud/11.txt')#dirname意思为固定路径

text = open(path.join(d,'11.txt')).read()

wordcloud = WordCloud().generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(max_font_size=70).generate(text)
plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()
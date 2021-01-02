#-*- codeing =utf-8 -*-
#@Time : 2020/4/7 0007 上午 9:12
#@Author : BYP
#@File : testCloud.py
#@Software:PyCharm


import jieba                            #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import sqlite3                          #数据库


#准备词云所需的文字(词)
con = sqlite3.connect("movie.db")
cur = con.cursor()
sql = 'select instroduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
    #print(item[0])
#print(text)
cur.close()
con.close()

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))
#-------------------------------------------------------------------------------#
img = Image.open(r'.\static\assets\img\Earth.jpg')   #打开遮罩图片
img_array = np.array(img)                           #将图片转化为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="fzse_gbk.ttf"                        #字体所在位置C:\windows\Fonts
)
wc.generate_from_text(string)



#绘图
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')                                       #是否显示坐标轴
#plt.show()                                            #显示生成词云图片


#输出词云生成图片
plt.savefig(r'.\static\assets\img\earth word.jpg')

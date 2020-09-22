import re
from re import fullmatch
import codecs
import jieba
import jieba.analyse
import numpy as np

fr1 = 'D:/orig.txt'
fr2 = 'D:/orig_0.8_add.txt'
stopwords = 'D:/stopwords'

def getfile(file):
    txt1 = ""
    data = []
    keywords = []
    weighthub = []
    linehub = 0
    with open (file,'r',encoding="utf-8") as origin_file:
        for line in origin_file.readlines():
            linehub = linehub + 1
            if linehub%2 != 0:
                punctuation = '、。!;:?"\''
                text = re.sub(r'[{}]+'.format(punctuation), '', line)
                txt1 = txt1 +text.strip()
            else:
                continue
    data = txt1.split('，')
    jieba.analyse.set_stop_words('./stopwords.txt')
    for i in data :
        for feature,weight in jieba.analyse.extract_tags(i ,topK=10,withWeight=True):
            keywords.append(feature)
            weighthub.append(int(10*weight))
    return keywords,weighthub

if __name__ == "__main__":
    a,b = getfile(fr1)
    print(b)



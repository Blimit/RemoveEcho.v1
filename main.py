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
    return data

if __name__ == "__main__":
    a = getfile(fr1)
    b = getfile(fr2)
    keywords = []
    quan=[]

    jieba.analyse.set_stop_words('./stopwords.txt')
    txt1=jieba.analyse.extract_tags(a[0], topK=2, withWeight=True)
    '''
    for i in a:
        for j,k in jieba.analyse.extract_tags(i, topK=0, withWeight=True):
            quan.append(k)
            keywords.append(j)
    '''
    print (txt1)

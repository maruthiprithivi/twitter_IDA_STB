__author__ = 'maruthi'

"""
R Codes Used for preping the data before pushing it to python
setwd("~/Desktop/twitter_IDA_STB/")
data = read.csv("YSG_SG.csv", header=TRUE, sep = ",")
data1 = read.csv("YSG_UK.csv", header=TRUE, sep = ",")
data2 = read.csv("YSG_US.csv", header=TRUE, sep = ",")
dataMerge = rbind(data1,data,data2)
dataMerge$text = gsub('"','',dataMerge$text)
dataMerge$text = gsub(',','',dataMerge$text)
write.csv(dataMerge,"Preped_data.csv",row.names=FALSE)
"""

import re
import csv

data = open("sg_text.csv", mode='r')
# data1 = csv.reader(data,delimiter=',',quotechar='"')
# da = data.read()
# d1 = csv.writer(open("sentosa.csv", "wb"), delimiter=',', quotechar="", quoting=csv.QUOTE_NONE, escapechar = ",")
# header = ["Tweet"]
# d1.writerow(header)
# print data
cnt = 0
sen_cnt=0
orc_cnt=0
zoo_cnt=0

# sentosa = ["sentosa", "#sentosa", "louge", "song of the sea", "#zoukout", "zoukout"]
# print type(sentosa)
for d in data:
    cnt = cnt + 1
    d =  d.lower()
    # print type(d)
    # x = re.findall('\"[a-zA-Z0-9].+\"',d) ## ReGex do not remove
    # print x
    # xL = [wordL.lower() for wordL in x]
    # print type(x)
    # print xL
    ck1 = d.find("sentosa")
    # if ck1 > 0:
    #     sen_cnt = sen_cnt + 1
    #     print d
    # y = re.findall(".*sentosa.*",xL)
    # print y
    if re.search('sentosa',d):
         # print d
         sen_cnt = sen_cnt + 1
    elif re.search('zoukout',d):
         # print d
         sen_cnt = sen_cnt + 1
    elif re.search('\sthe\ssea\s',d):
         # print d
         sen_cnt = sen_cnt + 1
    elif re.search('[^a-z0-9]uss',d):
         # print d
         sen_cnt = sen_cnt + 1
    elif re.search('universal',d):
         # print d
         sen_cnt = sen_cnt + 1
    elif re.search('underwater',d):
         # print d
         sen_cnt = sen_cnt + 1
    elif re.search('siloso',d):
         # print d
         sen_cnt = sen_cnt + 1
    elif re.search('orchard',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('[^a-z]ion',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('mbs',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('marina\sbay\ssand',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('marinabaysands',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('singapore\sflyer',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('hippo',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('gardensbythebay',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('gardenbythebay',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('gardens\sby\sthe\sbay',d):
         # print d
         orc_cnt = orc_cnt + 1
    elif re.search('zoo',d):
         # print d
         zoo_cnt = zoo_cnt + 1
    elif re.search('night\ssafari',d):
         # print d
         zoo_cnt = zoo_cnt + 1
    elif re.search('bird\spark',d):
         # print d
         zoo_cnt = zoo_cnt + 1
    elif re.search('jurongbirdpark',d):
         # print d
         zoo_cnt = zoo_cnt + 1
    elif re.search('botanic\s',d):
         # print d
         zoo_cnt = zoo_cnt + 1
    # if cnt > 2:
    #     break
print sen_cnt
print orc_cnt
print zoo_cnt
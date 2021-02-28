import re
from collections import OrderedDict
from collections import Counter
import sys

thres=10

file_name=sys.argv[1]
m=open(sys.argv[1],'r')
f=open("common_words.txt",'r')
WTfile_name=sys.argv[1]+"'s_XML_readable.txt"
WKfile_name=sys.argv[1]+"'s_Keywords_counting.txt"
WCKfile_name=sys.argv[1]+"'s_Combined_Keywords_counting.txt"
write_txt=open(WTfile_name,'w+')
write_keywords=open(WKfile_name,"w+")
write_combined_keywords=open(WCKfile_name,'w+')
common_words=f.read()
str1=m.read()
m.close()
f.close()
d1={}
str2=""
first_search=re.compile(">([^<>]+)<")
second_search=re.compile("[a-zA-Z]{2,}")
common_words=re.findall(second_search,common_words)
fdata=re.findall(first_search,str1)
for i in fdata:
 str2=str2+i
write_txt.write(str2)
sdata=re.findall(second_search,str2)
for x in sdata:
    d1[x]=0 if not x in d1 else d1[x]+1
# for y in sdata:
#     d1[y]=d1[y]+1
for rmw in common_words:
    d1.pop(rmw,None)
d2=OrderedDict(sorted(d1.items(), key=lambda t: t[1], reverse=True))
print("Processing.....")
dlist1=[]

for i in d2.keys():         #組合字
    if(d2[i]<thres):
        break
    for j in d2.keys():
        if(d2[j]<thres):
            break
        if(i!=j):
            combine_word=i+" "+j
            result=re.findall(combine_word,str2)
            if(result):
                dlist1.append(result)    
#print(dlist1)
write_keywords.write("Keywords Quantity:"+str(len(d2))+"\n")
print("keywords Quantity:",len(d2))
for z in d2.keys():
    print (z," => ",d2[z])
    write_keywords.write(str(z)+" => "+str(d2[z])+"\n")
td1=Counter()
for i in range(0,len(dlist1)):
    td1=td1+Counter(dlist1[i])
td2=td1.most_common()
write_combined_keywords.write("Combined Keywords Quantity:"+str(len(td2))+"\n")
print("Combined Keywords Quantity:"+str(len(td2)))
for i in range(len(td2)):
    print(td2[i][0],"=>",td2[i][1])
    write_combined_keywords.write(str(td2[i][0])+" => "+str(td2[i][1])+"\n")
print("Done!!")
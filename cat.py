#coding: UTF-8

f = open('ReadMe.md','r',encoding = 'UTF-8')

data = f.read()
print(data)
count = 0
with open('ReadMe.md',encoding = 'UTF-8') as f:
    for line in f:
        count += 1
print('このテキストは' + str(count) + '行' + str(len(data)) + '文字です')


f.close
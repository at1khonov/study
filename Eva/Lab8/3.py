file = open('text.txt', 'r+', encoding='utf-8')
min=100
minword=''
strong=file.read().split(" ")
for i in range(len(strong)):
    if strong[i]=='' or strong[i]=='.' or strong[i]==',' or strong[i]=='−':
        strong[i]='errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror'

k=0
for i in range(len(strong)):
    if len(strong[i])<min:
        min=len(strong[i])
        minword=strong[i]
        for i in range(len(strong)):
            if strong[i]==minword:
                k+=1

print(k)
file.close()

import re,json

p = re.compile("(\d{2}.\d{2}.\d{4})\s(\d{2}:\d{2})\s-\s([A-Za-zıİöÖüÜçÇşŞğĞ\s]*):\s(.*)")

text = open("deneme.txt","r")
metin = str
data = []
lineCount = 0

# line counter
while True:
    txtLine = text.readline()
    if( txtLine ):
        lineCount += 1
    else:
        break

print(lineCount)
text.close()

text = open("deneme.txt","r")
for i in range(lineCount):
    metin = text.readline()
    if( p.search(metin) is None):
        continue
    data.append(
        (p.search(metin).group(1),
        p.search(metin).group(2),
        p.search(metin).group(3),
        p.search(metin).group(4))
    )

# kullanici adlari ile dosya olusturup icine mesajlari split ile kelimelere bolerek atiyor
for i in data:
    with open(str(i[2].replace(" ","-"))+".txt", "a") as txtFile:
        for j in i[3].split():
            txtFile.write(str(j)+"\n")
        txtFile.close()

text.close()
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

kelimeler = {}
for r in data:
    name = r[2]
    name = name.replace(" ","-")
    name = name.replace('ş', 's')
    name = name.replace('ğ', 'g')
    name = name.replace('ç', 'c')
    name = name.replace('İ', 'i')
    name = name.replace('ı', 'i')
    name = name.replace('ö', 'o')
    name = name.replace('ü', 'u')
    kelimeler[name] = {}

for i in data:
    name = str(i[2].replace(" ","-"))
    name = name.replace('ş', 's')
    name = name.replace('ğ', 'g')
    name = name.replace('ç', 'c')
    name = name.replace('İ', 'i')
    name = name.replace('ı', 'i')
    name = name.replace('ö', 'o')
    name = name.replace('ü', 'u')

    for j in i[3].split():
        j = j.replace("İ","i")
        j = j.lower()
        if j not in kelimeler[name]:
            kelimeler[name].update({
                j:1
            })
        else:
            kelimeler[name].update({ j: int(kelimeler[name].get(j)+1) }) 

print(kelimeler)

text.close()
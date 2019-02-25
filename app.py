#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

p = re.compile("(\d{2}.\d{2}.\d{4})\s(\d{2}:\d{2})\s-\s([A-Za-zıİöÖüÜçÇşŞğĞ\s]*):\s(.*)")

textFile = "deneme.txt"
data = []
veriler = {}

text = open(textFile,"r")
while True:
    metin = text.readline()
    if( metin ):
        data.append(
            (p.search(metin).group(1),
            p.search(metin).group(2),
            p.search(metin).group(3),
            p.search(metin).group(4))
        )
    else:
        break

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
    veriler[name] = {}

for satir in data:
    name = str(satir[2].replace(" ","-"))
    name = name.replace('ş', 's')
    name = name.replace('ğ', 'g')
    name = name.replace('ç', 'c')
    name = name.replace('İ', 'i')
    name = name.replace('ı', 'i')
    name = name.replace('ö', 'o')
    name = name.replace('ü', 'u')

    for j in satir[3].split():
        j = j.replace("İ","i")
        j = j.lower()
        if j not in kelimeler[name]:
            kelimeler[name].update({
                j:1
            })
        else:
            kelimeler[name].update({ j: int(kelimeler[name].get(j)+1) }) 

for kullanici in kelimeler:
    sayac = 0
    word = ""
    for kelime in kelimeler[kullanici]:
        if(kelimeler[kullanici].get(kelime)>sayac):
            sayac = kelimeler[kullanici].get(kelime)
            word = kelime
    veriler[kullanici].update({word:sayac})

print(veriler)

text.close()
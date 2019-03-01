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
    if(not metin):
        break
    if( re.search(p,metin) ):
        data.append(
                (p.search(metin).group(1),
                p.search(metin).group(2),
                p.search(metin).group(3),
                p.search(metin).group(4))
        )
    else:
        continue
        

kelimeler = {}

for satir in data:
    name = str(satir[2].replace(" ","-"))
    name = name.replace('ş', 's')
    name = name.replace('ğ', 'g')
    name = name.replace('ç', 'c')
    name = name.replace('İ', 'i')
    name = name.replace('ı', 'i')
    name = name.replace('ö', 'o')
    name = name.replace('ü', 'u')

    if( name not in kelimeler ):
        kelimeler[name] = {}
        veriler[name] = {}

    for kelime in satir[3].split():
        kelime = kelime.replace("İ","i")
        kelime = kelime.lower()
        if kelime not in kelimeler[name]:
            kelimeler[name].update({
                kelime:1
            })
        else:
            kelimeler[name].update({ kelime: int(kelimeler[name].get(kelime)+1) }) 

# En çok geçen kelimenin bulunması
# kelimeler veriler dictionary'sine atılıyor. istenen kullanicinin kelimesi veriler[kullanici] ile cekilebilir.
for kullanici in kelimeler.keys():
    sorted_words = sorted(kelimeler[kullanici],key=kelimeler[kullanici].get)
    word_frequency = kelimeler[kullanici].get(sorted_words[-1])
    veriler[kullanici].update({ sorted_words[-1] : word_frequency })

print(veriler)

text.close()
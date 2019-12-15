#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
p = re.compile("(\d{2}.\d{2}.\d{4})\s(\d{2}:\d{2})\s-\s([A-Za-zıİöÖüÜçÇşŞğĞ\s]*):\s(.*)")

textFile = "deneme.txt"
result, words, data = {}, {}, []
turkishCharacters = { 'ş':'s', 'ğ':'g', 'ç':'c', 'İ':'i', 'ı':'i', 'ö':'o', 'ü':'u', ' ':'-' }

text = open(textFile,"r")
while True:
    try:
        line = str( text.readline() )
    except:
        continue
    if( not line ): break
    if( not re.search(p,line) ): continue

    data.append( (p.search(line).group(1), p.search(line).group(2), p.search(line).group(3), p.search(line).group(4)) )    

for element in data:
    name = str(element[2])
    for key in turkishCharacters:
        name = name.replace(key, turkishCharacters.get(key))

    if( name not in words ):
        words[name] = {}
        result[name] = {}

    for word in element[3].split():
        word = word.lower()
        if word not in words[name]:
            words[name].update({
                word:1
            })
        else: words[name].update({ word: int(words[name].get(word)+1) }) 

# En çok geçen kelimenin bulunması
# kelimeler result dictionary'sine atılıyor. istenen kullanicinin kelimesi result[users] ile cekilebilir.
for user in words.keys():
    sorted_words = sorted(words[user],key=words[user].get)
    word_frequency = words[user].get(sorted_words[-1])
    result[user].update({ sorted_words[-1] : word_frequency })

print(result)

text.close()
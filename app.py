import re,json

cumle = """25.11.2018 13:39 - Doğukan Gedik: Semih bilimle ilgili
25.11.2018 13:39 - Doğukan Gedik: Selçuk ve Enes makina ile ilgili bende mekatronikle ilgili
25.11.2018 13:40 - Doğukan Gedik: Hem bir şeyler paylaşırken bizde  bilgi olarak ilerleriz
25.11.2018 13:40 - Doğukan Gedik: Hem de sayfa büyürse belli bir ücrette kazanırız
25.11.2018 13:40 - Doğukan Gedik: Siz ne düşünüyorsunuz ?
25.11.2018 13:41 - Selçuk Kartal: bana uyar
25.11.2018 13:42 - Doğukan Gedik: Hem bir kitle oluştururuz kendimize bakarız tutuyor bunu YouTube a da taşıyabiliriz
25.11.2018 13:43 - Doğukan Gedik: Başta biraz sabır gerekecek ama tutarsa gerçekten büyük işler yapabileceğimizi düşünüyorum
25.11.2018 13:43 - Semih: Mühendislik ile benim alakam ne olum
25.11.2018 13:43 - Doğukan Gedik: Sende bilimle ilgili paylaşım yaparsın
25.11.2018 13:43 - Doğukan Gedik: Anladığın konularla ilgili yazılar yazarsın diye seni de ekledim
25.11.2018 13:44 - Doğukan Gedik: %100 mühendislikle ilgili bir sayfa olacak diye bir şey yok ki"""

p = re.compile("(\d{2}.\d{2}.\d{4})\s(\d{2}:\d{2})\s-\s([A-Za-zıİöÖüÜçÇşŞğĞ\s]*):\s(.*)")
bol = cumle.split("\n")

name = "akseyh"
data = {}  
data['gonderi'] = []  
for kelime in bol:
    data['gonderi'].append({  
        'tarih': p.search(kelime).group(1),
        'saat': p.search(kelime).group(2),
        'isim': p.search(kelime).group(3),
        'mesaj': p.search(kelime).group(4)
    })

for i in data['gonderi']:
    print(json.dumps(i))
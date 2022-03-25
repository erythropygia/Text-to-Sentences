def text_to_sentences(file_path):
	text_content = open(file_path , "r", encoding="utf8")
	text_string = text_content.read().replace("\n", " ")
	text_content.close()
	#metinden ayrılacak kelimeler, ayrılmasını istediğinizi listeye ekleyin.
	characters_to_remove = [",",";","'s", "@", "&","*", "(",")","#","!","%","=","+","-","_",":",'"',"'","1","2","3","4","5","6","7","8","9","0","\n","","yağmur","Yağm","ayağa","Ayağa","Ayağı","ayağı","yağız","Yağız"]

	for item in characters_to_remove:
		text_string = text_string.replace(item,"")
	characters_to_replace = ["?"]

	for item in characters_to_replace:
		text_string = text_string.replace(item,".")
	sentences = text_string.split(".")

	j = 0

	for sentence in sentences:
		if len(sentence) < 1:
			continue
		elif sentence[0] == " ":
			sentence = sentence[1:]
			sentences[j] = sentence
			j += 1
		else:
			sentences[j] = sentence
			j += 1
	sentences = sentences[0:j]
	return(sentences)


def word_search(file_path,data):
	i=0
	with open(file_path , "r", encoding="utf8") as dosya:
		for satir in dosya:
			if data in satir:
				print(satir)
				i=i+1
	print(str(data) + " içeren kelime sayısı:"+str(i))
            


file_sentences=text_to_sentences('Txt/Üstün Kırdar - Fi.txt') #Metin aranacak txt dosyası
with open('CumlelereAyrilmis/Üstün Kırdar - Fi.txt', 'w', encoding="utf8") as f: #Aranan kelimenin bulunduğu cümleleri yazdıracak fonksiyon
    for item in file_sentences: 
            f.write("%s\n" % item)
print("Cümlelere Dönüştürme Başarılı\n")

word=input("Aranacak Kelimeyi Giriniz:") #Metinde cümlelerde aranacak kelime girilecek
word_search("CumlelereAyrilmis/Üstün Kırdar - Fi.txt",word) #buradaki txt dosyası cümlelere ayırdığımız dosya olacaktır.


from KitabSinif import *

print("""
|----------------------------------------|
|    Kütüphane Uygulamasına Hoşgeldiniz    |
|----------------------------------------|
""")
k = Kutuphane()

while True:
    print("""
   |--------------------------------|
   |    İşlemler;                   |
   |                                |
   |    1. Kitapları Göster         |
   |    2. Kitap Sorgulama          |
   |    3. Kitap Ekle               |
   |    4. Kitap Sil                |
   |    5. Baskı Yükselt            |
   |                                |            
   |    Çıkmak için 'q' ya basın    |
   |--------------------------------|    
    """)
    islem = input("İşlem Seçiniz: ")

    if islem == "1":
        print("_______________________________")
        k.bilgileriGoster()

    elif islem == "2":
        yayinEvi = input("Hangi yayın evinin kitaplarını göstermesini istersiniz?: ")
        k.kitapSorgula(yayinEvi)

    elif islem == "3":
        k.kitapEkle()

    elif islem == "4":
        k.kitapSil()

    elif islem == "5":
        yayinEvi = input("Baskısını yükseltmek istediğiniz yayın evinin ismini giriniz: ")
        baskiSayisi = input("Baskısını sayısını giriniz: ")
        k.baskiYukselt(yayinEvi,baskiSayisi)

    elif islem == "q":
        baglaanti.close()
        break

    else:
        print("Geçersiz işlem! Lütfen doğru işlem giriniz.")





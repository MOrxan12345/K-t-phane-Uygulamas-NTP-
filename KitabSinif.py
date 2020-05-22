# Kütüphane Programına Hoşgeldiniz.
#
# İşlemler;
#
# 1. Kitapları Göster v
#
# 2. Kitap Sorgulama v
#
# 3. Kitap Ekle v
#
# 4. Kitap Sil v
#
# 5. Baskı Yükselt v
#
# Çıkmak için 'q' ya basın.
# ***********************************

import sqlite3

baglaanti = sqlite3.connect("kutuphane.db")
cursor = baglaanti.cursor()


class Kitap():



    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

class Kutuphane():

    def __init__(self):
        self.baglantiOlustur()

    def baglantiOlustur(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(Isim TEXT, Yazar TEXT,Yayinevi TEXT, Tur TEXT, Baski INT)")
        baglaanti.commit()

    def bilgileriGoster(self):
        cursor.execute("Select * From kitaplik")
        veri = cursor.fetchall()

        #Tamamdır doğru çalışıyor

        for x in veri:
            print(f"Kitab Adı: {x[0]}\nKitab Yazar Adı: {x[1]}\nYayın Evi: {x[2]}\nKitap Türü: {x[3]}\nKitap Baskı Sayısı: {x[4]}")
            print("_______________________________")

        #Tamamdır doğru calışıyor

    def kitapSorgula(self,yayinEvi):

        cursor.execute("Select * From kitaplik where Yayinevi = ?",(yayinEvi,))
        veri = cursor.fetchall()
        for x in veri:
            print(f"Kitab Adı: {x[0]}\nKitab Yazar Adı: {x[1]}\nYayın Evi: {x[2]}\nKitap Türü: {x[3]}\nKitap Baskı Sayısı: {x[4]}")
        #Tamamdır doğru calışıyor


    def kitapEkle(self):

        isim = input("Kitab ismini giriniz: ")
        yazar = input("Kitab yazarının ismini giriniz: ")
        yayinevi = input("Kitab yayın evinin ismini giriniz: ")
        tur = input("Kitab türünü giriniz: ")
        baski = int(input("Kitab baskı sayısını giriniz: "))

        kitap = Kitap(isim,yazar,yayinevi,tur,baski)

        cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?,?)",(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        baglaanti.commit()

        #Tamamdır doğru calışıyor

    def kitapSil(self):
        k_adi = input("Silmek istediğiniz kitabın adını giriniz: ")
        #k_yazar_adi = input("Silmek istediğiniz kitabın yazarının adını giriniz: ")

        cursor.execute("Delete  From kitaplik where Isim = ?",(k_adi,))
        baglaanti.commit()

        #Tamamdır doğru calışıyor

    def baskiYukselt(self,yayinEvi,baskiSayisi):
        cursor.execute("Update kitaplik set Baski = ? where Yayinevi = ?",(baskiSayisi,yayinEvi,))
        baglaanti.commit()

        #Tamamdır doğru calışıyor
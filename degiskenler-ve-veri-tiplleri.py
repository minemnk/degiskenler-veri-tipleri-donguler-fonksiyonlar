####Kullanıcıdan veri alma
isim= input("Lutfen isminizi giriniz : ")
yas = int(input("Lutfen yasinizi giriniz : "))
yil= int(input("Lutfen dogum yilinizi girin: "))

print(f"Merhaba {isim}, {yas} yasindasin ve {yil} yilinda dogmussun!")


#### kullanicidan sayi alarak islem yapma
birinci_sayi =float(input("Birinci sayiyi girin: "))
ikinci_sayi =float(input("ikinci sayiyi girin: "))

toplama= birinci_sayi + ikinci_sayi
cikarma= birinci_sayi - ikinci_sayi
carpim = birinci_sayi * ikinci_sayi
if (ikinci_sayi != 0):
   bolme = birinci_sayi / ikinci_sayi
else:
  bolme= print("Bir sayiyi 0'a bolemezsiniz.")

print("Toplama isleminin sonucu:", toplama) 
print("Cikarma isleminin sonucu:", cikarma)
print("Carpma isleminin sonucu:", carpim)
print("Bolme isleminin sonucu:", bolme)

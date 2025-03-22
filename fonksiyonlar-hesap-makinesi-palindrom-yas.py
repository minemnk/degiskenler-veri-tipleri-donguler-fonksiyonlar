### Girilen iki sayinin toplami, farkini,çarpımını ve bölümünü bulan hesap makinesi


def hesap_makinesi(sayi1, sayi2):


  toplam = sayi1 + sayi2
  fark = sayi1 - sayi2
  carpim = sayi1 * sayi2


  if sayi2 != 0:
    bolum = sayi1 / sayi2
  else:
    bolum = "0'a bölünemez!"

  return toplam, fark, carpim, bolum


# Kullanıcıdan iki sayı alalim
sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("İkinci sayiyi girin: "))

toplam, fark, carpim, bolum = hesap_makinesi(sayi1, sayi2)

print("Toplam:  ", toplam)
print("Fark: ", fark)
print("Carpim: ", carpim)
print("Bölüm:  ", bolum)



print("***************************")
#### Kullanicinin girdiği bir kelimenin polindrom olup olmadığını kontrol eden bir fonksiyon yazin.
### polindrom ileri ve geri okunduğunda ayni olan kelime

def ters_cevir(kelime):
  return kelime[::-1]

def polindrom_mu(kelime):
  kelime = kelime.lower()  # Büyük/küçük harf duyarlılığını kaldır
  return kelime == ters_cevir(kelime)

# Kullanıcıdan kelime al
kelime = input("Bir kelime girin: ")

# Polindrom kontrolü yap ve sonucu yazdır
if polindrom_mu(kelime):
  print(kelime, "bir polindromdur.")
else:
  print(kelime, "bir polindrom değildir.")


print("*******************************************")

def yuze_kalan(yas):
  yuz_yas = 100 
  kalan_sure = yuz_yas - yas  
  return kalan_sure 

yas = int(input("Yasiniz kaç? "))


kalan_yil = yuze_kalan(yas)

print(kalan_yil, "yil sonra 100 yasina gireceksiniz.")
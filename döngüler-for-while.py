#1den 100e kadar ekrana yazdirma
for i in range(1,101):
  print(i)

print("***********************************")

#1den yüze kadar çift sayilari ekrana yazdirma
for i in range(0,100,2):
  print(i)

#kullanicidan sayi alıp bunun faktoriyelini alan program
sayi= int(input("Bir sayi giriniz: "))
faktoriyel=1
if sayi < 0:
   print("Negatif sayiarin faktoriyeli yok")
elif sayi== 0:
  print("0!=1")
else:
  for i in range(1,sayi+1):
    faktoriyel=faktoriyel*i
  print(faktoriyel)


print("******************************")

###  1 den 100 e kadar olan tüm asal sayıları bulan bir program yazın

print("1'den 100'e kadar olan asal sayılar:")

sayi = 2
while sayi <= 100:
    bolen = 2
    asal_mi = True

    while bolen < sayi:
        if sayi % bolen == 0:
            asal_mi = False
            break 
        bolen += 1

    if asal_mi:
        print(sayi, end=" ")
    
    sayi += 1
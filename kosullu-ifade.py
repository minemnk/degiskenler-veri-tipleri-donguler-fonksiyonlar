#Kuulanıcıdan notunu alrak not sistemine göre hesaplama
''' 90-100 =A    
     80--89=B
     70-79=C
     60-69=D
     0-59=F
'''
notunuz=int(input("Lutfen notunuzu girn :"))
 
if notunuz>=90 and notunuz <=100:
  print("Notunuz:AA")
elif notunuz>=80 and notunuz<=89:
  print("Notunuz:B")
elif notunuz>=70 and notunuz<=79:
  print("Notunuz:C")
elif notunuz>=60 and notunuz<=69:
  print("Notunuz:D")
elif notunuz>=0 and notunuz<=59:
  print("Notunuz:F")


###KULLANICININ GİRGİGİ SAYİ TEK Mİ CİFT Mİ
sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
    print("Sayi çifttir.")
else:
    print("Sayi tektir.") 

### kullanıcın yaşina göre hangi yaş grubunda olduğunu hesaplama
yasiniz = int(input("Yaşınızı girin: "))

if yasiniz >= 0 and yasiniz <= 12:
    print("Çocuk grubundasiniz")
elif yasiniz >= 13 and yasiniz <= 19:
    print("Genc grubundasiniz")
elif yasiniz >= 20 and yasiniz <= 59:
    print("Yetiskin grubundasiniz") 
else :
  print("Yasli grubundasiniz")
# angka = 1

# while angka > 0 and angka < 11:
#     angka = int(input("Masukkan bilangan bulat : "))
#     if angka >= 1:
#         print("Bilangan Positif")
#     elif angka < 0:
#         print("Bilangan Negatif")



while True:
    nama = input("Masukkan nama anda: ")
    if nama == "X":
        break
    elif nama == "Adi":
        continue
      
    print("Selamat datang", nama)
while True:
    number = int(input("Masukkan angka: "))
    if number == 0:
        break

    if number % 2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")
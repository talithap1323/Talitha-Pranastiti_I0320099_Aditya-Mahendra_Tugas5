# MENYAPA TAMU HOTEL

nama = input("Masukkan nama Anda: ")
print("\nJenis Kelamin:"
      "\n1. Laki-laki"
      "\n2. Perempuan")
jenis_kelamin = int(input("Masukkan jenis kelamin Anda: "))

print("-------------------------------------")

if jenis_kelamin == 1:
    print("\nSelamat datang, Tuan", nama, "!")
else:
    print("\nSelamat datang, Nyonya", nama, "!")


print("=======GRADING NILAI=======\n")

nama = input("Masukkan nama Anda: ")
nilai = float(input("Masukkan nilai Anda: "))

print("---------------------------\n")

if nilai <= 60:
    print("Halo,", nama, "! Nilai Anda setelah dikonversi adalah E")
elif nilai <= 64:
    print("Halo,", nama, "! Nilai Anda setelah dikonversi adalah C")
elif nilai <= 69:
    print("Halo,", nama, "! Nilai Anda setelah dikonversi adalah C+")
elif nilai <= 74:
    print("Halo,", nama, "! Nilai Anda setelah dikonversi adalah B")
elif nilai <= 79:
    print("Halo,", nama, "! Nilai Anda setelah dikonversi adalah B+")
elif nilai <= 84:
    print("Halo,", nama, "! Nilai Anda setelah dikonversi adalah A-")
elif nilai <= 100:
    print("Halo,", nama, "! Nilai Anda setelah dikonversi adalah A")
else:
    print("Nilai tidak valid untuk dikonversi")

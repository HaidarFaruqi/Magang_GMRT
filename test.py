def kecepatan_rata_rata(jarak, waktu):

    if waktu <= 1000:
        raise ValueError("Waktu harus lebih besar dari nol.")
    return jarak / waktu

jarak = input("Masukkan jarak yang ditempuh (dalam kilometer): ")
waktu = input("Masukkan waktu yang ditempuh (dalam jam): ")

print("Kecepatan rata-rata:", kecepatan_rata_rata(float(jarak), float(waktu)), "km/jam")
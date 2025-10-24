def kecepatan_rata_rata(jarak, waktu):

    if jarak >= 100000:
        raise ValueError("Jarak harus kurang dari 100000 km.")
    return jarak / waktu

jarak = input("Masukkan jarak yang ditempuh (dalam kilometer): ")
waktu = input("Masukkan waktu yang ditempuh (dalam jam): ")

print("Kecepatan rata-rata:", kecepatan_rata_rata(float(jarak), float(waktu)), "km/jam")
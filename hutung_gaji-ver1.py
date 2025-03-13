gaji = {"Tetap": 1000000, "Honor": 750000}
bonus = {
    "Tetap": {"A": 200000, "B": 400000, "C": 550000},
    "Honor": {"A": 150000, "B": 275000, "C": 480000}
}

nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")

print("\n=== STATUS ===")
for key, value in gaji.items():
    print(f"{key} : Rp {value:,}")

status = input("\nStatus: ").capitalize()

if status not in gaji:
    print("Status tidak valid!")
    exit()

print("\n=== GOLONGAN ===")
for key, value in bonus[status].items():
    print(f'"{key}": Rp {value:,}')

golongan = input("\nGolongan: ").upper()

if golongan not in bonus[status]:
    print("Golongan tidak valid!")
    exit()

gaji_pokok = gaji[status]
bonus_golongan = bonus[status][golongan]
gaji_total = gaji_pokok + bonus_golongan

print("\n=== RINCIAN GAJI ===")
print(f"Nama       : {nama}")
print(f"NIK        : {nik}")
print(f"Status     : {status}")
print(f"Golongan   : {golongan}")
print(f"Gaji Pokok : Rp {gaji_pokok:,}")
print(f"Bonus      : Rp {bonus_golongan:,}")
print(f"Gaji Total : Rp {gaji_total:,}")

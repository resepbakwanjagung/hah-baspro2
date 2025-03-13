gaji = {"Tetap": 1000000, "Honor": 750000}
bonus = {
    "Tetap": {"A": 200000, "B": 400000, "C": 550000},
    "Honor": {"A": 150000, "B": 275000, "C": 480000}
}

for status, gaji_pokok in gaji.items():
    print(f"\nStatus: {status}")

    for golongan, bonus_golongan in bonus[status].items():
        gaji_total = gaji_pokok + bonus_golongan

        print(f"\nGolongan: {golongan}")
        print(f"    Gaji Pokok: {gaji_pokok:,}")
        print(f"    Bonus: {bonus_golongan:,}")
        print(f"    Total Gaji: {gaji_total:,}")

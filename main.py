satrlar = ["Bu birinchi satr", "Ikkinchi satr", "Uchinchi satr juda uzun"]
saralangan_satrlar = sorted(satrlar, key=lambda satr: len(satr.split()))
print(saralangan_satrlar)

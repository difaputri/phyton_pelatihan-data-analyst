a = 100
b = 10 ** 2
c = 101

print (f"nilai a adalah {a}")
print (f"nilai b adalah {b}")
print (f"nilai c adalah {c}")

#sama dengan
a_apakah_sama_dengan_b = a == b
a_apakah_sama_dengan_c = a == c

print (f"{a} apakah sama dengan {b}? {a_apakah_sama_dengan_b}")
print (f"{a} apakah sama dengan {c}? {a_apakah_sama_dengan_c}")

#tidak sama dengan
a_apakah_tdk_sama_dengan_c = a != c
print (f"{a} apakah tidak sama dengan {c}? {a_apakah_tdk_sama_dengan_c}")

#lebih besar
a_lebih_besar_dari_c = a > c
print(f"{a} apakah lebih besar dari {c}? {a_lebih_besar_dari_c}")

#lebih kecil
a_lebih_kecil_dari_c = a < c
print(f"{a} apakah lebih kecil dari {c}? {a_lebih_kecil_dari_c}")

#lebih besar sama dengan
a_lebih_besar_sama_dengan_dari_c = a >= c
print(f"{a} apakah lebih besar sama dengan {c}? {a_lebih_besar_sama_dengan_dari_c}")

#lebih kecil sama dengan
a_lebih_kecil_sama_dengan_dari_c = a <= c
print(f"{a} apakah lebih kecil sama dengan {c}? {a_lebih_kecil_sama_dengan_dari_c}")
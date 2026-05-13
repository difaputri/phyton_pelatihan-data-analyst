index = [0, 1, 2, 3, 4, 5]
nama = ["Alice", "Bob", "Charlie", "Edi", "Farah", "Gita", "Hasti"]
# nilai = [80, 90, 100, 80, 60, 90, 100]

nama_slice_3_tengah = nama[2:5]
# nilai_slice_3_tengah = nilai[2:5]

print(nama_slice_3_tengah)
# print(nilai_slice_3_tengah)


#slice
print("\n SLICE")
nama_slice_3_tengah[2] = "Clara"
# nilai_slice_3_tengah[0] = 99
print("\n")
print(nama_slice_3_tengah)
# print(nilai_slice_3_tengah)

#insert
print("\n INSERT")
nama_slice_3_tengah.insert(1, "Zara")
# nilai_slice_3_tengah.insert(1, 80)
# print("\n")
print(nama_slice_3_tengah)
# print(nilai_slice_3_tengah)

#APPEND
print("\n APPEND")
nama_slice_3_tengah.append("Dina")
# nilai_slice_3_tengah.append(100)
# print("\n")
print(nama_slice_3_tengah)
# print(nilai_slice_3_tengah)

#SORT
nama_slice_3_tengah.sort()
print("\n SORT")
print(nama_slice_3_tengah)

#POP
print("\n POP")
remove_nama = nama_slice_3_tengah.pop(1)
print(remove_nama)

#REVERSE



# Print dengan index
# print("\n")
# print("Print dengan index")
# print(f"Panjang data dari nama = {len(nama)}")
# print(f"Nama {nama[1]} mendapatkan nilai {nilai[1]}")

# for z in range(len(nama)):
#     print(z)
#     print(f"Nama {nama[z]} mendapatkan nilai {nilai[z]}")
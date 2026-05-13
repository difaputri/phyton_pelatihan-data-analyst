berat_badan = float(input("Masukan Berat Badan (kg): "))
tinggi_badan = float(input("Masukan Tinggi Badan (cm): "))

bmi = berat_badan / ((tinggi_badan/100)**2)
print(f"BMI kamu adalah {bmi:.2f}")

if bmi < 18.5 :
    print("Anda termasuk kategori Underweight")
elif bmi >= 18.5 and bmi < 25 :
    print("Anda termasuk kategori Normalweight")
elif bmi >= 25 and bmi < 30 :
    print("Anda termasuk kategori Overweight")
elif bmi >= 30 and bmi < 50 :
    print("Anda termasuk kategori Obesitas")
else:
    print("ERROR")
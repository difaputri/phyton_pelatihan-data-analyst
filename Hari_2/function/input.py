import aritmatika as f

berat_badan = float(input("Masukan Berat Badan (kg): "))
tinggi_badan = float(input("Masukan Tinggi Badan (cm): "))

bmi = f.bmi(berat_badan, tinggi_badan)
print("BMI kamu adalah", bmi)

f.bmi_check(bmi)

# print(f.add(10, 5))
# print(f.bmi(50, 170))
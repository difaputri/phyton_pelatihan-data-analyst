def add(a = None, b = None):
    if a == None or b == None:
        print("Parameter tidak lengkap")
        return
    
    totalTambah = a + b
    return totalTambah

# jumlah = add (10, 5)
# print(jumlah)

def substract(a = None, b = None):
    if a == None or b == None:
        print("Parameter tidak lengkap")
        return
    
    totalKurang = a - b
    return totalKurang

# kurang = substract(5, 10)
# print(kurang)

def bmi(berat_badan=None, tinggi_badan=None):
    if berat_badan == None or tinggi_badan == None:
        print("Parameter tidak lengkap")
        return
    
    total = berat_badan / ((tinggi_badan/100)**2)
    return total

def bmi_check(bmi):
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

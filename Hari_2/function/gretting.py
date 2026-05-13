from datetime import datetime

def sapa():
    print("Selamat Datang")

def sapaNama(nama=None):
    if nama is None:
        print("Silahkan masukkan nama Anda")
        return

    print(f"Hai, {nama}!")

sapa()
sapaNama("Difa")
print(f"\n{datetime.now()}")
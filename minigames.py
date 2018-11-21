import os

print("===============================")
print("   DAFTAR GAME YANG TERSEDIA   ")
print("===============================")
print("1. Tebak Kata                  ")
print("2. Tebak Angka                 ")
print("3. Lempar Dadu                 ")
print("4. Arah Petualangan            ")
print("5. Gunting Batu Kertas         ")
print("6. Cerita Maker                ")
print("0. Keluar Dari Game            ")
pilih=raw_input("Masukkan Pilihan : ")
if (pilih == '1'):
      os.system("python tebakkata.py")
      os.system("sleep 2")   
elif (pilih == '2'):
      os.system("python tebakangka.py")
      os.sytem("sleep 2")
elif (pilih == '3'):
      os.system("python lempardadu.py")
      os.system("sleep 2")
elif (pilih == '4'):
      os.system("python arahpetualangan.py")
      os.system("sleep 2")
elif (pilih == '5'):
      os.system("python guntingbatukertas.py")
      os.system("sleep 2")
elif (pilih == '6'):
      os.system("python ceritamaker.py")
      os.system("sleep 2")
elif (pilih == '0'):
      os.system("clear")
      os.system("figlet KELUAR")
      os.system("exit")
else :
      print("Format Yang Anda Masukkan Salah")
      print("Please Wait")
      os.system("sleep 3")
      os.system("clear")
      os.system("python2 asd.py")
      

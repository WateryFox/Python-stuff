import os
import time
def clear():
  _ = os.system('clear')

# EXAMPLE 1
def ex1():
  list = ["satu", "dua", "tiga", "empat", "lima"]
  X = int(input("Masukkan angka(1-5): "))
  print(list[X - 1])

# SECTION 1
def sect1():
  try:
    value = float(input("Berapa nilau mu? "))
    if value < 0 or value > 100:
      print("Error")
    else:
      if value >= 90:
        print("Skormu adalah A")
      elif value >= 70:
        print("Skormu adalah B")
      elif value >= 50:
        print("Skormu adalah C")
      elif value >= 20:
        print("Skormu adalah D")
      else:
        print("Skormu adalah E")
      print()
  except:
    print("Error\n")

# SECTION 2
def sect2():
  list = []
  try:
    for i in range(4):
      list.append(int(input("Masukkan umur: ")))
      list.sort()
      print(list)
  except:
    print("Error")
    exit()
  print("\nUmur termuda: ", list[0])

# SECTION 3
def sect3():
  x = int(input("Total kehadiran siswa: "))
  y = int(input("Total ketidakhadiran siswa: "))
  z = x / (x + y) * 100
  print("Persentase kehadiran siswa " + str(int(z)) + "%")
  if z >= 75:
    print("Siswa boleh mengikuti ujian")
  else:
    print("Siswa tidak boleh mengikuti ujian")

# SECTION 4
def sect4():
  pay = 0
  try:
    gender = input("Jenis kelamin (M/F): ")
    if not (gender.upper() == "M" or gender.upper() == "F"):
      ERROR
    age = int(input("Umur: "))
    if not (age > 17 and age < 41):
      ERROR
    days = int(input("Jumlah hari bekerja: "))
    if days < 0:
      ERROR
  except:
    print("Error")
    exit()
  if gender.upper() == "M":
    if age < 30:
      pay += 700 * days
    else:
      pay += 750 * days
  else:
    if age < 30:
      pay += 800 * days
    else:
      pay += 850 * days
  print("Upah yang harus anda: Rp."+str(pay))

# SECTION 5
def sect5():
  try:
    x = int(input("Masukkan nilai semester 1: "))
    y = int(input("Masukkan nilai semester 2: "))
    if (x or y) < 0 or (x or y) > 100:
      ERROR
  except:
    print("Error")
    exit()
  print()
  if y >= 90:
    print("Excellent Score")
  elif y >= 70:
    print("Good Score")
  elif y >= 50:
    print("Adequate Score")
  elif y >= 30:
    print("Poor Score")
  else:
    print("Fail")
  z = y - x
  if z >= 10:
    print("Major Improvement")
  elif z >= 1:
    print("Good Improvement")
  elif z >= 0:
    print("Conistent & Great effort")
  elif z >= -9:
    print("Need More Effort")
  else:
    print("Declining Progress, Need Improvement")

# SECTION 6
def sect6():
  try:
    y = float(input("Masukan tinggi suhu: "))
    x = int(input("Pilih satuan suhu yang ingin konversi.\n1.Celcius\n2.Fahrenheit\n3.Kelvin\n"))
    clear()
    z = int(input("Pilih satuan suhu tujuan konversi.\n1.Celcius\n2.Fahrenheit\n3.Kelvin\n"))
    clear()
    if x < 1 or x > 3 or z < 1 or z > 3:
      ERROR
    if x == 1:
      if z == 1:
        print("Hasilnya adalah",int(y),"celcius.")
      elif z == 2:
        print("Hasilnya adalah",int(y * 9/5 + 32),"fahrenheit.")
      else:
        print("Hasilnya adalah",int(y + 273.15),"kelvin.")
    elif x == 2:
      if z == 1:
        print("Hasilnya adalah",int((y - 32) * 5/9),"celcius.")
      elif z == 2:
        print("Hasilnya adalah",int(y),"kelvin.")
      else:
        print("Hasilnya adalah",int((y - 32) * 5/9 + 273.15),"fahrenheit.")
    elif x == 3:
      if z == 1:
        print("Hasilnya adalah",int(y - 273.15),"celcius.")
      elif z == 2:
        print("Hasilnya adalah",int((y - 273.15) * 9/5 + 32),"fahrenheit.")
      else:
        print("Hasilnya adalah",int(y),"kelvin.")
  except:
    print("Error")
    exit()

# SECTION 7
def sect7():
  try:
    x = int(input("Masukkan angka: "))
  except:
    print("Error")
    exit()
  if x % 2 == 0:
    print("Angka genap")
  else:
    print("Angka ganjil")

# SECTION 8
def sect8():
  try:
    x = int(input("Masukan sekon: "))
  except:
    print("Error")
    exit()
  hour = menit = 0
  while x >= 3600:
    hour += 1
    x -= 3600
  while x >= 60:
    menit += 1
    x -= 60
  print(f'{hour:02}:{menit:02}:{x:02}')

# SECTION 9
def sect9():
  try:
    tipe = int(input("1. Download\n2. Upload\n"))
    clear()
    satuan = int(input("1. MB\n2. GB\n"))
    clear()
    if tipe or satuan < 1 or tipe or satuan > 2:
      ERROR
    size = int(input("Size file: "))
    clear()
    if satuan == 2:
      size *= 1000
    print(size,"MB")
  except:
    print("Error")
    exit()
  size *= 8
  hour = menit = 0
  if tipe == 1:
    dt = size / 20
  else:
    dt = size / 5
  while dt >= 3600:
    hour += 1
    dt -= 3600
  while dt >= 60:
    menit += 1
    dt -= 60
  print(f'{hour:02}:{menit:02}:{int(dt):02}')

# SECTION 10
def sect10():
  try:
    no = int(input("Masukkan nomor loker: "))
    if no < 1:
      ERROR
    else:
      if no % 4 == 0:
        print("Loker anda berwarna biru.")
      elif no % 4 == 1:
        print("Loker anda berwarna merah.")
      elif no % 4 == 2:
        print("Loker anda berwarna putih.")
      elif no % 4 == 3:
        print("Loker anda berwarna kuning.")
  except:
    print("Error")
    exit()

# SECTION 11
def sect11():
  try:
    x = int(input("Pilih Algoritma:\n1.-1 & +3 \n2.+2 & +4\n3.*2 & *3\n"))
    if x < 1 or x > 3:
      ERROR
    starting = int(input("Masukkan angka awal: "))
    list = []
    func = 0
    while x == 1:
      list.append(starting)
      clear()
      print(list)
      starting -= 1
      time.sleep(0.2)
      list.append(starting)
      clear()
      print(list)
      starting += 3
      time.sleep(0.2)
    while x == 2:
      list.append(starting)
      clear()
      print(list)
      starting += 2
      time.sleep(0.2)
      list.append(starting)
      clear()
      print(list)
      starting += 4
    while x == 3:
      list.append(starting)
      print(list)
      time.sleep(0.2)
      func += 3
      list.append(func)
      print(list)
      time.sleep(0.2)
      starting += 2
  except:
    print("Error")
    exit()

def sect11A():
  sum = 0
  x = int(input("Masukkan angka: "))
  l = list(range(1, x + 1))
  for i in l:
      sum += i
  num = ""
  for i in range(len(l)):
      # num += str(l[i])
      num += str(l[i])
      if i != len(l) - 1:    
          num += " + " 
  print(f"Jumlah dari {num} adalah {sum}")


#   sum = 0
#   x = int(input("Masukkan angka: "))
#   l = list(range(1, x + 1))
#   for i in l:
#       sum += i
#   num = " + ".join(map(str, l))
#   print(f"Jumlah dari {num} adalah {sum}")

  # sum = 0
  # x = input("Masukkan angka-angka: ")
  # l = [int(i) for i in x.split()]
  # for i in l:
  #   sum += i
  # num = " + ".join(map(str, l))
  # print("Jumlah dari",num,"adalah",sum)

  # sum = 0
  # num = ""
  # l = []
  # for i in range(1, 11):
  #     print(i)
  #     l.append(i)
  #     sum += i
  # for i in l:
  #   num+= str(i) +","
  # print("Jumlah dari", num, "tersebut adalah", sum)

def sect12():
  n = int(input("Masukkan nilai n: "))
  a, b = 0, 1
  for i in range(n):
      a, b = b, a + b
  print("Fibonacci ke", n, "adalah", a)

def sect13():
  pass
# STARTER
x = input("Run program:\n0.Ex1(int->str)\n1.Sect1(grading nilai)\n2.Sect2(sorting umur)\n3.Sect3(persentase kehadiran)\n4.Sect4(upah biased)\n5.Sect5(perkembangan nilai)\n6.Sect6(konverter suhu)\n7.Sect7(ganjil genap)\n8.Sect8(konverter sekon)\n9.Sect9(download / upload)\n10.Sect10(loker berwarna)\n11.Sect11(algo angka)\n-1.Sect11A(Biofinancial)\n12.Sect12(fibonacci)\n13.Sect13()\nInput: ")
clear()
if x == "0":
  ex1()
elif x == "-1":
  sect11A()
elif x == "1":
  sect1()
elif x == "2":
  sect2()
elif x == "3":
  sect3()
elif x == "4":
  sect4()
elif x == "5":
  sect5()
elif x == "6":
  sect6()
elif x == "7":
  sect7()
elif x == "8":
  sect8()
elif x == "9":
  sect9()
elif x == "10":
  sect10()
elif x == "11":
  sect11()
elif x == "12":
  sect12()
elif x == "13":
  sect13()
else:
  exit()
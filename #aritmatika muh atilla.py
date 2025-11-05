#aritmatika 1
a = float(input("masukkan angka pertama: "))
op = input("masukkan operator (+,-): ")
b = float(input("masukkan angka kedua: "))
if op == '+':
    hasil = a + b
elif op == '-':
    hasil = a - b
print(f"hasil: {hasil}")
print(        )

#aritmatika 2
a = int(input("masukkan angka pertama (bilangan bulat): "))
b = int(input("masukkan angka kedua (bilangan bulat): "))
#melakukan operasi
jumlah = a + b
selisih = a - b
kali = a * b
#menampilkan hasil
print("\n=== Hasil Operasi-==")
print(f"{a} + {b} = {jumlah}")
print(f"{a} - {b} = {selisih}")
print(f"{a} * {b} = {kali}")
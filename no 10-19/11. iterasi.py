# Iterasi 

# => Dalam bahasa inggris (loop), adalah sebuah kode yang berfungsi untuk mengulang statement yang ada di dalam blok nya selama kondisi yang diberikan bernilai True / element array belum mencapai pojok.

# => Spread Operator dalam bahasa Python dilambangkan dengan tanda * didepan variabel, spread operator ini digunakan untuk mengeluarkan element dari array yang membungkusnya.
# Spread operator dapat digunakan oleh tipe data yang bersifat itterable atau memiliki index atau dapat di looping.
# contoh : *array => el,el,el, ...el

# For Loop

# Ada 2 macam For loop didalam python yaitu for in... dan for in range ...

# a. for in => digunakan untuk mengulang dan mengeluarkan element array, variabel disini akan berisi element array urut dari index terkecil.
angka = [1,2,3,4,5,6,7,8,9,10]
for i in angka :
    if(i % 2) :
        print("angka %s adalah ganjil"%(i))
    elif (not(i % 2)) :
        print("angka %i adalah genap"%(i))

# b. for in range => cara kerjanya adalah mengulang statement dibawah yang diidentasi sampai jarak yang ditentukan, variabel disini akan berisi index perulanganya, dan akan bertambah setiap berakhirnya satu perulangan
# INGAT!! Variabel disini akan dimulai dari angka 0
for index in range (2) : # index dimulai dari angka 0, dan jaraknya sampai 2, jadi kita hanay melooping statement dibawahnya sebanyak 2 kali. 0+1=1, 1+1=2 .
    print(index)
    print("///")

# destructuring element array, tuple, dll
nested_tup = ((1,2), (3,4), (5,6), (7,8))
for a,b in nested_tup : # element pertama masuk ke a, element ke 2 masuk ke b
    print(a, b)


# While Loop
#   => cara kerja nya sama seperti for loop, namun hanya berbeda cara penulisanya saja
# ada 3 argument yang dapat sangat berguna ketika menggunakan while loop
    # 1. break => untuk menghentikan looping
    # 2. continue => untuk mengulang looping dari awal
    # 3. pass => sebuah looping yang tidak melakukan apa apa
# ada 3 buah item yang *wajib* ketika menggunakan while loop
    # 1. nilai awal / nilai penentu 
    # 2. kondisi terminasi
    # 3. decrement / increment pada nilai awal jika bentuknya adalah integer/float

#  memprint angka dari 1 - 10 menggunakan while loop
nilai_awal = 1; # nilai awal
while (nilai_awal <= 10) :  # kondisi
    print(nilai_awal) # print value nilai_awal
    nilai_awal +=1 # inc pada nilai_awal

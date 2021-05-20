# Range 
# Range dalam for loop digunakan sebagai jarak / batas loop dijalankan
# Range memiliki 3 parameter yaitu mulai dari angka berapa, berhenti di angka berapa, lompatan angka

for i in range (1,10,2) : 
    # dimulai dari angka 1,
    # berhenti ketika i bernilai 10, jadi 10 tidak diikutkan
    # masuk ke dalam blok setiap 2 kali iterasi.
    print(i) # => 1,3,5,7,9


# range juga dapat kita gunakan untuk men-generate sebuah isi list angka yang berurutan
list_range = list(range(1,10)) # INGAT! saat menggunakan range, wajib membungkungnya dengan list() bukan []
print(list_range)


# Enumerate
# => adalah sebuah variabel yang menyimpan indeks ketika perulangan for in dilakukan, 
# => biasanya kan kalau kita melakukan iterasi for in, loopnya hanya diberikan 1 variabel yang akan menyimpan value dari element yang di loop,, sekarang kita belajar enumerate, yaitu indeks ke berapa saat ini
# dengan cara manual
indeks = 0 
items = list(range(1, 6)) 
# INGAT!! angka dibelakang koma tidak akan diikutkan, jadi rangenya : 1- (angka belakang -1)
print(items)
for i in items :
    print("%s memiliki indeks ke %s"%(i, indeks)) 
    indeks +=1

# Menggunakan enumerate
for i in enumerate (items) :
    print(i) 
    # maka i akan berbentuk tuple yang memiliki 2 elemen, 1 adalah indeks dan 2 adalah value nya

# Memecah tuple yang dihasilkan oleh enumerate (unpacking tuple) pada for in
for (i, v) in enumerate (items) : 
    # langsung masuk ke variabel i dan v, i untuk didepan atau indeks dan v untuk dibelakang atau value
    print("ini indeks ke %s dengan value %s"%(i, v))


# zip, berfungsi untuk menggabungkan array ke dalam iterasi, menghasilkan tipe data tuple
# zip memiliki urutan element yaitu : (elArr1, elArr2, ..), ...
# berikut cara penggunaan zip 
items2 = ["m","a","m","a","h"]
for (item1, item2) in zip(items, items2) :  
    # maka element arr dari items akan dimasukan ke variabel item1 dan sebaliknya
    print("%s memiliki kembaran %s"%(item1, item2))


# Item Checking
# => menggunakan keyword in, keyword ini dapat digunakan untuk mencari apakah sebuah karakter ada di dalam variabel/ tipe data yang di di sandingkan.
check = "aku seorang bajak laut"
result = "i" in check # => False, karena huruf i tidak ada di dalam strng pada variabel check

# item checking pada dictionary
# => item checking juga dapat di gunakan di dalam dictionary, secara manual python akan mendefinisikan bahwa kita akan mencari sebuah huruf apakah ada di dalam key dari dictionary tersebut.
dic = {"mama" : 10, "papah" : "sayang"}
result1 = "sayang" in dic.values()  # bernilai True karena sama/identik dengan value dictionary nya
# INGAT!! jika kita mencari sebuah karakter ketika menggunakan dictionary, amka karakter harus sama persis dengan yang ada di value/key dalam dictionary tersebut, jika tidak maka nilai nya False
print(result1)



# Advance Looping 

# Mengisikan list menggunakan for in range v2.0
# syntax seadanya :
itemm = []
for i in range(1,11) :
    itemm.append(i)
print(itemm) # berisi el dari angka 1 - 10
# menggunakan syntax singkat nya :
itemm2 = [i for i in range(1,11)]
# cara membaca syntax : deklarasikan variabel bernama itemm2 yang isinya adalah list yang element nya adalah i, dengan i saya looping sebanyak range 1 sampai 11,, jadi isinya adalah angka 1 - 10 .
print(itemm2) # sama seperti variabel itemm)

# Keunggalan Penulisan ini ketimbang yang v1 adalah kita dapat mengutak atik valuenya dan menambahkan sebuah kondisi langsung didalam list nya.
# 1. mengutak atik nilai yang dihasilkan
itemm3 = [(item**2) for item in range(1,6)]  # => [1,4,9,16,25] | kuadrat
    # saya akan memasukan element angka 1-5 ke dalam list dengan setiap element kita kuadratkan..
# 2. menambahkan suatu kondisi di dalam list
    # kita dapat menambahkan kondisi dimana itu bisa mengatur apakah perulangan tersebut di jalankan atau tidak
    # letak kondisi adalah di depan angka dari range. 
    # jika kondisi terpenuhi maka, iterasi akan berjalan/el akan ditambahkan ke list, namun jika tidak lompati iterasi tersebut/ tidak dimasukan ke dalam list
itemm4 = [(item**2) for item in range(1,11) if item%2] 
    # jika item%2 bernilai True/1 maka masukan element ke dalam list dan kuadratkan,, maka list akan berisi element : [1, 9, 25, 49, 81]
    # el akan berisi kuadrat dari bilangan ganjil diantara 1 - 10
# 3. Menambahkan Kondisi Else didalam perulangan item list
    # Jika kita menggunakan else disini, maka syntax nya akan berbeda dengan ketika kita hanya menggunakan if
itemm5 = [item if not(item%2) else "Ganjil" for item in range (1,7)]
    # Jika item bernilai genap / %2 = 0, maka masukan item ke dalam list, namun jika tidak masukan string "Ganjil" ke dalam list .
    # Syntax ini mungkin terlihat lebih rumit ketimbang yang diatas, namun dengan menggunakan syntax diatas kita dapat menulis lebih singkat dan lebih sedikit dalam menggunakan memory, namun kita tidak diwajibkan menulis syntax seperti diatas, semua dikembalikan kepada programmer masing masing
print(itemm5)  # => ['Ganjil', 2, 'Ganjil', 4, 'Ganjil', 6]

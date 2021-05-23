# Map
# => adalah sebuah fungsi di python yang membutuhkan 2 parameter, yaitu sebuah fungsi yang menerima argument (parameter 1) dan sebuah variabel yang dapat diiterasi.
# Function Map menghasilkan kumpulan data dari nilai yang dikembalikan oleh fungsi pada parameter 1.
def modulus5(angka) :# fungsi yang mengembalikan string "habis" jika habis dibagi 5, jika tidak maka "Sisa"
    return "Habis" if not angka%5 else "Sisa"
hasil = list(map(modulus5, [1,2,3,4,5])) 
print(*hasil) # akan menghasilkan string "Sisa" sebanyak 4 kali(1,2,3,4) dan "Habis" sebanyak 1 kali(5)
# cara kerja fungsi map:
    # a. map akan memanggil fungsi pada perameter 1 dengan mengirimkan argument parameter 2 dengan index 0 
    # b. fungsi akan memproses dan mengembalikan nilai
    # c. fungsi map akan menerima dan menyimpan nilai yang dikembalikan oleh fungsi pada parameter 1
    # d. hal diatas akan diulangi terus menerus sampai pada index terakhir parameter ke 2 fungsi map
    # e. fungsi map akan mengembalikan object map, cara mengeluarkan nya adalah dengan dibungkus dengan fungsi yang menyimpan banyak nilai (list(), tuple(), dll)


# Filter
def bisadibagi6(angka) :
    return not angka%10 
hasil = list(filter(bisadibagi6, [7,12,56,72,44,77,90,100])) # fungsi pada filter wajib mengembalikan nilai boolean
print(hasil) # akan menghasilkan list dengan value 90 dan 100
# Cara kerja fungsi filter :
    # a. filter akan memanggil fungsi pada perameter 1 dengan mengirimkan argument parameter 2 dengan index 0
    # b. fungsi akan memproses dan mengembalikan nilai yang bernilai boolean
    # c. fungsi filter akan menerima dan menyimpan nilai yang value nya adalah True, jika tidak maka nilai tersebut akan dibuang
    # d. hal diatas akan diulangi terus menerus sampai pada index terakhir parameter ke 2 fungsi filter
    # e. fungsi filter akan mengembalikan object filter, cara mengeluarkan nya adalah dengan dibungkus dengan fungsi yang menyimpan banyak nilai (list(), tuple(), dll)


# Lambda Expression
# => adalah sebuah cara membuat sebuah fungsi namun dengan syntax yang lebih singkat. Membuat fungsi dengan lambda expression biasanya digunakan ketika kita ingin menggunakan fungsi hanya untuk satu hal saja.
# Lambda expression sama seperti arrow function pada javascript. 
# Cara penulisan lambda expression :
# membuat fungsi kali 10 :
def kali(angka) :
    return angka*10
# hmm, oke normal
kali2point0 = lambda angka : angka*10
# cara baca : buatlah fungsi yang menerima satu paramter dan assign ke variabel kali2point0
# jadi secara tidak langsung variabel kali2point0 adalah sebuah fungsi, 

# wow, satu baris saja dan lebih singkat!!

# Hubungan dan Cara penggunaan lambda expression pada fungsi map dan filter
#  => jika kita ingin menggunakan fungsi map dan filter, kita harus mengirim argument berupa sebuah fungsi, lalu kita mendefinisikan sebuah fungsi yang hanya dipakai satu kali yaitu oleh fungsi map / filter,
# cara diatas adalah sebuah cara yang salah dan membuat kode anda terlihat newbie dan kotor(tidak bersih)
# disinilah lambda expression digunakan, dengan menggunakan lambda expression,, kita hanya perlu mendesinikan lambda expression langsung di dalam fungsi map tersebut.
# Sangat Efisien bukan??
angka = [65,23,12,76,90,33,55]
bagi10 = list(map(lambda x : x/10, angka)) # membagi setiap element dari angka dengan 10, 
print(bagi10) 

stringku = "Aku suka makan sate"
huruf_besar = list(filter(lambda x : x == x.upper() and x != ' ', stringku)) # hanya menerima huruf besar
print(huruf_besar) 
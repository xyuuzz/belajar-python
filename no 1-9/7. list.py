# List Pada Python 
#  => adalah kumpulan dari data yang dituliskan didalam tanda kurung siku dan setiap data tersebut dipisahkan dengan tanda koma.
#  => List dapat berisi lebih dari 1 tipe data yang berbeda
contoh_list = [12, 44.5, "halo", True]


# Me-looping isi list menggunakan fungsi len() dan for loop
# => method len berfungsi untuk menghitung panjang dari list, dimulai dari angka 1
for i in range(len(contoh_list)) :
    print(contoh_list[i]) # maka setiap element akan diprint, dari belakang ke depan

# Mengganti isi dari element list
contoh_list[1] = "mama" # akan mengganti isi list yang memiliki indeks 1
print(contoh_list) 


# Menambah element ke dalam list menggunakan method apped()
# => adalah method yang dapat menambahkan element ke dalam list di urutan paling belakang. kekurangan method append adalah hanya bisa menambah satu element saja.
contoh_list.append(22.1) # menambahkan float 22.1 ke element terakhir list
print(contoh_list)
# Jika ingin menambahkan banyak element sekaligus ke dalam list, maka harus membuat list sendiri lalu kita concat(tambahkan) menggunakan tanda + 
tambah_list = ["ini", "tambahan", "listnya"]
contoh_list = contoh_list + tambah_list # element list dari variabel tambah_list akan ditambahkan
print(contoh_list)
# Namun jika kita menambahkan tambah_list menggunakan method append(), maka yang terjadi adalah method append() menambahkan list nya, bukan isinya. Jadi akan terbentuk sebuah list didalam list. Ini dinamakan Nested List


# Mengambil serta menghapus element List menggunakan method pop()
# => Jika kita mendefinisikan method pop tanpa memberi argument indeks berapa yang akan diambil dan dihapus, maka secara otomatis method pop akan mengambil dan menghapus indeks terakhir. Namun jika kita mengirimkan argument indeks berapa yang akan dihapus, maka element itulah yang akan dihapus.
hapus_list = contoh_list.pop() # maka element terakhir dari list contoh_list akan dihapus dan menjadikanya value dari variabel hapus_list
hapus_indeks_3 = contoh_list.pop(3) # maka element yang akan dihapus dan dijadikan value dari variabel hapus_indeks_3 adalah element dengan indeks ke 3 dari list contoh_list


# Mengurutkan Element List menggunakan method sort()
# => method sort mengurutkan element dengan ketentuan dari yang paling kecil sampai ke paling besar(ini berlaku pada tipe data numeric ), namun method sort bisa juga digunakan pada string, ketentuanya tetap sama yaitu dari terkecil hingga terbesar, namun jika yang diurutkanya adalah string,, maka cara mengurutkan nya adalah sesuai abjad
# perlu diigat bahwa method sort tidak menghasilkan apa apa, tuganya hanya mengurutkan list !!
list_numeric_sort = [2,3,4,1,6,11,8,7]
list_string_sort = ["c", "a", "z", "g", "d", "i"]
list_numeric_sort.sort() # maka akan langsung diurutkan dari terkecil hingga terbesar
list_string_sort.sort() # mengurutkan string sesuai abjad nya

# Menggunakan method sort untuk mengurutkan string kalimat dan tipe data float
kalimat_sort = "Hari ini cuacanya bagus sekali ya mas Andi"
float_sort = [4.6, 1.4, 6.2, 77.2, 66.4, 100.255]
kalimat_sort = kalimat_sort.split() # mengubah string ke dalam array
kalimat_sort.sort() 
print(kalimat_sort)
# kesimpulan menggunakan method sort ke string kalimat : 
    # a. jika kata diawali dengan tanda baca(,.!? dll), maka tempatkan di paling depan,
    # b. setelah itu jika kata diawali dengan angka, maka urutkan sesuai angkanya (kecil ke besar)
    # c. lalu mengurutkan menurut huruf kapital nya,
    # d. terakhir, urutkan dengan urutan abjadnya

# Perulangan jika ada list di dalam list
nested_list = [1,2,3,[4,5,6],7,8,[9,10]]
for i in range (len(nested_list)) :
    if(type(nested_list[i]) == list) : # jika element list nya adalah list, maka true
        for isi_nested_list in nested_list[i] : # for in digunakan untuk melooping tipe data yang itterable
            print(isi_nested_list)
    else :
        print(nested_list[i])

# Tuples
    # => Tipe data tuple (bahasa jamaknya tuples) adalah tipe data yang dapat menyimpan lebih dari 1 jenis tipe data (sama seperti list & dictionary) namun tuple memiliki sifat yang immutable yaitu tidak dapat diubah.
    # Cara mendeklarasikan tuple ada 2, yaitu :
        # 1. dideklarasikan di dalam tanda () dan dipisahkan dengan tanda koma
contoh_tuple1 = ("ini", "adalah", "tuple")
print(type(contoh_tuple1)) # adalah tuple
        # 2. dideklarasikan tanpa tanda () namun diberi tanda koma pada setiap element nya
contoh_tuple2 = "ini", "tuple", 2
print(type(contoh_tuple2)) # adalah tuple

# * DIREKOMENDASIKAN SAAT MENDEKLARASIKAN TUPLE WAJIB MENGGUNAKAN TANDA () AGAR KONSISTEN DAN MUDAH UNTUK DIBACA


# Method Yang Ada di Tipe Data Tuple
    # => Tipe data tuple hanya memiliki 2 method saja, yaitu count untuk menghitung jumlah element dan index untuk mencari index dari element.
    # 1. count
print(contoh_tuple1.count("ini")) 
    # method count membutuhkan 1 parameter yang isinya adalah untuk mencari element pada list yang sama dengan yang diterima parameter
print(contoh_tuple1.index("tuple")) 
    # sama seperti method count, method index juga memerlukan 1 parameter untuk mencari index element yang diterima oleh parameter



# Sets
    # Tipe dat set (sets dalam bahasa jamak) adalah tipe data yang memiliki value yang unik(tidak dapat memiliki element duplikat) dan acak.
    # Tipe data set sama seperti dictionary namun tidak memiliki key, hanya value saja.
    # berikut adalah adalah 2 cara pendeklarasian tipe data set :
    # 1. dibungkus dengan tanda {}
set1 = {"ini", "adalah", "set", 1}
    # 2. Dengan menggunakan set() untuk membuat set kosong, lalu menambahkan element pada set menggunakan method add()
set2 = set() # membuat set kosong
set2.add("ini")
set2.add("adalah")
set2.add("set")
set2.add(2)
print(set2)
# INGAT!! URUTAN PADA TIPE DATA SET SELALU BERUBAH UBAH (ACAK)

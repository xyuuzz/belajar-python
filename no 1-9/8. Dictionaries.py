# Dictionaries atau tipe data dictionary adalah sebuah tipe data yang sifatnya hampir sama dengan list, namun yang membedakanya adalah cara mengaksesnya dan penulisanya.
    # a. Cara mengakses : dictionary menggunakan key untuk mengakses sebuah value didalamnya, setiap key hanya dapat memiliki satu value. Key berada disebelah kanan dan value berada di sebelah kiri, dengan dipisahkan dengan tanda titik dua (:) . key harus dibungkus dengan tanda petik ("" / '')
    # b. Cara penulisan tipe data dictionary adalah dengan dibungkus oleh curly bracket {}
# Contoh penulisan dictionary adalah sebagai berikut. 
contoh_dic = {"key1": "value1", "key2": 2}
# cara mengambil value dari dictionary :
contoh_dic_1 = contoh_dic["key1"]# maka hasilnya adalah "value1",sesuai dengan value dari kunci /key : key1


# contoh dictionary lagi
harga_makanan = {
    "sate" : 17,
    "ayam" : 15,
    "gule" : 21,
    "tengkleng" : 20
}
print("harga makanan sate adalah {a} ribu".format(a=harga_makanan["sate"])) # mengakses dictionary dengan key "sate"


# Mengakses Nested Dictionary 
# => mengakses nested dictionary caranya sama seperti mengakses nested list, namun pada dictionary menggunakan key. sudah itu saja perbedaan antara dictionary dan list
nested_dict = {
    "static" : "halo ane milik kunci 1",
    "nested" : {
        "nested_1" : "halo ane milih kunci nested 1",
        "nested_2" : "halo ane milih kunci nested 2",
        "nested_3" : "halo ane milih kunci nested 3"
    }
}
print("ini adalah value dari kunci nested 2 : {a} ... \ndan ini adalah value dari static key : {b}"
      .format(a=nested_dict["nested"]["nested_2"], b=nested_dict["static"])
)


# Mengganti value dari dictionary
ganti_isi = {
    "diganti" : 22,
    "tetap" : "ini tetap"
} 
ganti_isi["diganti"] = "ITEM INI SUDAH DIGANTI"
print(ganti_isi["diganti"]) # value nya bukan lagi 22, namun berbeda karena sudah diganti/ditimpa 


# Contoh method di dictionary
method_dict = {
    "sayang" : "apa??",
    "gapapa" : "mengcape"
}
    # 1. keys()
    # => method keys akan mengembalikan key yang ada di dalam dictionary 
method_dict_keys = method_dict.keys()

    # 2. values()
    # => method values akan mengembalikan value yang dimiliki oleh key di dalam Dictionary
method_dict_values = method_dict.values()

    # 3. items()
    # => adalah method yang mengembalikan sebuah nested tuple yang disetiap tuple nya berisi key dan value dari sebuah dictionary
method_dict_items = method_dict.items()

# Method keys() dan values() menghasilkan sebuah array yang dapat di looping menggunakan for in, namun tidak dapat diakses menggunakan indeks


# Menggunakan perulangan untuk menge-print dictionary
loop_dict = {
    "ke1" : "ini ke 1",
    "ke2" : "ini ke 2",
    "ke3" : "ini ke 3",
    "ke4" : "ini ke 4",
    "ke5" : "ini ke 5"
}

    # => dictionary merupakan tipe data yang memiliki sifat itterable, sehingga kita dapat menggunakan for in, namun for in hanya akan mengembalikan key nya tidack dengan value nya.
for key in loop_dict :
    print(loop_dict[key])
    
    # => mengakses dictionary menggunakan method items() 
for key,value in loop_dict.items() : 
    # kenapa ada 2 variabel diatas? karena tipe data tuple memiliki sifat yang dapat dipecah..
    print("%s : %s" % (key, value) ) # cara singkat penulisan format


# Menghapus pasangan key dan value dari dictionary
    # => dictionary juga dapat menggunakan method pop seperti list, yang fungsinya untuk menghapus element, namun berbeda dengan list, pada dictionary argument yang dikirimkan adalah nama key nya.
dic = { # buat dic
    "anjay" : 11
}
dic["mantab"] = 12 # buat pasangan key value baru
dic["anjay"] = 1000 # update value 
dic.pop("anjay") # hapus pasangan key dan value dengan indeks "anjay"



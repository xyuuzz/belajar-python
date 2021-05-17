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
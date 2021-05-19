# Fakta Fakta Yang ada pada Tipe Data Strings

    # 1. string tidak imutable
    #   => walaupun kita dapat mengakses string menggunakan indeks, namun kita tidak dapat mengubah value dari string menggunakan indeks.
    # 2. Operator Perkalian bereaksi terhadap string
    #   => walaupun bukan tipe data numeric(int, float), namun string dapat menjalankan operasi perkalian. Operasi ini akan menggandakan string tersebut menjadi jumlah yang diinginkan.
string = "python hebat sekali\n"
string3kali  = string*3 # isi dari var string akan dikali 3 kali, atau lebih tepatnya isinya akan disalin sebanyak 2 kali.
print(string3kali) 



# Contoh Method / Function Built In pada Python
    # => Cara penggunaan method pada python adalah letakan titik dibelakang variabel/tipe data lalu dibelakang titik tulis nama method tersebut. Ingat pakai () agar method dieksekusi.
    # 1. upper()
    #   => adalah sebuah method untuk mengubah seluruh string menjadi huruf besar(upper case)
contoh_upper = "ini akan menjadi upper case"
contoh_upper.upper() # maka variabel contoh_upper akan menjadi besar semua 
    # 2. split()
        # => adalah sebuah method yang fungsinya untuk mengubah tipe data string menjadi list. List memiliki 2 parameter opsional. Yaitu Delimiter dan max split.
        # jika kita tidak mengirimkan argument maka method split akan memecah string dan menjadikanya list setiap bertemu dengan spasi.
        # Namun jika diberi argument(1 argument), maka string akan dipecah setiap bertemu argument tersebut, maka split akan menganggapnya itu sebagai delimiter nya.
contoh_split = "ubah menjadi list"
split_spasi = contoh_split.split() # akan menghasilkan list yang berisi ['ubah', "menjadi", "list"]
split_bertemu_a = contoh_split.split("a") # ['ub', 'h menj', 'di list'] , karena setiap bertemu huruf a, maka string tersebut akan dipecah.


# Format Strings
    # => adalah sebuah fitur pada string dimana kita dapat menggunakan variabel di dalam string, dengan cara menggunakan method format yang diletakan dibelakang string tersebut.
contoh_format = "Maulana Yusuf"
format_1 = "{} bisa website".format(contoh_format) # maka hasilnya adalah = "Maulana Yusuf bisa website"
    # variabel dapat digunakan di dalam string karena diselipkan oleh method format
format_2 = "{1} Anjay lanjay bang {0}".format("manteb", "uga") # hasilnya = uga Anjay lanjay bang manteb
    # jika kita memberi angka pada curly bracket string, maka bracket tersebut akan mengakses urutan di method format sesuai nomor nya(ingat, dimulai dari 0 yaa)
format_3 = "ini apaan yak? {a} boss {b}?".format(a="makanan loh ya", b="kamu kenapa pulang marah?") 
    # Anggap saja huruf pada curly bracket didalam tanda petik adalah variabel yang nanti akan dideklarasikan di dalam method format
    # dan nanti nya curly bracket tersebut akan berisi variabel dengan nama yang sama dengan yang ada di dalam method format
format_4 = "ini adalah format yang {a:8.5}".format(a="abadiii")  # isi curly bracket dengan variabel a, dengan jarak diberi jarak 8 spasi dan element nya maksimal adalah 5 === 6 huruf, karena 0-5
    # dengan cara penulisan diatas maka method format dapat melakukan hal berikut :
        # - memberi nama variabel tertentu untuk menentukan valuenya
        # - memberi jarak(tab) sesuai parameter ke dua (nama_var:jml_tab.jml_print)
        # - mengatur sampai index berapa yang akan ditampilkan
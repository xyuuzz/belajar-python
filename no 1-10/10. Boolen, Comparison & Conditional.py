# Boolean
    # Tipe data bool (boolean) adalah tipe data yang hanya memiliki 2 value yaitu True (dengan T besar) dan False (dengan F besar). Boolean ini juga dapat disamakan dengan angka 1 = True dan 0 = False.



# Comparison
    # Comparison atau Perbandingan adalah sebuah operator yang berfungsi untuk membandingkan antara 2 buah object yang ada di sebelah kiri dan kanan nya.
    # Operator Comparison menghasilkan tipe data bool, yaitu True (jika benar) dan False (jika salah)
    # Berikut adalah operator Comparison
    # ==    -> sama dengan 
print(3 == 3) 
# bernilai True
    # !=    -> tidak sama dengan
print("a" != "b")
# bernilai True
    # >     -> lebih besar
print(3 > 5) 
# bernilai False
    # <     -> lebih kecil
print(5 < 1) 
# berniali False
    # >=    -> lebih besar sama dengan
print(5 >= 5)
# bernilai True
    # <=    -> lebih kecil sama dengan
print(6 <= 5)
#bernilai False

    # Comparison Operators Berantai, ada 3 buah/argument yaitu :
    # and   -> jika salah satu kondisi bernilai False, maka False
print(6 == 6 and 7 > 9) 
# False 
    # or    -> jika salah satu kondisi bernilai True, maka True
print(9 == "sembilan" or 0 < 10)
    # not   -> berfungsi untuk memutar balikan fakta, jika True maka False, jika False maka True
print(not(5 == 5))



# Conditional
    # Conditional diartikan sebagai pengontrol alur program, bagaimana program itu berjalan.
    # jika kondisinya a maka jalankan a, jika kondisi b maka jalankan b. Semua itu menggunakan konsep Conditional.
    # Suatu kondisi akan terpenuhi apabila kondisi yang dimasukan menghasilkan nilai True, dan sebaliknya. 
    # Ada beberapa Conditional pada python, berikut adalah contoh + cara penulisanya :
        # program dengan single Condition
if ("a" == "b") : # jika kondisi ini benar
    print("benar") # maka jalankan kode dibawah if, yang berjarak 1 indentasi

    # Menurut Contoh diatas, kita tidak bisa membuat kode yang dijalankan ketika kondisi dari if tidak terpenuhi atau menghasilkan nilai False.
    # Disinilah kita membutuhkan keyword else. kode dibawah else akan dijalankan ketika kondisi dari if tidak terpenuhi.
if ("aku" == "jelek") : # kondisi ini tidak terpenuhi
    print("benar") # kode ini tidak dijalankan
else : # masuk ke blok else
    print("salah") # kode ini dijalankan karena kondisi dari if tidak terpenuhi
    
    # Sampai sini kita sudah belajar tentang if else, yaitu jika a maka jalankan a, namun jika a False jalankan b..
    # Namun bagaimana kalau kita butuh lebih dari 2 kondisi??
    # Disini kita membutuhkan keyword *elif*
    # elif berfungsi sama seperti if, namun elif akan dicek kondisinya setelah kondisi if bernilai False.
tinggi = 250
if(tinggi < 160) : # bernilai False, lompati
    print("Anda memiliki tinggi tubuh yang pendek")
elif(160 < tinggi < 180) : # bernilai True, masuk ke blok statement nya
    print("Anda memiliki tinggi tubuh yang ideal di masa sekarang") # jalankan
else : # karena ada salah satu kondisi yang bernilai True, maka blok else tidak akan dicek/dijalankan
    print("Tinggi anda diatas rata rata manusia")
    
# INGAT!! JIKA SUDAH ADA SATU KONDISI YANG TERPENUHI, MAKA KONDISI DIBAWAHNYA TIDAK AKAN DI CEK MAUPUN DIJALANKAN



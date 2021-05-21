# Fungsi
# => Adalah sebuah kumpulan kode dalam satu blok {} yang berfungsi untuk menjalankan perintah.
# Kita tidak perlu mengulangi kode yang sama, cukup masukan ke dalam sebuah fungsi, lalu jika kita ingin menggunakanya cukup panggil fungsi yang berisi perintah yang ingin kita jalankan.

# Docstring => sebuah komentar untuk pembaca, biasanya digunakan untuk mendeskripsikan fungsi di program kita
# Keyword return => untuk mengembalikan satu nilai ke si pemanggil/tempat fungsi dipanggil. Jika sebuah fungsi tidak memiliki nilai return, maka jika dipanggil, fungsi akan mengembalikan nilai None (tidak ada)

# Cara mendeklrasikan fungsi :
def ini_fungsi() :
    print("Hello World")
ini_fungsi() 
# mencetak hello world

# Parameter
#  => adalah sebuah variabel yang dideklarasikan di dalam tanda kurung di depan nama fungsi () . Parameter berguna untuk menerima data yang dikirimkan saat fungsi dipanggil. Data yang dikirimkan disebut argument, sedangkan yang menerima data adalah parameter.
# def nama_fungsi (var_parameter1, var_parameter2)
# Tiap parameter dipisahkan dengan tanda koma
# Parameter hanya bisa digunakan di dalam fungsi itu saja, tidak bisa diakses diluar fungsi.

def terima_1(satu) :
    print(satu)
terima_1("haloooo") # mencetak kata sesuai nilai argument

def perkalian(a,b) :
    return a*b
print(perkalian(10, 10)) # mencetak hasil perkalian dari 2 bilangan yang dikirim

def unlimited(*angka) :
    return angka
print(unlimited(1,2,3))

# Parameter juga dapat memiliki nilai default, nilai default ini berguna ketika kita memanggil fungsi namun tidak mengirimkan argument, maka nilai default akan digunakan sebagai value parameter.
def default (deff="ini default") :
    print(deff)
default() # karena tidak mengirimkan argument, maka menggunakan default value


# tugas membuat fungsi
# buatlah fungsi yang menerima parameter kalimat, jika kalimat tersebut mengandung kata 'python' maka kembalikan nilai True, dan sebaliknya.
def cek_kata(kalimat) :
    # return True if kalimat.lower().find("python") != -1 else False 
    # ubah kalimat menjadi huruf kecil, lalu cara kata python, jika ada maka akan menampilkan indeksnya, jika tidak maka akan mengembalikan nilai -1.
    # jika nilai nya != -1 , maka return True , jika tidak maka return False
    
    # atau kita juga dapat menggunakan syntax berikut : 
    return "python" in kalimat.lower() 
    # jika ada kata python di var kalimat (huruf kecil semua) maka kembalikan True jika tidak kembalikan False
# kalimat = input("Masukan kalimat yang anda pikirkan : ")
# print(cek_kata(kalimat))


# Args
# => adalah sebuah operator yang dapat menangkap lebih dari satu argument, maka dari itu disebut args = arguments . Operator yang digunakan adalah tanda * didepan var parameter nya.
# Argument yang ditangkap oleh args nanti akan berbentuk sebuah tuple.
# contoh penggunaan
def penjumlahan(*angka) :
    return sum((angka)) # method sum berguna untuk menjumlahkan semua element. 
    # kenapa tanda () doble? karena angka yang berbentuk tuple sebenarnya berbentuk v1,v2,v3,v4 maka dari itu perlu dibungkus oleh tanda ()
print(penjumlahan(1,2,3,4,5,6,7))


# Kwargs
# => Kwargs sama seperti Args, perbedaanya adalah kwargs menerima argument yang berupa dictionary. Jadi harus ada pasangan antara key dan value. Operator Kwargs dilambangkan dengan tanda * sebanyak 2 kali atau ** lalu diikuti dengan nama variabel.
def print_dic(**dict) :
    print(*dict.keys(), *dict.values())

print_dic(nama = "Maulana", sapa = "Halo")
# menampilkan pasangan key dan value dari dictionary yang dikirimkan secara berpasangan, menggunakan spread operator.

# Menggabungkan *args dan **kwargs
# jika kita menggabungkan kedua operator diatas, maka urutan penggunaan nya disesuaikan oleh cara penulisan parameter nya.
def gabung(*args, **kwargs) :
    # python akan secara otomatis mengidentifikasi bahwa argument pertama dan selanjutnya berbentuk biasa adalah args sedangkan argument selanjutnya yang memiliki key dan value adalah kwargs
    print("%a adalah args\n%a adalah kwargs"%(args, kwargs))

gabung(1,2,3, sapa="hai")  
# sapa hai masuk ke kwaqgs, argument sebelumnya masuk ke args


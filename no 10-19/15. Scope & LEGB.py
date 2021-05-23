# Scope 
# => Scope / scope variabel adalah ruang lingkup variabel dapat diakses.
# Ada empat ruang lingkup / scope variabel di dalam python, yaitu LEGB :
    # 1. L => Local 
        # => variabel bersifat local, biasanya berada di dalam fungsi(def/lambda)
    # 2. E => Enclusion Local Variabel
        # => adalah variabel yang dideklarasikan di dalam fungsi yang fungsi tersebut ada di dalam fungsi / nested fungsi
    # 3. G => Global
        # => dapat diakses dimanapun, bebas, dideklarasikan di tahap awal
    # 4. Built in
        # => sebuah variabel bawaan dari python, contohnya : list, tuple, str, upper dll

# jika scope variabel sudah ditemukan, python akan langsung memakai variabel tersebut, tanpa melihat ke bawah lagi.

# Perlu diingat bahwa variabel local scope tidak dapat diakses diluar fungsi nya, namun variabel global scope dapat diakses di dalam fungsi Dan walaupun nama variabel sama tapi ruang lingkup nya beda maka 2 variabel tersebut merupakan variabel yang berbeda.

var_global = "INI VARIABEL GLOBAL" # dapat diakses dimanapun

def buat_fungsi() :
    lanjay = "mantab" # Enclusion local variabel untuk fungsi local2x, local variabel untuk fungsi buat_fungsi
    def local2x() :
        var_local = " lanjay" # var local untuk fungsi local2x
        var_local += lanjay # fungsi ini dapat mengakses variabel local induknya
        return var_local
    # namun fungsi induk tidak dapat mengakses variabel fungsi child/anak nya
    var_local = local2x() # local variabel
    return var_local


# Mengubah Variabel Global di dalam function
buat_global = "GLOBAL BOS"
def ganti_var() :
    global buat_global
    
    buat_global = "AKU GANTI YA MAK"
    return buat_global

print(buat_global) # variabel masih tetap
print(ganti_var()) # panggil fungsi pengubah variabel
print(buat_global) # value variabel berubah setelah fungsi dipanggil

# Diatas adalah salah satu cara untuk mengubah global variabel di dalam fungsi, namun cara ini sangat tidak direkomendasikan karena mengubah langsung value dari global variabel.
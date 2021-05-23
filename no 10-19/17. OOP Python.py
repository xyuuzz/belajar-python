'''
Ada 2 cara penulisan program yang umum digunakan, yaitu :
    1. Prosedural Programming : yaitu program yang dijalankan dari atas ke bawah secara urut
    2. Object Oriented Programming : yaitu program yang dijalankan dengan menggunakan sudut pandang bahwa semua yang kita tulis adalah object

FYI, semua tipe data yang ada di python adalah berbentuk object.
karena berbentuk object kita dapat menggunakan method/fungsi dan attribute dari tipe data(obejct) tersebut menggunakan tipedata.nama_method() / tipedata.attribute

Dengan Belajar Object Oriented Programming, kita akan dapat membuat object kita sendiri dan menggunakanya sesuka hati dan sesuai aturan yang ada di python. Dan dari sini kita akan mulai untuk terbiasa berpikir bahwa semua yang kita tulis di program python adalah sebuah object

Class
=> adalah sebuah blueprint(template) dari object. 
Misalnya, ketika kita ingin membuat rumah, maka kita perlu membuat rancangan pembuatan rumah. Nah rancangan ini jika kita ibaratkan di dalam OOP adalah sebuah class. 
Yang nantinya class ini akan di inisiasi(direalisasi) dan jadilah sebuah object dari class tersebut.
'''

# Cara Membuat Class / Template dari Object
class Hero :
    pass #pass menandakan bahwa class ini tidak menjalankan apa apa


hero1 = Hero() # membuat object / meng-inisiasi dari class / template Hero
hero1.name = "Maulana" #hero1 memiliki attribute name
hero1.healt = 1500 #hero1 memiliki attribute healt
print(hero1.name) #mencetak attribute name dari object hero1

hero2 = Hero() 
hero2.name = "Bersama"
hero2.health = 9000
print(f"Hero2 memiliki nyawa : {hero2.health}") # mencetak attribute health dari object hero2

'''
SEBUAH CLASS DAPAT DI INSTANSIASI BERULANG KALI,, SAK PUASMUU
'''
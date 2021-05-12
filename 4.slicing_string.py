#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:09:16 2021

@author: xyuuz
"""


# Slicing adalah sebuah metode memecah value dari tipe data yang bersifat itterable
# cara memecahnya pun mudah, yaitu dengan menggunakan rumus :
# [i.awal:i.akhir:jarak]
# ingat, indeks awal dimulai dari 0

# contoh slicing pada string
slicing_string = "Halo namaku Maulana"
print(slicing_string[0:2])
# kita mengakses string dari indeks ke 0 sampai indeks ke 2
# namun, perlu diingat bahwa, indeks akhir tidak ditampilkan
# jadi jika kita slicing sebuah tipe data maka yang akan keluar adalah :
# indeks awal - indeks akhir - 1

# la terus kalau kita mau mengakses value dari indeks terakhir bagaimana kak?
# kita tinggal mengosongkan argument dari i.akhir nya saja
# maka python akan mengetahui bahwa kita akan mengakses tipe data tersebut sampai indeks terakhir
print(slicing_string[2:])
# artinya kita akan mengakses dari indeks ke 2 sampai indeks terakhir

# menggunakan jarak
print(slicing_string[:7:2])
# kita akan mengakses dari indeks ke 0 sampai indeks ke 7, dan tampilkan valuenya setiap 2 indeks
# jarak digunakan ketika kita ingin melompati sebuah indeks dengan aturan tertentu

# membalikan urutan pada tipe data 
# Kita dapat membalikan urutan dengan cara memberi argument jarak dengan value -1
# nanti python akan menganggap bahwa kita akan mulai dari indeks -1 
# jangan lupa kosongkan argument i.awal dan i.akhir nya
print(slicing_string[::-1]) # analuaM ukaman olaH




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:05:53 2021

@author: xyuuz
"""


# Tipe data yang ada di Python

# 1. Strings -> str
# Strings adalah tipe data yang berupa tulisan, huruf. 
# Cara penulisanya adalah diapit dengan tanda petik 1 atau petik 2
strings = "Ini adalah tipe data strings"
print(strings)

# str adalah tipe data yang itterable (dapat di looping), yang artinya str ini memiliki index disetiap hurufnya
# index pada tipe data str tidak berbeda dengan tipe data list 
# s  t  r  i  n  g
# 0  1  2  3  4  5   => ini disebut indeks maju
# 0 -5 -4 -3 -2 -1   => ini disebut indeks mundur

# index mundur biasanya digunakan ketika kita dihadapkan sebuah keadaan dimana kita tidak tau seberapa panjang string yang kita ingin olah
# nah, cara nya tinggal akses string itu dengan index -1 untuk mengetahui huruf belakangnya
print(strings[-1])      # s -> karena s adalah huruf yang paling akhir 


# 2. Integers -< int
# Integers adalah tipe data yang berupa bilangan bulat
integers = 100
print(integers)


# 3. Floats -> float
# Floats adalah tipe data yang berupa bilangan angka desimal,
# Angka dibelakang nol, dipisahkan dengan tanda titik (.)
floats = 12.75
print(floats)


# 4. List -> list 
# List adalah tipe data yang dapat menyimpan banyak data sekaligus
# Atau kumpulan dari beberapa object
lists = ["string", 22, 45.5, True, ["stringke2", 2]]
print(lists)


# 5.Dictionaries -> dict
# Dictionaries adalah kumpulan dari berbagai tipe data yang berpasangan
# maksud berpasangan disini adalah mempunyai kunci dan value : {"kunci1" : "value1"}
# setiap pasangan dipisahkan dengan tanda koma
dictionaries = {
    "item1" : "value1",
    "item2" : 22,
    "item3" : 33.3,
    "item4" : False
}
print(dictionaries)


# 6. Tuples -> tup
# Kumpulan dari beberapa object yang tidak bisa diubah value nya
tuples = ("string", 11, 12.5, True, ["sting2", 22])
print(tuples)


# 7. Sets -> set
# Sets adalah kumpulan object tanpa urutan
# sets ini sama seperti dictionaries, namun sets tidak mempunyai kunci
sets = {"apel", 22, "pisang", True}
print(sets)


# 8, Boolean -> bool
# Boolean hanya memiliki 2 value, yaitu True dan False, bool juga melambangkan angka 1 dan 0
boolean = True
print(boolean)



# untuk mengetahui tipe data pada variabel, kita dapat menggunakan fungsi bawaan python
# yaitu type(variabel)
print(type(boolean))    # hasilnya adalah bool
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:26:16 2021

@author: xyuuz
"""


list_slicing = [1,2,3,4,5,6,7,8,9,10]

# aturan slicing pada list sama seperti slicing pada string, jadi tidak ada yang perlu dikhawatirkan
# anggap saja list dan string itu tipe data yang sama, namun hanya beda cara penggunaan

# mengakses list dengan index
print(list_slicing[1]) # 2


# slicing list
print(list_slicing[::2])
# artinya kita mengakses semua value, namun value yang dikeluarkan hanya setiap 2
# jadi => 1,3,5,7,9
#        0 - 2 - 4 - 6 - 8

# Jangan lupa, slicing pada list pastinya akan menghasilkan tipe data list juga, bukan string/int

print(list_slicing[:]) # mengakses semua value nya, sama seperti yang dilakukan pada slicing string


# print(list_slicing[::-1]) # membalik value nya, 

kebalikan_list_slicing = list_slicing[::-1] # mempunyai value list yang value list tersebut adalah kebalikan dari value list list_slicing
print(kebalikan_list_slicing)
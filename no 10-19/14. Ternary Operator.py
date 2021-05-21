# Ternary operator adalah operator yang fungsinya sama seperti if else namun dengan syntax yang lebih singkat.
# if else biasa
x, y = 5, 6
if x>y:
   print("x")
else:
   print("y")
# => y

# Jika menggunakan ternary operator :
print("x" if x>y else "y") # => y
# cara baca : print "x" jika x > y , jika tidak print "y"
# INGAT!! Ternary operator harus memiliki 2 value yaitu value if dan else
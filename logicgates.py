# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Sebagai Pembalik Keadaan, seperti "True" Menjadi "False", dan sebaliknya
'''
print('================ NOT ================')
t = True
s = False
# menggunakan Operator "not" dan diletakkan antara 2 variabel 
notTrue = not t 
notFalse = not s

print('|' , t, ' | not = ', '|',  notTrue, '|')
print('|' , s, '| not = ', '|', notFalse,' |')
print('\n')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
jika kedua input bernilai "True & False" atau sebaliknya maka hasilnya akan "False" , namun jika kedua input sama tetapi menggunkan "False" maka hasilnya akan "False". Namun Apabila kedua input bernilai "True" maka hasilnya adalah "True"
'''
print('================ AND ==============') 
t = True
s = False
# menggunakan Operator "and" dan diletakkan antara 2 variabel
and1 =  s and s
and2 =  s and t
and3 =  t and s
and4 =  t and t
print('|', s,'|','and','|', s,'|','=','|', and1, '|')
print('|', s,'|','and','|', t,' |','=','|', and2, '|')
print('|', t,' |','and','|', s,'|','=','|', and3, '|')
print('|', t,' |','and','|', t,' |','=','|', and4, ' |')
print('\n')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
NAND adalah kebalikan dari AND jika keduanya bernilai "True" maka hasilnya akan "False", sdangkan yang lainnya akan benilai "True"
'''
print('================ NAND ==============') 
t = True
s = False
nand1 =  s and s
nand2 =  s and t
nand3 =  t and s
nand4 =  t and t
# Tinggal Menambahkan operasi "not" pada Variabel "nand1"
print('|', s,'|','nand','|', s,'|','=','|', not nand1, ' |')
print('|', s,'|','nand','|', t,' |','=','|', not nand2, ' |')
print('|', t,' |','nand','|', s,'|','=','|', not nand3, ' |')
print('|', t,' |','nand','|', t,' |','=','|', not nand4, '|')
print('\n')



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Hasilnya akan "False" jika keduanya bernilai "False" 
'''
print('================ OR ==============') 
t = True
s = False
# menggunakan Operator "or" dan diletakkan antara 2 variabel
or1 =  s or s
or2 =  s or t
or3 =  t or s
or4 =  t or t
print('|', s, '|','or','|', s, '|','=', '|', or1, '|')
print('|', s, '|','or','|', t, ' |','=', '|', or2, ' |')
print('|', t, ' |','or','|', s, '|','=', '|', or3, ' |')
print('|', t, ' |','or','|', t, ' |','=', '|', or4, ' |')
print('\n')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Apabila keduanya berbeda "True & False" "False & True" maka hasilnya akan "True". Nmaun jika keduanya bernilai sama maka hasilnya "False"
'''
print('================ XOR ================') 
t = True
s = False
# menggunakan Operator "^" dan diletakkan antara 2 variabel
or1 =  s ^ s
or2 =  s ^ t
or3 =  t ^ s
or4 =  t ^ t
print('|', s,'|','xor','|', s,'  |','=','|',or1, '|')
print('|', s,'|','xor','|', t,'   |','=','|',or2, ' |')
print('|', t,' |','xor','|', s,'  |','=','|',or3, ' |')
print('|', t,' |','xor','|', t,'   |','=','|',or4, '|')
print('\n')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
XNOR adalah kebalikan dari XOR, apabila  jika keduanya bernilai sama maka hasilnya "True". Namun jika keduanya berbeda maka hasilnya akan "False"
'''
print('================ XNOR ================')
t = True
s = False
or1 =  s ^ s
or2 =  s ^ t
or3 =  t ^ s
or4 =  t ^ t
# Tinggal Menambahkan operasi "not" pada Variabel "or1"
print('|', s,'|','xor','|', s,'  |','=','|',not or1, '  |') 
print('|', s,'|','xor','|', t,'   |','=','|',not or2, ' |')
print('|', t,' |','xor','|', s,'  |','=','|',not or3, ' |')
print('|', t,' |','xor','|', t,'   |','=','|',not or4, '  |')
print('\n')
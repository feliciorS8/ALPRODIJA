#setelah diinputkan datanya acak buat soal online trus pas org pertama ngerjain bisa jd nomern 1 ada dibaris pertama tapi pas org ke2 no 1 ada di ke 10
#characteristic gk bisa diurut,aacak,tidak bisa diubah
#BUAT SET --> bracket, constructor
mySet = {'s', 'e', 't',1}
mySet2 = set(('s', 'e','t', 2))

# UNORDERED --> urutan tidak sama
print('Data', mySet)
print('Data', mySet2)
print('--------------')

# UNINDEXED --> tidak memiliki index
# ex: tampilkan index angka 1
myIndex = mySet.index(1)

print('Index angka 1:',myIndex)
print('--------------------')

#UNDUPLICATABLE --> unique
mySet = {'s', 'e', 't',1,1}
mySet2 = set(('s','e','t',2,2))
print('Duplikat', mySet)
print('Duplikat', mySet2)
print('--------------------')

# UNCHANGEABLE --> tidak dapat dirubah
# ex: ubah angka index 3 dengan 9
mySet [3] = 9
print('Hasil Edit', mySet)
print('--------------------')

# HAPUS DATA
# pop: random, remove: specific
mySet.pop()
print('Hasil Pop:', mySet)
print('--------------------')

# TAMBAH DATA add
mySet.add(5)
print('Hasil Add: ', mySet)
print('--------------------')

# ex: hapus 's' dari mySet
mySet.remove('s')
print('Hasil Remove :',mySet)
print('--------------------')
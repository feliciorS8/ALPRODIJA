def tanah(panjang, lebar):
  luas_tanah = panjang * lebar
  return luas_tanah

def harga(luas, hpm):
  jual = luas * hpm
  print('harga jual tanah:', jual)
  print('---------------------')
  return jual # Menambahkan return agar nilai bisa digunakan

#call function
luas = tanah(4, 4)
harga_total = harga(luas, 500)
print("Harga total yang dikembalikan:", harga_total)
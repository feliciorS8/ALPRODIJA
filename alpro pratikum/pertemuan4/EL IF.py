print ('HASIL UJIAN')
nilai =int(input('masukkan nilai:'))

#proses
if nilai > 90 :
    transkip = 'A'
    
elif nilai > 70 :
    transkip = 'B'
elif nilai > 60 :
    transkip = 'C'
elif nilai > 50:
    transkip = 'D'
else:
    transkip = 'E'
    
    #output
print('Nilai transkip:' , transkip)
print('---------------')
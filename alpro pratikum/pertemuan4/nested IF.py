#if didalam if
print('HASIL UJIAN')
nilai = int(input('Masukkan nilai: '))

#proses
if nilai >=80:
    status = 'LULUS'
    if nilai >=90:
        predikat = 'memuaskan'
    else:
        predikat = 'cukup'
else:
    status ='TIDAK LULUS'
    predikat = 'kurang'
    
#output
print('status:', status)
print('predikat:', predikat)
print('---------------')
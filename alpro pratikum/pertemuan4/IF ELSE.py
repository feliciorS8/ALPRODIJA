#input
print('hasil ujian akhir semester')
nilai = int(input('Masukkan nilai: '))

#proses
if nilai >= 80:
    status = 'lulus'
else:
    status = 'tidak lulus'
#output
print('status:', status)
print('---------------')
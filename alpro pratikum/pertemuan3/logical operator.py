print('operator AND')
print('semus perintah benar :',
       (5>3) and (10>5))
print('salah satu perintah salah :',
       (5<3) and (10>5))
print('-----------------')

print('operator OR')
print('semua perintah salah :',
       (5<3) or (10<5))
print('salah satu perintah salah :',
       (5<3) or (5>10))
print('-----------------')

print('operator NOT')
print('perintah benar :', not(10<5))
print('perintah salah :', not(10>5))
print('-----------------')
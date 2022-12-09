awal = int (input( "Masukkan awal deret :"))
akhir = int (input ( " Masukkan akhir deret :" ))

for x in range (awal,akhir):
    if x%6 != 0 and x%3 != 0 and x%2!= 0 :
        print (x, end= ' ')

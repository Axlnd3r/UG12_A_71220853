a = int(input( " Masukkan Pembatas :"))
z = int (input( "Masukkan Angka yang dilarang :"))

for x in range (0,a,1):
    if x == z:
        continue
    print (x, end=' ')

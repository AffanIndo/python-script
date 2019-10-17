
"""
kasir.py
The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
"""

from math import floor

uang = int(input("Masukkan uang (Rp): "))
harga = int(input("Masukkan harga barang (Rp): "))

if (uang < harga):
    print("Uang kurang")
else:
    kembalian = uang - harga
    print("Kembalian: " + str(kembalian))

    sisa = kembalian

    print(str(floor(sisa / 100000)) + " x Rp100000")
    sisa = kembalian % 100000

    print(str(floor(sisa / 50000)) + " x Rp50000")
    sisa = kembalian % 50000

    print(str(floor(sisa / 20000)) + " x Rp20000")
    sisa = kembalian % 20000

    print(str(floor(sisa / 10000)) + " x Rp10000")
    sisa = kembalian % 10000

    print(str(floor(sisa / 5000)) + " x Rp5000")
    sisa = kembalian % 5000

    print(str(floor(sisa / 2000)) + " x Rp2000")
    sisa = kembalian % 2000

    print(str(floor(sisa / 1000)) + " x Rp1000")
    sisa = kembalian % 1000

    print(str(floor(sisa / 500)) + " x Rp500")
    sisa = kembalian % 500

    print("Sisa: Rp" + str(sisa))

#
# Copyright (c) Kelompok 10 Alprog Matematika UI 2016. All rights reserved.
# Program: 79 lines
# Main Program: 62 sloc
#

print 75 * "=" + "\n" + (43 * " ").center(75, "=")
print (("Selamat Datang di Program Daftar Kata").center(43, " ")).center(75, "=")
print (("Created by:  Kelompok 10 Alprog").center(43, " ")).center(75, "=")
print (43 * " ").center(75, "=") + "\n" + 75 * "="
print "\nProgram ini akan menganalisis file anda dan menyimpannya dalam Hasil.txt"
print "Input harus berupa sebuah file txt"

import os, sys, time
os.chdir(os.path.dirname(sys.argv[0]))

while True:
    while True:
        while True:
            File = raw_input("\nplease enter file name: ")
            if File[-4:] == ".txt":
                break
            print("\nfile extension must be with .txt")
        print "loading..."
        time.sleep(1)
        if os.path.isfile(File) == True:
            print "\nfile loaded\n"
            break
        else:
            print "\nfile does not exist"
            
    Paragraph_Count = len(open(File, "r").readlines())
    
    Data = open(File, "r").read()
    Data = Data.lower()
    
    i = 0
    while i < len(Data):
        if ord(Data[i]) < ord("a") or ord(Data[i]) > ord("z"):
            if ord(Data[i]) == ord("-"):
                Data = Data[:i] + Data[i].replace(Data[i], "") + Data[i+1:]
                i += 1
            else:
                Data = Data[:i] + Data[i].replace(Data[i], " ") + Data[i+1:]
        i += 1
        
    Data = Data.split(" ")
    Data = filter(lambda i: i != "", Data)
    
    Word_Count = len(Data)
    
    DataSet = list(set(Data))
    DataSet.sort()
    
    Hasil = open("Hasil.txt", "w")
    Hasil.write(File)
    Hasil.write("\n\nBanyak Paragraf: %d"%(Paragraph_Count))
    Hasil.write("\nBanyak Kata: %d\n\n"%(Word_Count))
    Hasil.write("Daftar Kata".center(15))
    Hasil.write("\n" + 15 * "=")
    for i in range(0, len(DataSet)):
        Hasil.write("\n")
        Hasil.write(DataSet[i] + " = " + str(Data.count(DataSet[i])))
    Hasil.close()
    
    print "Banyak Paragraf: ", Paragraph_Count
    print "Banyak Kata: ", Word_Count
    print "\n Secara lengkap hasil dapat dilihat di Hasil.txt"
    
    print "\nApakah ingin mencoba lagi?"
    while True:
        Again = raw_input("y/n: ")
        if Again == "y" or Again == "n":
            break
        print "tolong masukkan pilihan yang benar\n"
    if Again == "n":
        print "\nTerima kasih telah menggunakan program ini ^-^"
        time.sleep(3)
        sys.exit()
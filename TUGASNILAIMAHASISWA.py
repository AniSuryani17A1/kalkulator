print "PENGHITUNGAN NILAI MAHASISWA SEMESTER \n<><><><><><><><><><><><><>\n"
nama  = raw_input ("Masukan Nama Anda         : ")
uas   = input ("Masukan Nilai UAS Anda    : ")
uts   = input ("Masukan Nilai UTS Anda    : ")
quis  = input ("Masukan Nilai Quis Anda   : ")
final = input ("Masukan NilaiFinal Anda   : ")
print"\n HASIL AKHIR NILAI MAHASISWA \n<><><><><><><><><><><><><><><><><>\n"

print "NAMA ANDA ADALAH        :%s"%nama
print "NILAI UAS ANDA ADALAH   :%d"%uas
print "NILAI UTS ANDA ADALAH   :%d"%uts
print "NILAI QUIS ANDA ADALAH  :%d"%quis
print "NILAI FINAL ANDA ADALAH :%d"%final

Nilai = uas+uts+quis+final
print "JUMLAH NILAI ANDA SEMUA :%d"%nilai
print "NILAI SEMUA ANDA ADALAH :"

if nilai   >= 80:
    print "A"

elif nilai >= 70:
    print "B"

elif nilai >= 55:
    print "C"

elif nilai >= 40:
    print  "D"

elif nilai >= 39:
    print  "E"


    

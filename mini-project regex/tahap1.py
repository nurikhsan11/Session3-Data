#Import library yang dibutuhkan
import pandas as pd

# Baca file dqlabregex.tsv
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
print("Tabel A:")
print(dqlabregex)

#Ubah karakter pada kolom jumlah_member sesuai ketentuan
mapchange = {'([0-9]{2})-([0-9]{2})-([0-9]{4})': '\\3-\\2-\\1', '([0-9]{2})/([0-9]{2})/([0-9]{4})' : '\\3-\\1-\\2'}
for ubah, pengubah in mapchange.items():
   dqlabregex['tanggal_catat'] = dqlabregex['tanggal_catat'].str.replace(ubah, pengubah)
 
#Ubah menjadi tipedata datetime pada kolom tanggal_catat
dqlabregex['tanggal_catat'] = pd.to_datetime(dqlabregex['tanggal_catat'])
 
#Hapus karakter non numerik pada kolom jumlah_member dan ubah tipedatanya menjadi integer
dqlabregex['jumlah_member'] = dqlabregex['jumlah_member'].str.replace('[^0-9]','')
dqlabregex['jumlah_member'] = dqlabregex['jumlah_member'].astype('int')
 
#Ubah kata Sendja ataupun padanannya menjadi satu kata 'Senja' pada kolom staf_pencatat
dqlabregex['staf_pencatat'] = dqlabregex['staf_pencatat'].str.replace('Sen.?ja', 'Senja')
 
#Tampilkan hasilnya
print("\nTabel B:")
print(dqlabregex)
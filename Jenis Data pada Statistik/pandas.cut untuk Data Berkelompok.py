# Importlah pandas sebagai aliasnya pd
import pandas as pd
# Data berat badan 120 orang 
bb120 = [71.2, 66.8, 66.9, 65.9, 69.7, 63.4, 71.5, 66.5, 68.6, 67.5, 
         70.9, 63.9, 67.4, 67.2, 70.3, 65.8, 67.7, 66.2, 68.1, 69.2, 
         65.8, 70.3, 69.8, 69.0, 69.8, 66.6, 67.8, 66.1, 67.5, 69.1, 
         66.6, 67.2, 66.6, 66.3, 66.7, 68.0, 65.8, 68.5, 71.3, 69.5, 
         67.6, 66.2, 66.5, 71.4, 68.1, 66.7, 68.4, 72.2, 68.2, 69.2, 
         68.6, 67.3, 65.7, 67.3, 67.6, 69.2, 69.7, 69.9, 68.6, 69.8, 
         66.5, 70.5, 69.0, 67.4, 69.0, 67.8, 70.3, 71.0, 72.4, 65.2, 
         65.1, 67.0, 68.3, 69.8, 68.6, 64.0, 67.4, 69.7, 68.5, 69.5, 
         67.6, 67.6, 68.4, 68.8, 68.4, 68.2, 66.7, 68.8, 68.2, 70.3, 
         70.4, 68.4, 67.2, 66.7, 68.8, 68.2, 67.3, 68.1, 66.8, 69.4, 
         67.1, 70.4, 68.8, 69.2, 65.8, 68.3, 69.5, 66.1, 67.5, 68.1, 
         65.3, 68.6, 69.7, 66.3, 68.7, 65.4, 67.9, 64.8, 70.2, 68.8]
# Bin dengan menggunakan urutan bilangan (menggunakan list)
# yang sesuai dengan tabel yang dicontohkan
bin_list = list(range(63, 74))
print("bin berat badan dalam urutan bilangan:\n", bin_list)
# Buatlah kelompok data seperti tabel yang ditunjukkan
bin_bb = pd.cut(bb120, bin_list, right=False, include_lowest=True)
# Ubah bb120 ke dalam pandas.DataFrame
df_bb120 = pd.DataFrame(bb120)
# Kelompokkanlah df_bb120 ke dalam bin yang telah disediakan
tabel_bb = df_bb120.groupby(bin_bb).count()
# Untuk menset header dari tabel_bb
tabel_bb.rename(columns={0: "frekuensi"}, inplace=True)
tabel_bb.index.rename("rentang berat badan [kg]", inplace=True)
print("\nData berkelompok berat badan 120 orang:\n", tabel_bb)

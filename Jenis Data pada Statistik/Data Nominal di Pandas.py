# Importlah pandas sebagai aliasnya pd
import pandas as pd
# Data jenis_kelamin
gender = ["Pria", "Pria", "Wanita", "Pria", "Wanita",
          "Wanita", "Wanita", "Pria", "Pria", "Wanita"]
df = pd.DataFrame({"jenis_kelamin": gender})
# Cek tipe data
print("Cek tipe data awal:\n ", df.dtypes)

# Buat kategori untuk kolom jenis_kelamin
cat = pd.CategoricalDtype(["Pria", "Wanita"])
# Ubahlah tipe data kolom jenis_kelamin
df = df.astype({"jenis_kelamin": cat})
# Cek kembali tipe data
print("\nCek tipe data setelah diubah:\n ", df.dtypes)

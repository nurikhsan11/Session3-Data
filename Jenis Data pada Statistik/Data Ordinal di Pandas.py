# Importlah pandas sebagai aliasnya pd
import pandas as pd
# Data jenis_kelamin
gender = ["Pria", "Pria", "Wanita", "Pria", "Wanita",
          "Wanita", "Wanita", "Pria", "Pria", "Wanita"]
# Data cek medis
mcu = ["tidak pernah", "rutin (1 tahun sekali)",
       "tidak tentu waktunya", "tidak pernah", 
       "rutin (1 tahun sekali)", "lebih dari 2 tahun sekali",
       "tidak pernah", "tidak pernah", 
       "rutin (1 tahun sekali)", "2 tahun sekali"]
# Data frame
df = pd.DataFrame({"jenis_kelamin": gender,
                   "cek_medis": mcu})
# Cek tipe data
print("Cek tipe data awal:\n", df.dtypes)

# Buat kategori untuk kolom jenis_kelamin
cat = pd.CategoricalDtype(["Pria", "Wanita"])
# Buat kategori berurut untuk kolom cek_medis
ordl = pd.CategoricalDtype(["tidak pernah", 
                            "tidak tentu waktunya",
                            "lebih dari 2 tahun sekali",
                            "2 tahun sekali",
                            "rutin (1 tahun sekali)"], ordered=True)
# Ubahlah tipe data kolom jenis_kelamin dan cek_medis
df = df.astype({"jenis_kelamin": cat,
                "cek_medis": ordl})
# Cek kembali tipe data
print("\nCek tipe data setelah diubah:\n", df.dtypes)

# Cetaklah tiga baris teratas sesuai dengan yang ditunjukkan pada bagian Theory, ketikkan di baris 33
print("\n", df["cek_medis"].head(3))
# Gunakan kutip dua untuk setiap string
import numpy as np
# Importlah norm dari scipy.stats
from scipy.stats import norm

# Baca data survei_tinggi_badan.txt dengan numpy loadtxt
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)

# Rata-rata dan standar deviasi unbiased tinggi_badan
tb_mean = tinggi_badan.mean()
tb_std = tinggi_badan.std(ddof=1)
# Tentukanlah nilai probabilitas dan probabilitas kumulatif menggunakan 
# distribusi normal untuk tinggi badan, x = 165 cm
x = 165
pdf_x = norm.pdf(x, loc=tb_mean, scale=tb_std)
cdf_x = norm.cdf(x, loc=tb_mean, scale=tb_std)
print("Probabilitas x = %d cm adalah %.4f." % (x, pdf_x))
print("Probabilitas kumulatif x = %d cm adalah %.4f." % (x, cdf_x))

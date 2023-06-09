# Gunakan kutip dua untuk setiap string
import numpy as np
# Import matplotlib.pyplot dan seaborn sebagai aliasnya
# dan importlah norm dari scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Baca data survei_tinggi_badan.txt dengan numpy loadtxt
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)

# Rata-rata dan standar deviasi unbiased tinggi_badan
tb_mean = tinggi_badan.mean()
tb_std = tinggi_badan.std(ddof=1)
# Buat data tinggi badan yang terdistribusi normal dengan 
# rata-rata pada tb_mean dan standar deviasi unbiased pada tb_std
# untuk menghasilkan 1001 titik data baru berdasarkan nilai kuantilnya
tb = np.linspace(norm.ppf(0.001, loc=tb_mean, scale=tb_std), 
                 norm.ppf(0.999, loc=tb_mean, scale=tb_std), 1001)
# kurva pdf dan kurva cdf berdasarkan data tb
pdf_tb = norm.pdf(tb, loc=tb_mean, scale=tb_std)
cdf_tb = norm.cdf(tb, loc=tb_mean, scale=tb_std)
# Nilai probabilitas dan probabilitas kumulatif menggunakan 
# distribusi normal untuk tinggi badan, 150 cm dan 170 cm
x = [150, 170]
pdf_x = norm.pdf(x, loc=tb_mean, scale=tb_std)
cdf_x = norm.cdf(x, loc=tb_mean, scale=tb_std)

# Buat figure sebagai canvas dengan ukuran 10 in x 5 in
# dengan dua suplots (2 kolom)
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# plotkan kurva pdf_tb pada subplot pertama: axs[0]
sns.lineplot(x=tb, y=pdf_tb, lw=3, ax=axs[0])
axs[0].fill_between(tb[(tb>=x[0]) & (tb<=x[1])], 
                    pdf_tb[(tb>=x[0]) & (tb<=x[1])], 
                    color="tab:orange", alpha=0.4)
axs[0].text(161, 0.023, "Area: %.4f" % (cdf_x[1]-cdf_x[0]), ha="center", fontsize=12)

# plotkan kurva cdf_tb pada subplot kedua: axs[1]
sns.lineplot(x=tb, y=cdf_tb, lw=3, ax=axs[1])
for i, _x in enumerate(x):
    axs[1].plot([_x, _x], [0, cdf_x[i]], color="tab:orange")
    axs[1].plot([140, _x], [cdf_x[i], cdf_x[i]], color="tab:orange")
    axs[1].text(140.8, cdf_x[i], "%.4f" % cdf_x[i], color="tab:orange", ha="right")
    
axs[1].plot([147, 147], cdf_x, color="black")
axs[1].text(147, 0.5, "%.4f" % (cdf_x[1]-cdf_x[0]), color="black", ha="center", backgroundcolor="white")

# set label
axs[0].set_ylabel("Probabilitas", fontsize=12)
axs[0].set_ylim(bottom=-0.001)
for ax in axs:
    ax.set_xlabel("Tinggi badan (cm)", fontsize=12)
    ax.set_xlim([141,182])
    ax.grid(axis="y")
ax.set_ylabel("Probabilitas kumulatif", fontsize=12)
plt.tight_layout()
plt.show()

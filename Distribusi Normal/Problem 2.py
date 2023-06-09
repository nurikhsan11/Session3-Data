import numpy as np
from scipy.stats import norm

tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)

tb_mean = tinggi_badan.mean()
tb_std = tinggi_badan.std(ddof=1)

for i in range(1,4):
    x = tb_mean + np.array([-i, i]) * tb_std
    cdf_x = norm.cdf(x, loc=tb_mean, scale=tb_std)
    print("Area di bawah kurva pdf (%ds s/d %ds)" % (-i, i))
    print("  pdf(%.4f <= x <= %.4f) = %.4f.\n" % (*x, np.diff(cdf_x)))

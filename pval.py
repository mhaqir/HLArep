from scipy.stats import binom

# n = 642234 * 10
n = int((107039 * 12000) / 24)
k = 194
f = 2000 / 42
p = 66 / (300000 * f)

# pvalue = 1 - binom.cdf(k, n, p)
print("p:", p)
print ("pvalue:", 1 - binom.cdf(k, n, p))
print("n:", n)

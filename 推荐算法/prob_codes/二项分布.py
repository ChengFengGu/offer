import numpy as np
from scipy import stats

import matplotlib.pyplot as plt


def binom_pmf_test():

    n = 100
    p = 0.5
    k = np.arange(0, 100)

    binomal = stats.binom.pmf(k, n, p)

    print(f"概率和为=>{binomal} binomal[2]:{binomal[2]}")
    plt.plot(k, binomal, "o-")
    plt.xlabel("Number of successive")
    plt.ylabel("Probability of success", fontsize=15)
    plt.im

if __name__ == '__main__':

    binom_pmf_test()

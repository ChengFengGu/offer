import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def normal_distribution():

    mu = 0
    sigma = 1
    x = np.arange(-10, 10, 0.1)
    y = stats.norm.pdf(x, mu, sigma)

    print(y)

    plt.plot(x, y)
    plt.title(f'Norm mu:{mu:.2f} sigma:{sigma:.2f}')
    plt.xlabel('x')
    plt.ylabel('Probability density',fontsize=15)
    plt.savefig("推荐算法/prob_codes/imgs/normal.png")


if __name__ == '__main__':
    normal_distribution()
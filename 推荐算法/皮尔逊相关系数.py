from scipy.stats import pearsonr
from sklearn.metrics.pairwise import cosine_similarity

A = [5,3,4,4]
u1 = [3,1,2,3]
u2 = [4,3,4,3]
u3 = [3,3,1,5]
u4 = [1,5,5,2]


print(pearsonr(A,u1))
print(pearsonr(A,u2))
print(pearsonr(A,u3))
print(pearsonr(A,u4))

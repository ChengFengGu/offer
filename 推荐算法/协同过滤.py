import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

a1=np.arange(15).reshape(3,5)
a2=np.arange(20).reshape(4,5)

s12 = cosine_similarity(a1,a2)   #第一行的值是a1中的第一个行向量与a2中所有的行向量之间的余弦相似度

s11 = cosine_similarity(a1)   #a1中的行向量之间的两两余弦相似度

print(s12)
print(s11)
"""
pip install jieba
"""
import jieba
s = "人生苦短，我学Python。Python是世界上最好的语言"
r = jieba.cut(s)
print(r)
print(",".join(r))
l = jieba.lcut(s)
print(l)
# import  os
# os.system("pa")
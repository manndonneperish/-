score = [9, 10, 8, 9, 10, 7, 6, 8, 7, 8]
score.sort()
del score[0]
del score[-1]
avescore = sum(score) / len(score)
print("总分为：", avescore)

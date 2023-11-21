s = "How are you"
n = int(input("您要查看第几个单词（1—3）:"))
word = s[(n - 1) * 4:4 * n]
print(word)
s1 = s[::-1]
s1 = s1.upper()
print(s1)
s2 = s.title()
lst = s2.split()
s2 = ' '.join(lst[::-1])
print(s2)

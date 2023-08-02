date = '10/9/2020'
i = date.find('/')
j = date.rfind('/')
year = date[j + 1:]
month = date[i + 1:j]
day = date[:i]
print('{:0>4}-{:0>2}-{:0>2}'.format(year, month, day))

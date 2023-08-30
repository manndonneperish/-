# 6
dic_country = {'China': 'Beijing', 'America': 'Washington', 'Norway': 'Oslo', 'Japan': 'Tokyo', 'Germany': 'Berlin',
               'Canada': 'Ottawa', 'France': 'Paris', 'Thailand': 'Bangkok'}
country = input("请输入国家名：")
Country = country.title()
if Country not in dic_country:
    print("未查询到该国家名！")
else:
    print(dic_country[Country])

# 7
dicUsers = {"John": 123, "Marry": 111, "Tommy": 123456}
name = input()
password = eval(input())
if name not in dicUsers:
    print("u name not exist")
elif password == dicUsers[name]:
    print("welcome")
else:
    print("password error!")

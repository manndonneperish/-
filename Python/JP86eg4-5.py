ls = eval(input('请输入一个数值列表：'))
lst = sorted(ls)
x = int(input('请输入待查找的数：'))
low = 0
high = len(lst) - 1
while low < high:
    mid = (low + high) // 2
    if lst[mid] < x:
        low = mid + 1
    elif lst[mid] > x:
        high = mid - 1
    else:
        print('找到{}，索引为{}！'.format(x, mid));
        break;
else:
    print('没有找到{}'.format(x))

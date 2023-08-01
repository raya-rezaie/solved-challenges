length = int(input())

heights = list(map(int,
	input().strip().split()))[:length]
a = heights[0]
list1 = [a]
for i in range(1,length):
    if heights[i] > a :
        list1.append(heights[i])
        a = heights[i]
    else :
        list1.append(a)
a = heights[length-1]
list2 = [a]
for i in range(length-2 , -1 , -1):
    if heights[i] > a:
        list2.append(heights[i])
        a = heights[i]
    else :
        list2.append(a)

list2.reverse()

result1 = []
result2 = []
for i in range(length):
    result1.append(min(list1[i] , list2[i] ))
ans = 0
for i in range (length):
    ans += result1[i] -heights[i] 

print(ans)
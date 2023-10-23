#1919번 애너그램 만들기

a = input()
b = input()
res = 0

alpah = [0] * 26
alpah_2 = [0] * 26

for i in a:
    idx = ord(i) - ord('a')
    alpah[idx] += 1

for j in b:
    idx = ord(j) - ord('a')
    alpah_2[idx] += 1
    
for k in range(26):
    if alpah[k] == alpah_2[k]:
        continue
    else:
        res += abs(alpah[k] - alpah_2[k])
        
print(res)
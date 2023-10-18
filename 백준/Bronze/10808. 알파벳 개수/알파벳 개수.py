#10808번 알파벳 개수

bark = input()
data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
data_2 = [0] * 26
for i in range(len(bark)):
    for j in range(len(data)):
        if bark[i] == data[j]:
            data_2[j] += 1
res = []            
res = " ".join(map(str, data_2))          
print(res)
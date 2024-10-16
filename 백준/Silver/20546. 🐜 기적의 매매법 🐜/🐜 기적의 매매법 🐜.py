money = int(input()) # 초기 현금
MachineDuck = list(map(int, input().split())) # 1일부터 14일까지의 주가

money_bnp = money
count_bnp = 0

money_timing = money_bnp
count_timing = 0

for num, price in enumerate(MachineDuck):
    #준현의 경우 
    count_bnp += (money_bnp // price)
    money_bnp %= price

    temp = MachineDuck[num:num+4]
    if len(temp) < 4:
        continue

    if temp[0] < temp[1] < temp[2] < temp[3] and count_timing > 0:
        money_timing += count_timing * temp[3]
        count_timing = 0
    elif temp[0] > temp[1] > temp[2] > temp[3]:
        count_timing += (money_timing // temp[3])
        money_timing %= temp[3]

answer_bnp = money_bnp +count_bnp * MachineDuck[-1]
answer_timing = money_timing + (count_timing * MachineDuck[-1])

if answer_bnp > answer_timing:
    ans = 'BNP' 
elif answer_bnp < answer_timing:
    ans = 'TIMING'
else:
    ans = "SAMESAME"
    
print(ans)


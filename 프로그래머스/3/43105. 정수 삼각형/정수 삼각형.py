def solution(triangle):
    #dp 테이블 구성
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[1][0] + triangle[0][0]
    dp[1][1] = triangle[1][1]+ triangle[0][0]
    for i in range(2, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
                continue
            elif j == len(triangle[i])-1:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                continue
                
            dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])
            
    return max(dp[len(triangle)-1])
        
        
class Solution:
    def reverse(self, x: int) -> int:
        print('dfdf')
        if (x < 10 and x > -10):
            return x
        
        # tag 数字转成对于python更容易
        x_str = list(str(x))
        i, j = 0, len(x_str) - 1
        if (x_str[0] == '-'):
            i += 1
            
        while(i < j):
            x_str[i], x_str[j] = x_str[j], x_str[i]
            i += 1
            j -= 1
        
        
        i, j = 0, len(x_str) - 1
        if (x_str[0] == '-'):
            i += 1
            
        while (i < len(x_str) and x_str[i] == '0'):
            i += 1
            
        result = 0
        for v in range(j, i - 1, -1):
            print((len(x_str) - 1 - j), v)
            # result += int(x_str[v]) * 1e(len(x_str) - 1 - j)
            
        
        if (x_str[0] == '-'):
            result *= -1
        return result

s = Solution()
print(s.reverse(123))
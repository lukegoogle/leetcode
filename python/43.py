def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
        
    m, n = len(num1), len(num2)
    result_arr = [0] * (m + n)
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            d1 = int(num1[i])
            d2 = int(num2[j])
            
            prod = d1 * d2
            pos1 = i + j
            pos2 = i + j + 1
            
            total_sum = prod + result_arr[pos2]
            
            result_arr[pos1] += total_sum // 10
            result_arr[pos2] = total_sum % 10

    i = 0
    while i < len(result_arr) and result_arr[i] == 0:
        i += 1
        
    return "".join(map(str, result_arr[i:]))

# Example Output
print(f"Output for ('2', '3'): {multiply('2', '3')}")
print(f"Output for ('123', '456'): {multiply('123', '456')}")
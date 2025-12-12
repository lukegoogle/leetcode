def myPow(x: float, n: int) -> float:
    def fast_pow(base, exponent):
        if exponent == 0:
            return 1.0
        
        half = fast_pow(base, exponent // 2)
        
        if exponent % 2 == 0:
            return half * half
        else:
            return half * half * base

    if n < 0:
        x = 1 / x
        n = -n
        
    return fast_pow(x, n)

# Example Output
print(f"Output for (2.00000, 10): {myPow(2.0, 10)}")
print(f"Output for (2.10000, 3): {myPow(2.1, 3)}")
print(f"Output for (2.00000, -2): {myPow(2.0, -2)}")
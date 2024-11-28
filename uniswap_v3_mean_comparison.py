import math

def compare_means():
    # Initial values
    x = 10.0        # ETH
    y = 20000.0     # USDC
    price = y/x     # 2000 USDC/ETH
    
    # Calculate both means
    geometric_mean = math.sqrt(x * y)
    arithmetic_mean = (x + y) / 2
    
    print("Initial State:")
    print(f"ETH (x): {x}")
    print(f"USDC (y): {y}")
    print(f"Price: {price}")
    print(f"\nGeometric Mean (L): {geometric_mean}")
    print(f"Arithmetic Mean: {arithmetic_mean}")
    
    # Recover x and y using geometric mean (L)
    recovered_x = geometric_mean / math.sqrt(price)
    recovered_y = geometric_mean * math.sqrt(price)
    
    print(f"\nRecovered using geometric mean (L):")
    print(f"Recovered ETH: {recovered_x}")
    print(f"Recovered USDC: {recovered_y}")
    
    # Try to recover using arithmetic mean
    # This is much more complex and doesn't work well
    print(f"\nArithmetic mean is less useful because:")
    print(f"1. It's affected by token scales ({arithmetic_mean} is closer to USDC amount)")
    print(f"2. No simple formula to recover original amounts")
    print(f"3. Doesn't maintain useful properties during trades")

if __name__ == "__main__":
    compare_means()
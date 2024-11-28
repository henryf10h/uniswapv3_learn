import math

def calculate_liquidity(x: float, y: float) -> float:
    """Calculate liquidity L given token amounts x and y"""
    return math.sqrt(x * y)

def demonstrate_liquidity_changes():
    # Initial state
    x1 = 10.0  # Initial ETH
    y1 = 20000.0  # Initial USDC
    L1 = calculate_liquidity(x1, y1)
    
    print("Initial State:")
    print(f"Token X (ETH): {x1:.2f}")
    print(f"Token Y (USDC): {y1:.2f}")
    print(f"Liquidity (L): {L1:.2f}")
    print(f"x * y = {x1 * y1:.2f}")
    
    # Simulate a trade (x*y remains constant)
    x2 = 8.0  # Less ETH
    y2 = y1 * (x1/x2)  # More USDC (maintaining x*y constant)
    L2 = calculate_liquidity(x2, y2)
    
    print("\nAfter Trade (should maintain same L):")
    print(f"Token X (ETH): {x2:.2f}")
    print(f"Token Y (USDC): {y2:.2f}")
    print(f"Liquidity (L): {L2:.2f}")
    print(f"x * y = {x2 * y2:.2f}")
    
    # Simulate adding liquidity (x*y increases)
    x3 = x2 + 5.0  # Add 5 ETH
    y3 = y2 + 10000.0  # Add 10000 USDC
    L3 = calculate_liquidity(x3, y3)
    
    print("\nAfter Adding Liquidity (L should increase):")
    print(f"Token X (ETH): {x3:.2f}")
    print(f"Token Y (USDC): {y3:.2f}")
    print(f"Liquidity (L): {L3:.2f}")
    print(f"x * y = {x3 * y3:.2f}")
    
    # Simulate removing liquidity (x*y decreases)
    x4 = x3 - 3.0  # Remove 3 ETH
    y4 = y3 - 6000.0  # Remove 6000 USDC
    L4 = calculate_liquidity(x4, y3)
    
    print("\nAfter Removing Liquidity (L should decrease):")
    print(f"Token X (ETH): {x4:.2f}")
    print(f"Token Y (USDC): {y4:.2f}")
    print(f"Liquidity (L): {L4:.2f}")
    print(f"x * y = {x4 * y4:.2f}")

if __name__ == "__main__":
    demonstrate_liquidity_changes()

"""
If we have:
- 10 ETH (x)
- 20,000 USDC (y)
- Price = 20,000/10 = 2,000 USDC per ETH

Then:
L = √(10 * 20,000) = 447.21

We can verify:
x = L/√P = 447.21/√2000 = 10 ETH
y = L*√P = 447.21*√2000 = 20,000 USDC

"""
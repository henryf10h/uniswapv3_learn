import math
from decimal import Decimal, getcontext
import numpy as np
import matplotlib.pyplot as plt

# Set high precision for decimal calculations
getcontext().prec = 28

def tick_to_sqrt_price_x96(tick: int) -> int:
    """Convert a tick to its square root price"""
    return int(1.0001 ** (tick/2) * 2**96)

def sqrt_price_x96_to_price(sqrt_price_x96: int) -> Decimal:
    """Convert sqrt_price_x96 to actual price"""
    sqrt_price = Decimal(sqrt_price_x96) / Decimal(2**96)
    return sqrt_price * sqrt_price

def tick_to_price(tick: int) -> Decimal:
    """Convert a tick directly to price"""
    return Decimal(1.0001 ** tick)


def main():
    # Example: Converting between ticks, sqrt prices, and actual prices
    print("=== Uniswap V3 Price Conversion Examples ===")
    
    # Example tick value
    tick = 10
    
    # Get sqrt_price_x96
    sqrt_price_x96 = tick_to_sqrt_price_x96(tick)
    
    # Calculate final price
    price = sqrt_price_x96_to_price(sqrt_price_x96)
    
    print(f"\nFor tick {tick}:")
    print(f"sqrt_price_x96: {sqrt_price_x96}")
    print(f"Final price: {price}")
    
    # Direct tick to price calculation
    direct_price = tick_to_price(tick)
    print(f"Direct price calculation: {direct_price}")
    
    # Verify that both methods give the same result
    print(f"Difference between methods: {abs(price - direct_price)}")
    
if __name__ == "__main__":
    main()

"""
If you know you'll need to calculate with square roots most of the time
And you have a choice of storing either:

. The full number (P) and taking its square root repeatedly
. Or just storing its square root (√P) to begin with


It's more efficient to store √P
"""
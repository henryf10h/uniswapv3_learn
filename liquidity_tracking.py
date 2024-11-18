class Tick:
    def __init__(self, price, net_liquidity):
        self.price = price
        self.net_liquidity = net_liquidity

class LiquidityTracker:
    def __init__(self):
        self.ticks = {}  # price -> Tick
        self.current_liquidity = 0
        self.MAX_LIQUIDITY_PER_TICK = 2**238 - 1  # Uniswap V3's max liquidity per tick
    
    def add_position(self, lower_price, upper_price, liquidity):
        """Add a new liquidity position between two prices"""
        # Validate liquidity amount against max per tick
        if liquidity > self.MAX_LIQUIDITY_PER_TICK:
            raise ValueError(f"Liquidity exceeds maximum allowed per tick: {self.MAX_LIQUIDITY_PER_TICK}")
        
        # Add or update lower tick
        if lower_price not in self.ticks:
            self.ticks[lower_price] = Tick(lower_price, liquidity)
        else:
            new_net = self.ticks[lower_price].net_liquidity + liquidity
            if abs(new_net) > self.MAX_LIQUIDITY_PER_TICK:
                raise ValueError("Combined liquidity at tick exceeds maximum allowed")
            self.ticks[lower_price].net_liquidity = new_net
        
        # Add or update upper tick
        if upper_price not in self.ticks:
            self.ticks[upper_price] = Tick(upper_price, -liquidity)
        else:
            new_net = self.ticks[upper_price].net_liquidity - liquidity
            if abs(new_net) > self.MAX_LIQUIDITY_PER_TICK:
                raise ValueError("Combined liquidity at tick exceeds maximum allowed")
            self.ticks[upper_price].net_liquidity = new_net
    
    def calculate_liquidity_at_price(self, target_price):
        """Calculate active liquidity at a specific price"""
        active_liquidity = 0
        
        # Add up all liquidity changes from lowest tick up to target price
        for price in sorted(self.ticks.keys()):
            if price > target_price:
                break
            active_liquidity += self.ticks[price].net_liquidity
            
        return active_liquidity

def main():
    # Initialize tracker
    tracker = LiquidityTracker()
    
    # Add positions from our example
    print("Adding positions...")
    print("Position 1: 1800-2000 with 5 units of liquidity")
    tracker.add_position(1800, 2000, 5)
    
    print("Position 2: 1900-2200 with 3 units of liquidity")
    tracker.add_position(1900, 2200, 3)
    
    # Check liquidity at different price points
    test_prices = [1750, 1850, 1950, 2100, 2300]
    
    print("\nChecking liquidity at different price points:")
    for price in test_prices:
        liquidity = tracker.calculate_liquidity_at_price(price)
        print(f"Price {price}: Active Liquidity = {liquidity}")
        
    # Print tick information
    print("\nTick Information:")
    for price, tick in sorted(tracker.ticks.items()):
        print(f"Tick at price {price}: Net Liquidity = {tick.net_liquidity}")

if __name__ == "__main__":
    main()
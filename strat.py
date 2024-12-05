import random

# Constants for Abu Dhabi Grand Prix
TOTAL_LAPS = 58
PIT_STOP_TIME = 25  # Average time loss for a pit stop in seconds
SAFETY_CAR_PROBABILITY = 0.15  # Probability of safety car in a given stint

# Tire degradation rates (seconds lost per lap)
TIRE_DEGRADATION = {
    "Soft": 0.2,
    "Medium": 0.15,
    "Hard": 0.1
}

# Base lap times (approximation for Ferrari at Abu Dhabi)
BASE_LAP_TIMES = {
    "Soft": 95,   # Seconds per lap on Soft tires
    "Medium": 97,  # Seconds per lap on Medium tires
    "Hard": 99    # Seconds per lap on Hard tires
}

# Strategy configurations
STRATEGIES = [
    {"stints": [("Soft", 15), ("Medium", 23), ("Hard", 20)], "description": "Soft-Medium-Hard"},
    {"stints": [("Medium", 28), ("Hard", 30)], "description": "Medium-Hard"},
    {"stints": [("Soft", 20), ("Hard", 38)], "description": "Soft-Hard"},
]

def simulate_stint(tire, laps, safety_car=False):
    """Simulates a stint for a given tire type and number of laps."""
    total_time = 0
    lap_time = BASE_LAP_TIMES[tire]
    for lap in range(laps):
        # Apply degradation for each lap
        total_time += lap_time
        lap_time += TIRE_DEGRADATION[tire]
        # Apply safety car effect (if active)
        if safety_car and random.random() < SAFETY_CAR_PROBABILITY:
            total_time += lap_time * 0.7  # Reduced lap time during safety car
    return total_time

def simulate_race(strategy):
    """Simulates a full race based on a given strategy."""
    total_time = 0
    for stint in strategy["stints"]:
        tire, laps = stint
        safety_car = random.random() < SAFETY_CAR_PROBABILITY
        total_time += simulate_stint(tire, laps, safety_car)
        if stint != strategy["stints"][-1]:  # Add pit stop time unless it's the last stint
            total_time += PIT_STOP_TIME
    return total_time

def main():
    results = []
    for strategy in STRATEGIES:
        race_time = simulate_race(strategy)
        results.append((strategy["description"], race_time))
    
    # Sort results by race time
    results.sort(key=lambda x: x[1])
    
    # Display results
    print("Strategy Results:")
    for strategy, time in results:
        print(f"Strategy: {strategy}, Total Time: {time:.2f} seconds")
    
    print("\nOptimal Strategy:")
    print(f"Strategy: {results[0][0]}, Total Time: {results[0][1]:.2f} seconds")

# Run the simulation
main()

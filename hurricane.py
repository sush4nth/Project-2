import random
import time

class Hurricane:
    def __init__(self, name, wind_speed, pressure):
        self.name = name
        self.wind_speed = wind_speed  
        self.pressure = pressure 
        self.category = self.classify()

    def classify(self):
        """Classify the hurricane based on wind speed."""
        if self.wind_speed >= 157:
            return "Category 5"
        elif self.wind_speed >= 130:
            return "Category 4"
        elif self.wind_speed >= 111:
            return "Category 3"
        elif self.wind_speed >= 96:
            return "Category 2"
        elif self.wind_speed >= 74:
            return "Category 1"
        else:
            return "Tropical Storm"

    def update(self, wind_speed, pressure):
        """Update the hurricane's wind speed and pressure, and reclassify it."""
        self.wind_speed = wind_speed
        self.pressure = pressure
        self.category = self.classify()

    def __str__(self):
        """String representation of the hurricane."""
        return (f"Hurricane {self.name} - Wind Speed: {self.wind_speed} mph, "
                f"Pressure: {self.pressure} hPa, Classification: {self.category}")


# Simulation function
def simulate_hurricane():
    """Simulate changes in hurricane intensity over time."""
    hurricane = Hurricane("SimStorm", random.randint(60, 160), random.randint(950, 1010))
    print("Starting Hurricane Simulation...")
    print(hurricane)

    for i in range(10):  
        time.sleep(1) 
        new_wind_speed = hurricane.wind_speed + random.randint(-10, 10)
        new_pressure = hurricane.pressure + random.randint(-5, 5)

        new_wind_speed = max(0, new_wind_speed)  
        new_pressure = max(900, new_pressure)  
        hurricane.update(new_wind_speed, new_pressure)
        print(f"Update {i + 1}: {hurricane}")

# Run the simulation
if __name__ == "__main__":
    simulate_hurricane()

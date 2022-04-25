# Name: f1.py
# Author: Joe Bloggs, v1.0, contact_email
# Description: F1 car fuel calculations
"""
    Docstring contents here
"""

race_length = 45
fuel_per_lap = 2.25
fuel_requirement = race_length * fuel_per_lap
print("Minimum fuel requirement for %d laps at %.2fKg fuel per lap: %.2fKg" % (race_length, fuel_per_lap, fuel_requirement))

fuel_reserve = 1.5  # 50% contingency fuel
fuel_with_reserve = fuel_requirement * fuel_reserve
print("Total fuel carried with 50%% reserve: %.2fKg" % fuel_with_reserve)

lap_time_qualifying = 80.45     # Lap time with only 5kg fuel
lap_time_increase = 0.35        # Lap time increase per 10kg fuel
t_lap_time = lap_time_qualifying - (lap_time_increase/10) * 5    # Theoretical lap time
print("Qualifying lap time (5Kg Fuel): %.2f Seconds" % lap_time_qualifying)
print("Theoretical initial lap time: %.2f Seconds" % t_lap_time)

first_lap_time = t_lap_time + ((fuel_with_reserve/10) * lap_time_increase)
print("Lap 1 time (%.2fKg fuel): %.2f Seconds" % (fuel_with_reserve, first_lap_time))

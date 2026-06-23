print("welcome to the interactive person  data collection")

name=input("please enter your name")
age_str=input("please enter your age")
height_str=input("pleasse enter your height")
fav_num_str=input("please enterr your favourate number")

print("\nthank you ! here is the information we collected:\n")
age=int(age_str)
height=float(height_str)
fav_num_=int(fav_num_str)
current_year=2026
approx_birth_year=current_year-age

print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Fav Number: {fav_num_} (Type: {type(fav_num_)}, Memory Address: {id(fav_num_)})")

print(f"Your birth year is approximately: {approx_birth_year} (based on your age of {age})")
print("\nThank you for using the Personal Data Collector. Goodbye!")
year = [2020, 2021, 2022, 2023]

make = ["Toyota", "Ford", "Nissan"]

model = ["Corolla"]

number_of_doors = [1, 2, 3, 4]

type_of_sunroof = ["solid", "sunroof"]

if (year in year and
    make in make and
    model in model and
    number_of_doors in number_of_doors and
    type_of_sunroof in type_of_sunroof):

    print("\nVehicle type: Car")
    print("Year:", year)
    print("Make:", make)
    print("Model:", model)
    print("Number of doors:", number_of_doors)
    print("Type of roof:", type_of_sunroof)
else:
    print("\nSorry, one or more entries are not valid.")
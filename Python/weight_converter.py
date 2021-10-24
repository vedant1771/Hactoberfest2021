weight = input('weight: ')
unit = input('Lbs or Kg: ')

if unit.upper() == "LBS":
    converted = int(weight)*0.45
    print(f"you are {converted} kilos")
else:
    converted = int(weight)/0.45
    print(f"you are {converted} pounds")

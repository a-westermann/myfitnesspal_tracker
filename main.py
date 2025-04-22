import myfitnesspal

with open('creds') as file:
    lines = file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()

mfp_client = myfitnesspal.Client()

day = mfp_client.get_date(2024, 4, 21)


print(f"Calories: {day.totals['calories']}")
print(f"Protein: {day.totals['protein']}g")
print(f"Carbs: {day.totals['carbohydrates']}g")
print(f"Fat: {day.totals['fat']}g")

def main():
    welcome()
    gender = sex()
    weight = get_weight()
    height = get_height()
    age = get_age()

    # BMI Calculation
    bmi = calculate_bmi(weight, height)
    display_bmi(bmi)

    # BMR & Calorie Maintenance
    rest_bmr = calculate_bmr(gender, weight, height, age)
    total_calculation(rest_bmr)


def welcome():
    print("Welcome to your Calories + BMI Calculator!\nFind out how many calories you need daily and check your BMI.\n")


def sex():
    sexes = ["male", "female", "M", "F", "f", "m", "Male", "Female"]
    while True:
        sex = str(input("Do you identify as male or female? "))
        while sex not in sexes:
            sex = str(input("Please enter either 'male' or 'female': "))
        return sex


def get_weight():
    weight_kg = float(input("Enter your weight in kilograms: "))
    while weight_kg <= 0:
        weight_kg = float(input("Invalid input. Please enter your weight in kilograms: "))
    return weight_kg


def get_height():
    height_cm = float(input("Enter your height in centimeters: "))
    while height_cm <= 0:
        height_cm = float(input("Invalid input. Please enter your height in centimeters: "))
    return height_cm


def get_age():
    age_yrs = int(input("Enter your age in years: "))
    while age_yrs <= 0:
        age_yrs = int(input("Invalid input. Please enter your age in years: "))
    return age_yrs


def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def display_bmi(bmi):
    print(f"\nYour BMI is: {bmi}")
    if bmi < 18.5:
        print("You are classified as: Underweight")
    elif 18.5 <= bmi < 25:
        print("You are classified as: Normal weight")
    elif 25 <= bmi < 30:
        print("You are classified as: Overweight")
    else:
        print("You are classified as: Obese")


def calculate_bmr(gender, weight, height, age):
    male = ["male", "M", "m", "Male"]
    female = ["female", "F", "f", "Female"]
    if gender in female:
        bmr = (weight * 10) + (height * 6.25) - (age * 5) - 161
    else:
        bmr = (weight * 10) + (height * 6.25) - (age * 5) + 5
    return int(bmr)


def total_calculation(rest_bmr):
    user_activity_lvl = get_user_activity()

    maintain = {
        "sedentary": get_sedentary(rest_bmr),
        "light": get_light_activity(rest_bmr),
        "moderate": get_moderate_activity(rest_bmr),
        "active": get_very_active(rest_bmr)
    }

    print("\nCalorie Maintenance Recommendation:")
    if user_activity_lvl == "sedentary":
        print(f"You need to eat {int(maintain['sedentary'])} calories/day to maintain your current weight.")
    elif user_activity_lvl == "light":
        print(f"You need to eat {int(maintain['light'])} calories/day to maintain your current weight.")
    elif user_activity_lvl == "moderate":
        print(f"You need to eat {int(maintain['moderate'])} calories/day to maintain your current weight.")
    elif user_activity_lvl == "active":
        print(f"You need to eat {int(maintain['active'])} calories/day to maintain your current weight.")


def get_user_activity():
    activity_lvl = ["sedentary", "light", "moderate", "active"]
    prompt = """
What is your activity level?

- Sedentary: little to no exercise
- Light: light exercise/sports 1–3 days/week
- Moderate: moderate exercise/sports 3–5 days/week
- Active: hard exercise daily or twice/day

Please enter: 'sedentary', 'light', 'moderate', or 'active': """
    
    while True:
        user_lvl = str(input(prompt)).lower()
        while user_lvl not in activity_lvl:
            user_lvl = str(input("Invalid input. Please enter: 'sedentary', 'light', 'moderate', or 'active': "))
        return user_lvl


def get_sedentary(rest_bmr):
    return rest_bmr * 1.25


def get_light_activity(rest_bmr):
    return rest_bmr * 1.375


def get_moderate_activity(rest_bmr):
    return rest_bmr * 1.550


def get_very_active(rest_bmr):
    return rest_bmr * 1.725


if __name__ == '__main__':
    main()

# workout_planner.py

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def workout_suggestion(bmi):
    if bmi < 18.5:
        return "Workout Time: 20 mins/day | Diet: High Protein | Location: Home"
    elif 18.5 <= bmi < 24.9:
        return "Workout Time: 30 mins/day | Diet: Balanced | Location: Home"
    elif 25 <= bmi < 29.9:
        return "Workout Time: 45 mins/day | Diet: Low Carb | Location: Gym"
    else:
        return "Workout Time: 60 mins/day | Diet: Low Fat & Sugar | Location: Gym"


def main():
    try:
        weight_input = input("Enter your weight in kg: ")
        height_input = input("Enter your height in cm: ")

        if not weight_input or not height_input:
            raise ValueError("Fields cannot be empty.")

        weight = float(weight_input)
        height = float(height_input)

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        suggestion = workout_suggestion(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(suggestion)

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()

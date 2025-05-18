# test_workout_planner.py
import pytest
from workout_planner import calculate_bmi, workout_suggestion

def test_calculate_bmi():
    assert calculate_bmi(70, 175) == 22.86
    assert calculate_bmi(50, 160) == 19.53
    assert calculate_bmi(90, 180) == 27.78

def test_workout_suggestion_underweight():
    assert "20 mins" in workout_suggestion(17)

def test_workout_suggestion_normal():
    assert "30 mins" in workout_suggestion(22)

def test_workout_suggestion_overweight():
    assert "45 mins" in workout_suggestion(27)

def test_workout_suggestion_obese():
    assert "60 mins" in workout_suggestion(32)

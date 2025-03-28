def generate_workout(goal):
    workouts = {
        "weight_loss": ["Running", "HIIT", "Jump Rope"],
        "muscle_gain": ["Push-ups", "Deadlifts", "Squats"]
    }
    return workouts.get(goal, [])

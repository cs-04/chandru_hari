import argparse
from workout_generator import generate_workout
from food_tracker import log_food
from database import *
from user_profile import view_profile , update_profile
from food_tracker import get_calories

def main_manu():
    while True:
        print("\n📲 Welcome to the Fitness Tracker CLI")
        print("1. Sign Up (Create a New Account)")
        print("2. Log In to Existing Account")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            create_user()
        elif choice == "2":
            return login()
        elif choice == "3":
            print("👋 Goodbye! See you next time.")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

   
def dashboard(user):
    """Main fitness dashboard."""
    while True:
        print("\n📊 Fitness Dashboard (Main Menu)")
        print("1. View Profile")
        print("2. Log Workout")
        print("3. Log Food Intake")
        print("4. View Progress")
        print("5. Update Profile")
        print("6. Log Out")
        
        choice = input("Choose an option (1–6): ")

        if choice == "1":
            view_profile(user)
        elif choice == "2":
            #log_workout()
            print("Log workout")
        elif choice == "3":
            get_calories()
        elif choice == "4":
            #view_progress()
            print("Your progress")
        elif choice == "5":
            update_profile(user)
        elif choice == "6":
            print("👋 Logging out... See you next time!")
            break
        else:
            print("❌ Invalid choice. Please select a number between 1 and 6.")


    parser = argparse.ArgumentParser(description="Fitness Tracker CLI")
    parser.add_argument('--workout', help="Generate a workout plan")
    parser.add_argument('--food', nargs=2, help="Log food and calories")

    args = parser.parse_args()

    if args.workout:
        workout_plan = generate_workout(args.workout)
        print(f"Workout Plan for {args.workout}: {workout_plan}")

    if args.food:
        item, calories = args.food
        result = log_food(item, calories)
        print(result)            
    

def main():
    
    user = main_manu()

    dashboard(user)
         

if __name__ == '__main__':
    main()

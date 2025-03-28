from database import *


def view_profile(user):
    """Display user profile."""
    print("\n📄 Your Profile")
    print(f"Name: {user.name}")
    print(f"Username: {user.username}")
    print(f"Age: {user.age}")
    print(f"Gender: {user.gender}")
    print(f"Weight: {user.weight} kg")
    print(f"Height: {user.height} cm")


def update_profile(user):
    """Update user profile."""
    session = Session()
    try:
        print("\n✏️ Update Profile")
        user.name = input(f"Enter your name ({user.name}): ") or user.name
        user.age = int(input(f"Enter your age ({user.age}): ") or user.age)
        user.weight = float(input(f"Enter your weight ({user.weight} kg): ") or user.weight)
        user.height = float(input(f"Enter your height ({user.height} cm): ") or user.height)
        user.gender = input(f"Enter your gender ({user.gender}): ") or user.gender

        session.add(user)
        session.commit()
        print("✅ Profile updated successfully!")
    except Exception as e:
        session.rollback()
        print(f"❌ Error updating profile: {e}")
    finally:
        session.close()    
        
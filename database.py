import os
from sqlalchemy import create_engine, Column, Integer, String, Float ,DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from getpass import getpass
from datetime import datetime


# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://chandru:chandru8904@localhost/fitness")

# Connect to PostgreSQL
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define the 'users' table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String, nullable=False)
    weight = Column(Float)
    height = Column(Float)

class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)  # Link to the user
    meal_type = Column(String, nullable=False)  # Breakfast, Lunch, etc.
    food_name = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    protein = Column(Float, nullable=False)
    fat = Column(Float, nullable=False)
    date_logged = Column(DateTime, default=datetime.utcnow)

    
# Create tables
try:
    Base.metadata.create_all(engine)
    print("welcome to fitness tracker")
except Exception as e:
    print(f"Error creating tables: {e}")

# Session setup
Session = sessionmaker(bind=engine)
session = Session()

# Function to create a new user with hashed password
def create_user():
    session = Session()
    try:
        print("\n👤 Create a New Account")
        username = input("Enter a username: ")
        existing_user = session.query(User).filter_by(username=username).first()
        
        if existing_user:
            print("❌ Username already exists. Try a different one.")
            return

        password = getpass("Enter your password: ")
        confirm_password = getpass("Confirm your password: ")
        
        if password != confirm_password:
            print("❌ Passwords do not match. Try again.")
            return
        
        name = input("Enter your full name: ")
        age = int(input("Enter your age: "))
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        gender = input("Enter your gender (Male/Female): ").strip().capitalize()

        # Validate gender input
        if gender not in ["Male", "Female"]:
            print("❌ Invalid input. Please enter Male or Female.")
            return

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create a new user object
        new_user = User(
            username=username,
            password_hash=hashed_password,  # Save the hashed password
            name=name,
            age=age,
            gender=gender,                   # Save the gender
            weight=weight,
            height=height,
        )

        # Save to the database
        session.add(new_user)
        session.commit()
        print(f"✅ User {username} created successfully!")
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error creating user: {e}")
    finally:
        session.close()

def verify_password(username, password):
    session = Session()
    try:
        user = session.query(User).filter_by(username=username).first()
        if not user:
            print("❌ User not found.")
            return None
        
        # Debug: Print to check if hash exists
        print(f"🔑 Stored Hash: {user.password_hash}")

        # Check the password hash
        if check_password_hash(user.password_hash, password):
            print("✅ Password matched!")
            return user
        else:
            print("❌ Password mismatch.")
            return None
    finally:
        session.close()

def calculate_calories_and_protein(weight, height, age, gender, activity_level):
    if gender.lower() == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    activity_multiplier = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "heavy": 1.725,
        "athlete": 1.9,
    }

    tdee = bmr * activity_multiplier.get(activity_level.lower(), 1.2)
    protein_min = weight * 1.6
    protein_max = weight * 2.2

    return tdee, protein_min, protein_max


# to login 
def login():
    print(" Welcome to the Login Portal!")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")  # Hides the password input

    if verify_password(username, password):
        print("Access granted! You can now use the application.")
        return username
    else:
        print("Access denied. Please try again.")





if __name__ == "__main__":
    create_user()

    login()






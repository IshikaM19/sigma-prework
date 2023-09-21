from datetime import datetime 


birthday = input("Enter your Birthday in the format DD-MM-YYYY: " )

def calculate_age(birthday):
    today = datetime.today()
    birthday = datetime.strptime(birthday, "%d-%m-%Y")
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.year))
    return age 

age = calculate_age(birthday)

print(f"You're {age} years old!")
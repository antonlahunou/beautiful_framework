from faker import Faker

fake = Faker()

def generate_random_user_data() -> dict:
    return {
        "name": fake.first_name(),
        "email": fake.email(),
        "gender": fake.random_element(elements=("male", "female")),
        "status": fake.random_element(elements=("active", "inactive"))
    }
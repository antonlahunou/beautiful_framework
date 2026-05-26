from faker import Faker

fake = Faker()

def generate_random_post_data() -> dict:
    return {
        "body": fake.text()
    }
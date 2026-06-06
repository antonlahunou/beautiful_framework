from faker import Faker

fake = Faker()

bird_species = [
    "Parus major",
    "Fringilla coelebs",
    "Erithacus rubecula",
    "Turdus merula",
    "Cyanistes caeruleus",
    "Sturnus vulgaris",
    "Columba palumbus",
    "Pica pica",
    "Corvus monedula"
]

def generate_random_bird_data() -> dict:
    return {
        "device_id": fake.bothify(text='device-???-###'),
        "detection_type": fake.random_element(elements=("audio", "video")),
        "species": fake.random_element(elements=bird_species),
        "confidence": round(fake.pyfloat(min_value=0.5, max_value=1.0), 2),
        "photo_url": fake.image_url(),
        "audio_url": fake.url(),
        "location_lat": float(fake.latitude()),
        "location_lon": float(fake.longitude())
    }
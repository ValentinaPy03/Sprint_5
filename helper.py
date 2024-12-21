from faker import Faker
from faker.contrib.pytest.plugin import faker

faker = Faker()

def generate_registration_data():
    email = faker.email()
    password = faker.password(7, True, True, True, True)
    return email, password

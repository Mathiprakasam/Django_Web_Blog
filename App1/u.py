from faker import Faker

fake = Faker()

print(fake.name())       # Generates a random name
print(fake.address())    # Generates a random address
print(fake.email())      # Generates a random email
print(fake.text())       # Generates random text

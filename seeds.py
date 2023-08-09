from models import Owner, Pet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from faker import Faker
fake = Faker()

print("🌱 Seeding DB...")

engine = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Owner).delete()
session.query(Pet).delete()


owners = [
    Owner(username="BugsBunnyFanatic", email="bugs@me.com"),
    Owner(username="WackyDaffy91", email="daffy@me.com"),
    Owner(username="WackyDaffy913", email="fake_daffy@me.com"),
    Owner(username="TazmanianTornado22", email="taz@me.com"),
    Owner(username="SylvesterSneakyCat", email="sufferin_succotash@me.com"),
    Owner(username="RoadRunnerSpeedster", email="later_loser@me.com"),
]

session.bulk_save_objects(owners)

db_owners = session.query(Owner).all()

# Add owner_id to pets
for owner in db_owners:
    pets = [Pet(name=fake.first_name(), species="Cat", breed="Unknown", age=random.randrange(2, 20), color=fake.color_name(), weight=random.random() * 50) for _ in range(2)]
    session.bulk_save_objects(pets)

session.commit()
print("✅ Done seeding!")

import ipdb; ipdb.set_trace()
#!/usr/bin/env python3

from app import db, User

def seed_database():
    db.create_all()

    # Create a test user with username "stephan maina" and password "Liverpool fc"
    user = User(username="stephan maina")
    user.set_password("Liverpool fc")

    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    seed_database()

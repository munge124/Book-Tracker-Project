from lib.connection import session
from lib.models.user import User

def create_user(name):
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User '{name}' created.")

def list_users():
    users = session.query(User).all()
    for user in users:
        print(f"{user.id}: {user.name}")

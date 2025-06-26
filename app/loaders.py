from strawberry.dataloader import Dataloader
from app.models import User
from app.database import SessionLocal

def load_users(keys: list[int]) -> list[User]:
    db = SessionLocal()
    users = db.query(User).filter(User.id.in_(keys)).all()
    user_map = {user.id: user for user in users}
    db.close()
    return [user_map.get(key) for key in keys]
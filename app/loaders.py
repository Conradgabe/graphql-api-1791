from strawberry.dataloader import Dataloader
from app.models import User
from app.database import SessionLocal

# -----------------------------------------------
# Batch loader function for users
# This function is designed to be used with Strawberry's DataLoader.
# It fetches all users whose IDs are in the 'keys' list,
# and returns them in the same order as the keys.
# -----------------------------------------------
def load_users(keys: list[int]) -> list[User]:
    # Create a new database session
    db = SessionLocal()

    # Fetch all users with IDs in the provided keys
    users = db.query(User).filter(User.id.in_(keys)).all()

    # Map users by their ID for quick lookup
    user_map = {user.id: user for user in users}

    # Close the session to avoid leaks
    db.close()

    # Return users in the same order as keys
    # If a key has no corresponding user, None is returned
    return [user_map.get(key) for key in keys]

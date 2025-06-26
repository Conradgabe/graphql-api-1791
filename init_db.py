from app.database import engine, SessionLocal
from app.models import Base, User, Post

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    user1 = User(name="Alice", email="alice@example.com")
    user2 = User(name="Bob", email="bob@example.com")
    db.add_all([user1, user2])
    db.commit()

    post1 = Post(title="First Post", content="Hello GraphQL", author_id=user1.id)
    post2 = Post(title="Second Post", content="With FastAPI", author_id=user2.id)
    db.add_all([post1, post2])
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()

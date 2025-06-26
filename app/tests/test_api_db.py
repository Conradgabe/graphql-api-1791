import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from app.models import User, Post

client = TestClient(app)

# Create a fresh in-memory DB for testing
@pytest.fixture(autouse=True)
def setup_and_teardown():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Seed one user for post creation tests
    db = SessionLocal()
    user = User(name="Test User", email="test@example.com")
    db.add(user)
    db.commit()
    db.refresh(user)
    post = Post(title="Initial Post", content="First post content", author_id=user.id)
    db.add(post)
    db.commit()
    db.close()

    yield

    Base.metadata.drop_all(bind=engine)

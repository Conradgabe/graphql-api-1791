# 🧠 GraphQL API – Apollo Server with FastAPI Backend

This is a sample GraphQL API built with **FastAPI** and **Strawberry GraphQL**, demonstrating robust schema design, input validation, optimized data loading, and playground integration.

## 📌 Objective

Build a clean and scalable GraphQL API that supports:

- Schema-first design
- Queries and mutations
- Input validation with Pydantic
- DataLoader for optimisation
- GraphQL Playground for testing

---

## ⚙️ Tech Stack

| Component       | Technology                |
|----------------|---------------------------|
| Backend         | FastAPI                   |
| GraphQL Server  | Strawberry (Apollo Compatible) |
| Database        | SQLite (via SQLAlchemy)   |
| ORM             | SQLAlchemy                |
| Validation      | Pydantic                  |
| Loader Pattern  | Strawberry Dataloader     |
| Playground      | GraphQL at `/graphql`     |

---

## 🚀 Getting Started

### 📦 Installation

```git clone https://github.com/conradgabe/graphql-api-1791.git```

```cd graphql-api-1791```

```python -m venv venv```

```source venv/bin/activate  # or `venv\Scripts\activate` on Windows```

```pip install -r requirements.txt```

### ⚙️ Configuration
``` DATABASE_URL=sqlite:///./test.db ```

### 🛠️ Initialize & Seed the Database
``` python app/init_db.py ```

### 🔄 Run the API
``` uvicorn app.main:app --reload ```

## 🔍 GraphQL Playground
### ✅ Open GraphQL Playground

`http://127.0.0.1:8000/graphql`

### 📄 Example Query
```
query GetAllPosts {
  posts {
    id
    title
    author {
      name
      email
    }
  }
}
```

### ✍️ Example Mutation
```
mutation CreatePost {
  createPost(title: "GraphQL with FastAPI", content: "Learning is fun", authorId: 1) {
    id
    title
    author {
      name
    }
  }
}
```
## More examples are in examples/queries.graphql and examples/mutations.graphql.

### 🧱 Project Structure
```
graphql-api-project/
├── app/
│   ├── main.py                  # FastAPI app entry
│   ├── schema.py                # GraphQL schema definition
│   ├── models.py                # SQLAlchemy models
│   ├── database.py              # DB setup and session
│   ├── init_db.py               # DB seeding script
│   ├── loaders.py               # Dataloader pattern
│   ├── types/                   # Strawberry types
|   ├── tests/                  # Tests for Endpoint
│   └── resolvers/              # Query and mutation logic
├── examples/                   # Playground queries/mutations
├── requirements.txt
├── .env
└── README.md
```

### ✅ Features
- 📐 Well-defined schema using Strawberry GraphQL
- 🔁 DataLoader-ready structure for resolving N+1 issues
- 🧪 Input validation via Pydantic
- 🧵 Modular code (types, resolvers, models, config)
- 🧑‍💻 Developer-friendly GraphQL Playground
- 📘 Clear documentation & examples

### 📤Submission
GitHub Repository: [https://www.github:com/conradgabe/graphql-api-1791](https://github.com/Conradgabe/graphql-api-1791)

### 📩 Contact
For inquiries or technical questions, feel free to reach out via the repo issues or gisuekebho5880@gmail.com.


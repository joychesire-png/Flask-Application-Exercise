Build a minimal Flask application that demonstrates a One-to-Many relationship and uses the SQLAlchemy-Serializer mixin to automate the JSON conversion process.

---

### Part 1: Discussion & Design

Before coding, discuss the following as a group:

1. The Mixin: How does SerializerMixin differ from manually creating a to_dict() method?
2. Recursion Depth: When using serialize_rules, how do we prevent the "infinite loop" (User → Post → User → Post)?
3. Cascading: If a User is deleted, should their Posts be deleted automatically (cascade="all, delete-orphan")?

---

### Part 2: The Implementation Task

Build a single-file Flask app (app.py) that meets these requirements:

1. Models:

- User: id, name.
- Post: id, title, content, user_id.
- Setup: Both models must inherit from SerializerMixin.

2. Serialization Rules:

- Configure the User model to include their posts when serialized.
- Use -posts.user in the serialize_rules to prevent recursion.

3. Routes:

- GET /users: Returns a list of all users and their associated posts in JSON format.
- POST /users: Add a new user to the database.

---

Once the app is running, try to add a Many-to-Many relationship (e.g., Tags for Posts). How do the serialize_rules change when you have a bridge/association table in the middle?

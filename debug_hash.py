from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
password = "testpassword123"
hashed = pwd_context.hash(password)
print(f"Hashed: {hashed}")
assert pwd_context.verify(password, hashed)
print("Success!")

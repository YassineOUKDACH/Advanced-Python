from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pydantic import BaseModel


app = FastAPI()

# Secret key used to sign the token
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Fake user
fake_user = {
    "username": "amine",
    "password": "1234"
}

# Request body for login
class LoginData(BaseModel):
    username: str
    password: str

# Function to create token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Login route
@app.post("/login")
def login(data: LoginData):
    if data.username != fake_user["username"] or data.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": data.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# JWT security scheme
security = HTTPBearer()

# Dependency to verify token
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# Protected route
@app.get("/profile")
def get_profile(username: str = Depends(verify_token)):
    return {
        "message": "Protected route accessed successfully",
        "username": username
    }

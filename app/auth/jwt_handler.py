import time
import jwt
from dotenv import load_dotenv
import os
load_dotenv()

JWT_SECRET = os.getenv("secret")
JWT_ALGORITHM = os.getenv("algorithm")


def token_response(token: str):
    return {
        "access token": token
    }

JWT_EXPIRATION_SECONDS = 3600  # 1 hour

def signJWT(email: str) -> str:
    payload = {
        "email": email,
        "exp": int(time.time()) + JWT_EXPIRATION_SECONDS
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def decodeJWT(token: str):
    try:
        token = token.split(" ")[1]
        print(token)
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if 'exp' in decode_token and 'email' in decode_token:
            # check if iat and exp are valid
            if decode_token['exp'] >= int(time.time()):
                print("Token is valid")
                return True
        else:
            return None
    except Exception as e:
        print(e)
        return None
from fastapi import HTTPException, status
import secrets


key1 = secrets.token_urlsafe(32)

print("================================")
print("Generated Secret API Key:")
print(key1)
print("================================")


def verify_secret_key(api_key: str):

    if api_key != key1:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid secret API key"
        )

    return True
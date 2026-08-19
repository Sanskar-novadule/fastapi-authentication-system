from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/oauth/login"
)


OAUTH_DEMO_TOKEN = "oauth-demo-token"


def verify_oauth_token(token: str):

    if token != OAUTH_DEMO_TOKEN:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid OAuth2 token",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    return "sanskar"
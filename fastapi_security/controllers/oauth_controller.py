from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from auth.oauth_auth import (
    oauth2_scheme,
    verify_oauth_token
)


router = APIRouter(
    prefix="/oauth",
    tags=["OAuth2 Authentication"]
)


items = [
    {
        "id": 1,
        "name": "Keyboard",
        "price": 2500
    },
    {
        "id": 2,
        "name": "Monitor",
        "price": 15000
    }
]


# -------------------------
# LOGIN
# -------------------------

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    if (
        form_data.username != "sanskar"
        or form_data.password != "123456"
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return {
        "access_token": "oauth-demo-token",
        "token_type": "bearer"
    }


# -------------------------
# PROTECTED
# -------------------------

@router.get("/protected")
def protected(
    token: str = Depends(oauth2_scheme)
):

    username = verify_oauth_token(token)

    return {
        "message": "OAuth2 authentication successful",
        "username": username
    }


# -------------------------
# CREATE
# -------------------------

@router.post("/items")
def create_item(
    name: str,
    price: float,
    token: str = Depends(oauth2_scheme)
):

    verify_oauth_token(token)

    new_id = len(items) + 1

    item = {
        "id": new_id,
        "name": name,
        "price": price
    }

    items.append(item)

    return {
        "message": "Item created successfully",
        "item": item
    }


# -------------------------
# GET
# -------------------------

@router.get("/items")
def get_items(
    token: str = Depends(oauth2_scheme)
):

    verify_oauth_token(token)

    return {
        "items": items
    }


# -------------------------
# UPDATE
# -------------------------

@router.put("/items/{item_id}")
def update_item(
    item_id: int,
    name: str,
    price: float,
    token: str = Depends(oauth2_scheme)
):

    verify_oauth_token(token)

    for item in items:

        if item["id"] == item_id:

            item["name"] = name
            item["price"] = price

            return {
                "message": "Item updated successfully",
                "item": item
            }

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )


# -------------------------
# DELETE
# -------------------------

@router.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    token: str = Depends(oauth2_scheme)
):

    verify_oauth_token(token)

    for item in items:

        if item["id"] == item_id:

            items.remove(item)

            return {
                "message": "Item deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )
from fastapi import APIRouter, Header, HTTPException

from auth.secret_key_auth import verify_secret_key


router = APIRouter(
    prefix="/secret",
    tags=["Secret Key Authentication"]
)


items = [
    {
        "id": 1,
        "name": "Phone",
        "price": 30000
    },
    {
        "id": 2,
        "name": "Headphones",
        "price": 5000
    }
]


def authenticate(x_api_key: str):

    verify_secret_key(x_api_key)


# -------------------------
# PROTECTED
# -------------------------

@router.get("/protected")
def protected(
    x_api_key: str = Header(...)
):

    authenticate(x_api_key)

    return {
        "message": "Secret key authentication successful"
    }


# -------------------------
# CREATE
# -------------------------

@router.post("/items")
def create_item(
    name: str,
    price: float,
    x_api_key: str = Header(...)
):

    authenticate(x_api_key)

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
    x_api_key: str = Header(...)
):

    authenticate(x_api_key)

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
    x_api_key: str = Header(...)
):

    authenticate(x_api_key)

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
    x_api_key: str = Header(...)
):

    authenticate(x_api_key)

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
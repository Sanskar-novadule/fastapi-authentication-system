from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import (
    OAuth2PasswordRequestForm,
    HTTPAuthorizationCredentials
)

from utils.logger import logger

from auth.jwt_auth import (
    create_access_token,
    security,
    verify_token
)


router = APIRouter(
    prefix="/jwt",
    tags=["JWT Authentication"]
)


# ============================================================
# TEMPORARY DATA
# ============================================================

items = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 70000
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 1500
    }
]


# ============================================================
# LOGIN
# ============================================================

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    username = form_data.username

    logger.info(
        f"Login attempt for user: {username}"
    )

    # Temporary username/password
    if (
        username != "sanskar"
        or form_data.password != "123456"
    ):

        logger.warning(
            f"Login failed for user: {username}"
        )

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Create JWT
    token = create_access_token(username)

    logger.info(
        f"Login successful for user: {username}"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ============================================================
# PROTECTED ROUTE
# ============================================================

@router.get("/protected")
def protected(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    logger.info(
        "Protected route accessed"
    )

    # Extract token
    token = credentials.credentials

    # Verify JWT
    username = verify_token(token)

    logger.info(
        f"Protected route authorized for user: {username}"
    )

    return {
        "message": "JWT authentication successful",
        "username": username
    }


# ============================================================
# CREATE ITEM
# ============================================================

@router.post("/items")
def create_item(
    name: str,
    price: float,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    logger.info(
        f"Create item request: {name}"
    )

    # Extract token
    token = credentials.credentials

    # Verify token
    username = verify_token(token)

    logger.info(
        f"Create item authorized for user: {username}"
    )

    # Generate new ID
    new_id = max(
        [item["id"] for item in items],
        default=0
    ) + 1

    # Create item
    item = {
        "id": new_id,
        "name": name,
        "price": price
    }

    items.append(item)

    logger.info(
        f"Item created successfully: id={new_id}, name={name}"
    )

    return {
        "message": "Item created successfully",
        "item": item
    }


# ============================================================
# GET ALL ITEMS
# ============================================================

@router.get("/items")
def get_items(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    logger.info(
        "Get all items request"
    )

    # Extract token
    token = credentials.credentials

    # Verify token
    username = verify_token(token)

    logger.info(
        f"Get items authorized for user: {username}"
    )

    return {
        "items": items
    }


# ============================================================
# UPDATE ITEM
# ============================================================

@router.put("/items/{item_id}")
def update_item(
    item_id: int,
    name: str,
    price: float,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    logger.info(
        f"Update item request: id={item_id}"
    )

    # Extract token
    token = credentials.credentials

    # Verify token
    username = verify_token(token)

    logger.info(
        f"Update item authorized for user: {username}"
    )

    # Find item
    for item in items:

        if item["id"] == item_id:

            item["name"] = name
            item["price"] = price

            logger.info(
                f"Item updated successfully: id={item_id}"
            )

            return {
                "message": "Item updated successfully",
                "item": item
            }

    logger.warning(
        f"Item not found: id={item_id}"
    )

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )


# ============================================================
# DELETE ITEM
# ============================================================

@router.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    logger.info(
        f"Delete item request: id={item_id}"
    )

    # Extract token
    token = credentials.credentials

    # Verify token
    username = verify_token(token)

    logger.info(
        f"Delete item authorized for user: {username}"
    )

    # Find item
    for item in items:

        if item["id"] == item_id:

            items.remove(item)

            logger.info(
                f"Item deleted successfully: id={item_id}"
            )

            return {
                "message": "Item deleted successfully"
            }

    logger.warning(
        f"Item not found for deletion: id={item_id}"
    )

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )
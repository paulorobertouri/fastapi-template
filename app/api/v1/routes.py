from fastapi import APIRouter, Depends, Response

from app.api.deps import get_auth_service, get_customer_service, require_token
from app.services.auth_service import AuthService
from app.services.customer_service import CustomerService

router = APIRouter()


@router.get("/customer")
def list_customers(
    service: CustomerService = Depends(get_customer_service),
) -> list[dict]:
    return [customer.model_dump() for customer in service.list_customers()]


@router.get("/auth/login")
def login(
    response: Response,
    auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    token = auth_service.issue_token(subject="demo-user")
    response.headers["Authorization"] = f"Bearer {token}"
    response.headers["X-JWT-Token"] = token
    return {"token": token}


@router.get("/public")
def public() -> dict:
    return {"message": "public endpoint"}


@router.get("/private")
def private(token_payload: dict = Depends(require_token)) -> dict:
    return {"message": "private endpoint", "subject": token_payload.get("sub")}

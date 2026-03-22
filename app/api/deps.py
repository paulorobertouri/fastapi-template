from functools import lru_cache

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.repositories.customer_repository import InMemoryCustomerRepository
from app.services.auth_service import AuthService
from app.services.customer_service import CustomerService

_security = HTTPBearer(bearerFormat="JWT")


@lru_cache
def get_customer_service() -> CustomerService:
    return CustomerService(repository=InMemoryCustomerRepository())


@lru_cache
def get_auth_service() -> AuthService:
    return AuthService()


def require_token(
    credentials: HTTPAuthorizationCredentials = Depends(_security),
    auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    try:
        return auth_service.decode_token(credentials.credentials)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        ) from exc

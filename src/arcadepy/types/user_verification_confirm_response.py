from .._models import BaseModel

__all__ = ["UserVerificationConfirmResponse"]


class UserVerificationConfirmResponse(BaseModel):
    auth_id: str
    next_uri: str | None

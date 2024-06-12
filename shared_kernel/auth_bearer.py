
from fastapi import Depends, HTTPException 
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from shared_kernel.auth_handler import decode_jwt


security = HTTPBearer()


async def has_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = decode_jwt(token)
    except Exception:
        raise HTTPException(status_code=403, detail='Error validating auth token')

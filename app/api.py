from fastapi import Depends, FastAPI 

from app import auth, sales
from shared_kernel.auth_bearer import has_access

app = FastAPI()
protected = Depends(has_access)


@app.get('/')
def home():
    return {'message": "Go to /docs to see documentation'}

app.include_router(
    auth.router,
    prefix='/auth'
)

app.include_router(
    sales.router,
    prefix='/sales',
    dependencies=[protected]
)

from fastapi import APIRouter


router = APIRouter()


@router.get('/by_employee')
def sales_by_employee():
    return []

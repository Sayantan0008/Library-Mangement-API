from fastapi import APIRouter

router = APIRouter()

@router.post("/borrow")
async def borrow_book(borrow_record: dict):
    return {"message": "Book borrowed", "borrow_record": borrow_record}

@router.put("/return/{id}")
async def return_book(id: int):
    return {"message": "Book returned", "id": id}

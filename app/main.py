from fastapi import FastAPI
from app.routes import book_routes, user_routes, borrow_routes

app = FastAPI()

app.include_router(book_routes.router)
app.include_router(user_routes.router)
app.include_router(borrow_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management System API"}

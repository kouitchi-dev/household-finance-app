

from fastapi import APIRouter,Depends,HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session
import crud
import schemas
import auth
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends





router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users")
async def create_user_endpoint(user:schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db,user)


@router.get("/users/{user_id}")
async def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return crud.get_users(db,user_id)


@router.patch("/users/{user_id}")
async def update_user_endpoint(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db,user,user_id)

@router.delete("/users/{user_id}")
async def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db,user_id)
    return {"message":"deleted"}



@router.post("/login")
async def login_user_endpoint(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db,form_data.username)

    if not db_user:
        raise HTTPException(status_code=401, detail="ユーザーが存在しません")
    
    if not auth.verify_password(form_data.password,db_user.password):
        raise HTTPException(status_code=401, detail="パスワードが一致しません")

    token = auth.create_access_token({"sub":db_user.email})
    return {"access_token": token, "token_type": "bearer"}
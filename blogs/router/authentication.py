from fastapi import APIRouter, Depends, status, HTTPException
from .. import jwt_token, schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    if not Hash.verify(user.password, request.password):
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect password")
    access_token = jwt_token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


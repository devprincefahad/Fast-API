from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title= request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        blog.delete(synchronize_session=False)
    db.commit()
    return {'Deleted successfully'}

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        blog.update({
        "title": request.title,
        "body": request.body
    })
    db.commit()
    return 'update'

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Blog with {id} is not available.")
        #  response.status_code = status.HTTP_404_NOT_FOUND
        #  return {'detail': f'Blog with {id} is not available.'}
    return blog
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get('/blog?limit=10')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/{id}/commnets')
def comments(id, limit = 10):
    return {'data': {'1', '2'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with tile as {blog.title}'}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Post(BaseModel):
    id: int
    title: str
    content: str


posts_db = []


@app.post("/posts/", response_model=Post)
def create_post(post: Post):
    posts_db.append(post)
    return post


@app.get("/posts/", response_model=List[Post])
def get_posts():
    return posts_db


@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post: Post):
    for index, existing_post in enumerate(posts_db):
        if existing_post.id == post_id:
            posts_db[index] = post
            return post
    raise HTTPException(status_code=404, detail="Post não encontrado")


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for index, existing_post in enumerate(posts_db):
        if existing_post.id == post_id:
            del posts_db[index]
            return {"message": "Post deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Post não encontrado")

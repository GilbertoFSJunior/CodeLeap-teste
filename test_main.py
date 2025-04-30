from fastapi.testclient import TestClient
from main import app  # Certifique-se de salvar o backend como `main.py`

client = TestClient(app)

def test_create_post():
    response = client.post("/posts/", json={"id": 1, "title": "Título Teste", "content": "Conteúdo Teste"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Título Teste", "content": "Conteúdo Teste"}

def test_get_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_post():
    response = client.put("/posts/1", json={"id": 1, "title": "Título Atualizado", "content": "Novo Conteúdo"})
    assert response.status_code == 200
    assert response.json()["title"] == "Título Atualizado"

def test_delete_post():
    response = client.delete("/posts/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Post deletado com sucesso"
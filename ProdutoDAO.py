from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()


class Produto(BaseModel):
    id: int = None
    nome: str
    preco: float
    qtd: int
    descricao: str = None
    
# Criar os endpoints de Produto: GET, POST, PUT, DELETE
@router.get("/produto/{id}", tags=["produto"])
def get_produto(id: int):
    return {"msg": "get executado"}, 200

@router.post("/produto/{id}", tags=["produto"])
def post_produto(id: int, f: Produto):
    return {"msg": "post executado", "id": id, "nome" : f.nome, "preco" : f.preco, "qtd" : f.qtd, "descricao" : f.descricao}, 200

@router.put("/produto/{id}", tags=["produto"])
def put_produto(id: int, f: Produto):
    return {"msg": "put executado", "id": id, "nome" : f.nome, "preco" : f.preco, "qtd" : f.qtd, "descricao" : f.descricao}, 201

@router.delete("/produto/{id}", tags=["produto"])
def delete_produto(id: int):
    return {"msg": "delete executado"}, 201
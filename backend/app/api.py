from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.sec.query_edgar import query_edgar
from ../sec import query_edgar

app = FastAPI()

origins = ["http://localhost:3000", "localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Default route for api"}


@app.get("/sec")
async def read_doc() -> dict:
    return {
        "documentName": "Document content asjdfkajskfdl;jsdkfl;ajkfl;dsajkfl;asjkl;f"
    }

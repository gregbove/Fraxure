# api
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# sec
import backend.sec

# tagtog

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


@app.get("/sec/{document_id}")
async def get_sec_doc(document_id) -> dict:
    return sec.query_edgar(docuement_id)

@app.get("/tagtog/{document_id}")
async def get_tagtog_doc() -> dict:
    return tagtog.get_document(document_id)

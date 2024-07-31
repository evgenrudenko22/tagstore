from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random

app = FastAPI()

@app.get("/items")
def get_items():
    items = [
        {
            "id": 1,
            "name": "Capibara"
        },
        {
            "id": 2,
            "name": "Sniffer"
        }
    ]

    random.shuffle(items)
    return items

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://185.198.165.177"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
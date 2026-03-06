from fastapi import FastAPI

app = FastAPI(title="DevOps Poke-API")

@app.get("/")
def home():
    return {"message": "Bienvenido a mi API de Portfolio", "status": "Online"}

@app.get("/pokemon/{name}")
def get_pokemon(name: str):
    # En un paso futuro, aquí conectaremos con la PokéAPI real
    return {
        "pokemon": name,
        "type": "Fire",
        "owner": "Cris",
        "environment": "Azure-Ready"
    }
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ghost_functions.generate_info import GenerateGhost
from ghost_functions.image_generation import *
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/info/ghost")
def getGhostInfo():
    ghost = GenerateGhost()
    response = ghost.full_info()
    if response:
        return response
    raise HTTPException(404, f"0")

@app.get("/api/info/{ghost}/image")
def getImage(ghost):
    ghost = GenerateGhost()
    ghost_image = ImageProcessing("3.png")
    ghost_image.invert_image()
    ghost_image.apply_filter(ghost.ghost_rarity)

    response = ghost_image.save_image()
    if response:
        return response
    raise HTTPException(404, f"0")

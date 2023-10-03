
from fastapi import FastAPI
from fastapi.responses import FileResponse
from PIL import Image, ImageDraw
from uuid import uuid4

import random
import math

## generate random rgb values
def generate_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    
## generate the avatar image
def generate_avatar_image():
    bg_color = generate_random_color()
    image = Image.new(mode = 'RGB', size = (200, 200), color = bg_color)
    
    ## draw on image
    avatar_image = ImageDraw.Draw(image)
    
    n = random.randint(50, 70)
    eye_x = n
    eye_y = n
    
    ## draw eyes
    avatar_image.arc(
        (eye_x, eye_y, eye_x + 10, eye_y + 10),
        start = math.pi / 2,
        end = 1,
        width = 50,
        fill='black'
    )
    
    
    avatar_image.arc(
        (eye_x + 80, eye_y, eye_x + 90, eye_y + 10),
        start = math.pi / 2,
        end = 1,
        width = 50,
        fill='black'
    )
    
    
    avatar_image.arc(
        (90, 100,  random.randint(100, 130), random.randint(110, 130)),
        start = math.pi / 2,
        end = 1,
        width = 50,
        fill='black'
    )
    
    avatar_path =  f'images/{str(uuid4())}.jpg'
    image.save(avatar_path)
    return avatar_path


app = FastAPI()

@app.get('/')
def home():
    return {'msg': 'welcome'}

@app.get('/random')
def generate_random_avatar():
    return FileResponse(generate_avatar_image())

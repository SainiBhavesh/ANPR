from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.anpr import anpr
from app.details import details
from app.util import NMS


app=FastAPI()

@app.get('/')
def welcomeHomePage():
    return "Welcome to our ANPR System"

@app.get('/details')
def generate():
    details()
    return "List of Number Plates"


@app.post("/upload")
async def upload_image(image: UploadFile = File(...)):
    # Save the uploaded file to a directory
    # Modify the path 'uploads/' to your desired directory
    with open('C:\\Users\\Bhavesh Saini\\Desktop\\ANPR\\upload' + image.filename, 'wb') as f:
        f.write(await image.read())

    # Return the image directory as a response
    anpr('C:\\Users\\Bhavesh Saini\\Desktop\\ANPR\\upload\\' + image.filename)
    return {'image_directory': 'C:\\Users\\Bhavesh Saini\\Desktop\\upload\\' +image.filename}
    
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from flask import Flask, request, send_file
from flask_cors import CORS
from algorithms.random_image_generator import random_generator
from utils.helpers import open_image
import io

app = Flask(__name__)
CORS(app)  # enable CORS for all routes so I don't see an error when sending requests to backend


@app.route("/generate", methods=['POST'])
def generate_new_image():

    # destructure image property from the request object 
    uploaded_file = request.files["image"]
    # open image inside of PIL so that it is accessible to library
    image = open_image(uploaded_file)

    # make modifications to image
    processed_image = random_generator(image)

    # creates an in-memory binary stream that temporarily creates an object in RAM that acts like one stored on the disk
    img_io = io.BytesIO()
    # save processed image
    processed_image.save(img_io, format="PNG")

    # reset pointer to start of the file
    img_io.seek(0) 

    # send processed image back to frontend
    return send_file(img_io, mimetype="image/png")

    # pseudo-code/thoughts
    # # in order to view results of the function, you must save them in a variable 
    # image1 = open_image(request.image or whatever i need to access)
    # image2 = random_generator(image1)
    # return result to front-end


if __name__ == "__main__":
    app.run(debug=True)
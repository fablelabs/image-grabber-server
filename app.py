from flask import Flask, send_file
from flask_cors import CORS
from PIL import Image

import io
import statistics

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/solarize/test")
def solarize_test():
    img = Image.open("test.jpg")

    # Get pixels from our test image
    pixels = list(img.getdata())
    newPixels = []
    for pixel in pixels:
        # Figuring out if we turn a pixel black or not
        if statistics.mean(pixel) <= 128:
            newPixel = (0, 0, 0)
        else:
            newPixel = (255, 255, 255)
        newPixels.append(newPixel)

    # Create a image and put data into it
    newImg = Image.new(img.mode, img.size)
    newImg.putdata(newPixels)

    # Create file-object in memory and write to it
    file_object = io.BytesIO()
    newImg.save(file_object, "png")
    file_object.seek(0)

    # Sends back image data
    return send_file(file_object, mimetype="image/png")


@app.route("/solarize")
def solarize_image():
    """
    You will design the parameter request here to work injunction with the client side.

    This endpoint should:
      - Get an image URL from the API request.
      - Perform the logic to solarize an image.
      - Return the final result to the client.

    See above example in solarize_test() to see the logic for handling that process.
    """

    return ""


from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    # getting the image data
    image_data = request.form['image_data']
    # converting classified data into json module using jsonify
    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Woman Cricketers Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
from flask import Flask, request, jsonify
from app.mmf.mmf.models.qlarifais import Qlarifais
import torch
import numpy as np

# MobilenetV2 might have to be changed fromt torch.ao to torch

app = Flask(__name__)

def allowed_image(filename):
    return filename.split(".")[-1].lower() in ['png', 'jpg', 'jpeg']

def load_model():
    model = Qlarifais.from_pretrained('/mmf/save/models/ama_opt')
    model.to("cpu") # needed for heroku
    return model

@app.route('/predict', methods=['POST'])
def predict():
    # 1 load image (and string)
    # preprrocess image - probably just use Alberts already createdd
    # 3 predict
    # 4 return json


    if request.method == 'POST':

        # Either a URL a path or a PIL.Image.Image object
        #image = request.files['image'].read()

        # Loading imageURL
        image = request.files['URL'].read().decode('UTF-8')

        # Loading question
        question = request.files['question'].read().decode('UTF-8')

        """
        Not needed unless actual image is passed!
        if image is None or image.filename == "":
            return jsonify({'error': 'no file'})

        if not allowed_image(image.filename):
            return jsonify({'error': 'format not supported'})"""
        try:
            # both obv. shouldn't be file.read, however will be updated later.
            top_k = 5

            model = load_model()

            # outputs is (probs, answers)
            outputs = model.classify(image=image, text=question, top_k=top_k)

            # Probably shouldn't print - but for now:
            for i, (prob, answer) in enumerate(zip(*outputs)):
                print(f"{i + 1}) {answer} \t ({prob})")

            #return jsonify({'prediction': outputs})
            return jsonify({'q': question, 'URL': image, 'answer': answer})#, 'q': question, 'topk': top_k})

        except:
            return jsonify({'error': 'error during prediction'})
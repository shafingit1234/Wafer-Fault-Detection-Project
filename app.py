import os
import sys


from src.logger import logs_path, LOG_FILE
from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
from src.pipeline.training_pipeline import TrainingPipeline
from src.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)


@app.route("/")
def home():
    # return jsonify("home")
    # return "<h1>Welcome to Home page</h1>"
    return render_template('index.html')


@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()

        # return "Training Completed."
        return render_template('success.html')

    except Exception as e:
        raise CustomException(e, sys)


@app.route('/predict', methods=['POST', 'GET'])
def upload():

    try:

        if request.method == 'POST':
            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail = prediction_pipeline.run_pipeline()

            lg.info("prediction completed. Downloading prediction file.")
            return send_file(prediction_file_detail.prediction_file_path,
                             download_name=prediction_file_detail.prediction_file_name,
                             as_attachment=True)

        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e, sys)


@app.route('/logged')
def training_logger():
    try:

        LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
        log_contents = []

        with open(LOG_FILE_PATH, 'r') as file:
            logs = file.readlines()
            filtered_logs = [log for log in logs if 'root' in log]
            log_contents.extend(filtered_logs)

        return render_template('logs.html', logs=log_contents)
    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

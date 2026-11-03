from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    else:
        return f"For the given statement, the system response is 'anger': {str(response['anger'])}, 'disgust': {str(response['disgust'])}, 'fear': {str(response['fear'])}, 'joy': {str(response['joy'])} and 'sadness': {str(response['sadness'])}. The dominant emotion is {str(response['dominant_emotion'])}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

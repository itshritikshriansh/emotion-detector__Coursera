from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask('Emotion Detection using Watson NLP library')

@app.route("/")
def emotionDetector():
    text = request.args.get('textToAnalyze')
    emotion_val = emotion_detector(text)

    final_output = f"For the given statement, the system response is 'anger': {emotion_val['anger']}, 'disgust': {emotion_val['disgust']}, 'fear': {emotion_val['fear']}, 'joy': {emotion_val['joy']}, 'sadness': {emotion_val['sadness']}. The dominant emotion is: {emotion_val['dominant_emotion']}"

    return final_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    object =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = object, headers = header)
    
    formatted_response = response.json()
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    max_val = max(anger, disgust, fear, joy, sadness)

    if max_val == anger:
        dominant_emotion = 'anger'
    
    elif max_val == disgust:
        dominant_emotion = 'disgust'

    elif max_val == fear:
        dominant_emotion = 'fear'

    elif max_val == joy:
        dominant_emotion = 'joy'
    
    else:
        dominant_emotion = 'sadness'
    
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}

import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion_response = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']
    anger_score = emotion_response['anger']
    disgust_score = emotion_response['disgust']
    fear_score = emotion_response['fear']
    joy_score = emotion_response['joy']
    sadness_score = emotion_response['sadness']
    match max(anger_score, disgust_score, fear_score, joy_score, sadness_score):
        case x if x == anger_score:
            dominant_emotion = 'anger'
        case x if x ==  disgust_score:
            dominant_emotion = 'disgust'
        case x if x ==  fear_score:
            dominant_emotion = 'fear'
        case x if x ==  joy_score:
            dominant_emotion = 'joy'
        case x if x ==  sadness_score:
            dominant_emotion = 'sadness'
        case _:
            dominant_emotion = 'UNDEFINED'
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }
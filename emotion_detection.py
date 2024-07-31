import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers= headers)
    response_json = json.loads(response.text)
    emotions = response_json['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    max_score = 0
    max_emotion = None
    for emotion, emotion_score in zip(list(emotions.keys()), list(emotions.values())):
        if emotion_score > max_score:
            max_score = emotion_score
            max_emotion = emotion
    emotions['dominant_emotion']=max_emotion

    return emotions

# if __name__ == "__main__":
#     print(emotion_detector("I love this new technology"))
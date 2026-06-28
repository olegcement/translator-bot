import requests
import os
api_key = os.environ.get("api_key")
URL = "https://api.anthropic.com/v1/messages"
headers = {
    "x-api-key": api_key,
    "anthropic-version":"2023-06-01",
    "content-type":"application/json"
}
def translate (text, language):
    body = {
    "model": "claude-haiku-4-5",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": f"Переведи на {language}, ответь только переводом без пояснений: {text}"}]
}    
    respons = requests.post(URL, headers=headers, json=body)
    text_output = respons.json()["content"][0]["text"]
    return(text_output)
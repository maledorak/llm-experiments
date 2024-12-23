import os
import base64
import json

import requests

from dotenv import load_dotenv

load_dotenv()

assets_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
prompt_path = os.path.join(os.path.dirname(__file__), "prompt.txt")

with open(prompt_path, "r") as file:
    prompt = file.read()


def image_to_base64(image_path: str):
    with open(image_path, "rb") as image_file:
        return f"data:image/jpeg;base64,{base64.b64encode(image_file.read()).decode('utf-8')}"


def openrouter_inference(image_base64: str):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "mistralai/pixtral-12b",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_base64}},
                ],
            },
        ],
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(response.json())

    completion_text = response.json()["choices"][0]["message"]["content"].replace("```json", "").replace("```", "").strip()
    completion_json = json.loads(completion_text)

    return completion_json, completion_text


if __name__ == "__main__":
    images_array = [
        ("Normal profile photo", "profile_photo.jpg"),
        ("Upside down profile photo", "profile_photo-upside_down.jpg"),
        ("Person with a gun", "person_with_gun.jpg"),
        ("Animal photo", "dog.jpg"),
        ("Drawing 1", "avatar_in_mask.png"),
    ]

    for image in images_array:
        print(f"{image[0]}")
        image_base64 = image_to_base64(os.path.join(assets_path, image[1]))
        completion_json, completion_text = openrouter_inference(image_base64)
        print(completion_text)

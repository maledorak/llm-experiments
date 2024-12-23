import json
import os

import mlx.core as mx
from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template
from mlx_vlm.utils import load_config

assets_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
prompt_path = os.path.join(os.path.dirname(__file__), "prompt.txt")

with open(prompt_path, "r") as file:
    prompt = file.read()


def mlx_inference(image_path: str):
    # Load the model
    model_path = "mlx-community/pixtral-12b-8bit"
    model, processor = load(model_path)
    config = load_config(model_path)

    # Prepare input
    image = [image_path]

    # Apply chat template
    formatted_prompt = apply_chat_template(
        processor, config, prompt, num_images=len(image)
    )

    # Generate output
    output = generate(
        model, processor, image, formatted_prompt, verbose=False, max_tokens=1000
    )

    completion_text = output.replace("```json", "").replace("```", "").strip()
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
        completion_json, completion_text = mlx_inference(os.path.join(assets_path, image[1]))
        print(completion_text)

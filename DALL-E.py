# Code to send image requests to the DALL-E API for AI image generation
import requests
import json

# Set up the API endpoint and headers
url = "https://api.openai.com/v1/images/generations"
headers = {
    "Content-Type": "application/json",
    # "Authorization": f"Bearer {YOUR API KEY HERE}"
    "Authorization": f"Bearer {'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'}"
}

prompt = input("Enter the Description of the Image : \n");
# Define the image generation parameters
data = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images":1,
    "size":"1024x1024"
}

# Send the request and get the response
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())

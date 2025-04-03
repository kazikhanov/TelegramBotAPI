import asyncio

import requests
import json
API_KEY = "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"
async def deepseek(content):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages": [
                {
                    "role": "user",
                    "content": f"{content}"
                }
            ],

        })
    )

    message = ""
    res = response.json()

    for i in res["choices"]:
        message += i["message"]["content"]

    return message



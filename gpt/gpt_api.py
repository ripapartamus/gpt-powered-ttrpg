from openai import OpenAI
from common.credentials import GPT_KEY
from common.config import chat_gpt
from common.general_prompts import base_system_prompt

def gpt_call(prompt, system_prompt=base_system_prompt):
    client = OpenAI(api_key=GPT_KEY)
    response = client.chat.completions.create(
        model=chat_gpt['model']
        , messages=[{"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                    ]
        , max_tokens=chat_gpt['max_tokens']
        , temperature=chat_gpt['temperature']
        , top_p=chat_gpt['top_p']
    )
    # retrieve the actual text of the response
    response_text = response.choices[0].message.content
    return response_text
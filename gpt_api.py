from openai import OpenAI
from common.credentials import GPT_KEY
from common.config import token_param, temperature_param, top_p_param, model_name
from common.prompts import system_prompt

def gpt_call(prompt):
    client = OpenAI(api_key=GPT_KEY)
    response = client.chat.completions.create(
        model=model_name
        , messages=[{"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                    ]
        , max_tokens=token_param
        , temperature=temperature_param
        , top_p=top_p_param
    )
    # retrieve the actual text of the response
    response_text = response.choices[0].message.content
    return response_text
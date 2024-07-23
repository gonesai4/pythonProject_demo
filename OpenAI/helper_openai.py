from openai import OpenAI
import os
import tiktoken

#client = openai.OpenAI()
client = OpenAI(
    #api_key="sagdsgas"
    api_key=os.environ.get("OPEN_API_KEY")
)

# def generate_text_with_openai(model, system_prompt, user_prompt):
#     response = client.chat.completions.create(
#         model= model,
#         messages=[
#             {
#                "role": "system",
#                 #"content": "you will be provided with statements, and your task is to convert them to standard English",
#                 "content": system_prompt
#             },
#             {
#                 "role": "user",
#                 #"content": "She not went to the market.",
#                 "content": user_prompt
#             }
#         ],
#         temperature=0.7,
#         max_tokens=64,
#         top_p=1
#     )
#     return response.choices[0].message.content



def count_token(prompt, model):
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = encoding.encode(prompt)
    return len(num_tokens)



def estimate_input_tokens_cost(model_name, token_count):
    if model_name == "gpt-3.5-turbo":
        cost_per_1000_tokens = 0.00050
    if model_name == "gpt-3.5-turbo-instruct":
        cost_per_1000_tokens = 0.00150
    if model_name == "gpt-4o":
        cost_per_1000_tokens = 0.0050
    if model_name == "gpt-4o-2024-05-13":
        cost_per_1000_tokens = 0.0050

    estimated_cost = (token_count / 1000) * cost_per_1000_tokens
    return estimated_cost


def estimate_output_tokens_cost(model_name, token_count):
    if model_name == "gpt-3.5-turbo":
        cost_per_1000_tokens = 0.00050
    if model_name == "gpt-3.5-turbo-instruct":
        cost_per_1000_tokens = 0.00150
    if model_name == "gpt-4o":
        cost_per_1000_tokens = 0.0050
    if model_name == "gpt-4o-2024-05-13":
        cost_per_1000_tokens = 0.0050

    estimated_cost = (token_count / 1000) * cost_per_1000_tokens
    return estimated_cost


def retrieve_openai_llm_models():
    models = client.models.list()
    print(models.data)
    for model in models.data:
        print(model.id)
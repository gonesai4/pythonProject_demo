"""
#import openai
from openai import OpenAI

#client = openai.OpenAI()
client = OpenAI(
    api_key="sagdsgas"
)

def generate_text_with_openai(model, system_prompt, user_prompt):
    response = client.chat.completions.create(
        model= model,
        messages=[
            {
               "role": "system",
                #"content": "you will be provided with statements, and your task is to convert them to standard English",
                "content": system_prompt
            },
            {
                "role": "user",
                #"content": "She not went to the market.",
                "content": user_prompt
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    return response.choices[0].message.content
"""
"""
import helper_openai

system_prompt = "give me only youtube questions related answers"
user_prompt = "Generate 5 Youtube video titles for the following content [AWS Engineer]"

output = helper_openai.generate_text_with_openai("gpt-3.5-turbo", system_prompt, user_prompt)


print(output)

system_prompt = "give me only youtube questions related answers"
user_prompt = "Generate 5 Youtube video titles for the following content [AWS Engineer]"

output = helper_openai.generate_text_with_openai("gpt-4o", system_prompt, user_prompt)

#print(response)
#print(response.choices[0].message.content)

print(output)

"""

"""
import helper_openai

system_prompt = "give me only youtube questions related answers"
user_prompt = "Generate 5 Youtube video titles for the following content [AWS Engineer]"

output = helper_openai.generate_text_with_openai("gpt-3.5-turbo", system_prompt, user_prompt)

print(output)

input_count = helper_openai.count_token(system_prompt + user_prompt, "gpt-3.5-turbo")
output_count = helper_openai.count_token(output, "gpt-3.5-turbo")
print(f"Total Input Tokens {input_count}")
print(f"Total Output Tokens {output_count}")

estimated_cost = helper_openai.estimate_input_tokens_cost("gpt-3.5-turbo", input_count)

print(f"Total estimated cost for Input Tokens {estimated_cost}")

estimated_cost = helper_openai.estimate_output_tokens_cost("gpt-3.5-turbo", output_count)

print(f"Total estimated cost for Output Tokens {estimated_cost}")

"""

"""
#adding dynamic prompts from prompt.py file
import helper_openai
import llm
import prompts

service_name = "OpenAI"
model_name = "gpt-3.5-turbo"
#system_prompt = "give me only youtube questions related answers"
#user_prompt = "Generate 5 Youtube video titles for the following content [AWS Engineer]"

#______________
# LinkedIn Post Generation
#______________

system_prompt = prompts.system_prompt_media.format(media="LinkedIn")
user_prompt = prompts.linkedin_post_generator_prompt.format(topic="Prompt Engineering Tips")



#output = llm.generate_text_with_openai("gpt-3.5-turbo", system_prompt, user_prompt)
output = llm.llm_generate_text(service_name, model_name, system_prompt, user_prompt)

print(output)

#______________
# Blog Summary Generation
#______________

system_prompt = prompts.system_prompt_media.format(media="blog")
user_prompt = prompts.linkedin_post_generator_prompt.format(MaxPoints="10", MinPoints="5", InputText=output)



#output = llm.generate_text_with_openai("gpt-3.5-turbo", system_prompt, user_prompt)
output = llm.llm_generate_text(service_name, model_name, system_prompt, user_prompt)

print(output)




# input_count = helper_openai.count_token(system_prompt + user_prompt, model_name)
# output_count = helper_openai.count_token(output, model_name)
# print(f"Total Input Tokens {input_count}")
# print(f"Total Output Tokens {output_count}")
#
# estimated_cost = helper_openai.estimate_input_tokens_cost(model_name, input_count)
#
# print(f"Total estimated cost for Input Tokens {estimated_cost}")
#
# estimated_cost = helper_openai.estimate_output_tokens_cost(model_name, output_count)
#
# print(f"Total estimated cost for Output Tokens {estimated_cost}")
"""
import helper_openai

helper_openai.retrieve_openai_llm_models()

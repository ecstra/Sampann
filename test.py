import openai, json

openai.api_key = "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"

def gpt3(messages, model = "gpt-3.5-turbo", temperature = 0, max_tokens = 500):
    """
    Utility function to interact with the OpenAI API.
    
    Args:
        messages (list): A list of message objects.
        model (str, optional): The GPT model to use. Defaults to "gpt-3.5-turbo".
        temperature (float, optional): Controls randomness. Defaults to 0.
        max_tokens (int, optional): Maximum number of tokens for the output. Defaults to 500.
    
    Returns:
        str: The generated content.
    
    Variables:
        response (dict): The raw output from the OpenAI API.
    """
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

delimiter = "#####"
system_message_context = f"""
You are an Ayurvedic doctor specialized in diabetes care. \
You will be provided with medical queries related to diabetes. \
The medical queries will be delimited with \
{delimiter} characters.
Classify each query into a primary category \
and a secondary category. 
Provide your output in json format with the \
keys: primary and secondary.

Primary categories: Diabetes Management, Diet and Nutrition, \
Herbal Remedies, or Lifestyle Changes.

Diabetes Management secondary categories:
Blood sugar monitoring
Insulin management
Medication advice

Diet and Nutrition secondary categories:
Meal planning
Foods to avoid
Nutritional supplements

Herbal Remedies secondary categories:
Herbal treatments
Ayurvedic medicines
Natural therapies

Lifestyle Changes secondary categories:
Exercise and physical activity
Stress management
Sleep quality
"""
user_message = f"""Blood sugar monitoring"""
messages =  [  
{'role':'system', 
'content': system_message_context},    
{'role':'user', 
'content': f"{delimiter}{user_message}{delimiter}"},  
]
category = gpt3(messages)
category = json.loads(category)
primary_category = category["primary"]
secondary_category = category["secondary"]
print(f"Primary category: {primary_category}")
print(f"Secondary category: {secondary_category}")
print(category)
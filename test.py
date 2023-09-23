
import json
import os

import openai

openai.api_key = "secret"

def gpt3(messages, model = "gpt-4", temperature = 0, max_tokens = 4000):
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


def get_info(user_message):
    """
    Classifies the user's query and fetches additional context.
    
    Args:
        user_message (str): The user's query.
    
    Returns:
        str: Additional information related to the user's query.
    
    Variables:
        delimiter (str): Serves as a delimiter for the system message.
        system_message_context (str): Describes the role and categories.
        messages (list): Includes a sequence of role-based messages.
        category (dict): Output from the GPT model indicating the primary and secondary categories.
        primary_category (str): Extracted primary category.
        secondary_category (str): Extracted secondary category.
        category_info (dict): Loaded from a JSON file, contains additional context.
        context (str): The additional information related to the user's query.
    """
    
    delimiter = "#####"
    system_message_context = f"""
    You are an Ayurvedic doctor specialized in diabetes care. \
    You will be provided with medical queries related to diabetes. \
    The medical queries will be delimited with \
    {delimiter} characters.
    Classify each query into a primary category \
    , secondary category and a tertiary category. 
    Provide your output in json format with the \
    keys: primary, secondary and tertiary. \
    If the message does not fit a category, \
    respond with "None" for both primary, secondary and tertiary.

    Primary Categories : Physical, Financial, All Schemes, Karnataka Diabetes Government Healthcare Schemes, Karnataka Government Healthcare Schemes Up To That Point, India Government Healthcare Schemes Up To That Point

    Physical Secondary Categories:
    Pranayama
    Yoga Asanas
    Mudras for Diabetes Management
    Color Therapy
    Seed Therapy
    Nutrition & Diet

    Financial Secondary Categories:
    Health Insurance Review
    Budget for Medical Expenses
    Medication Costs
    Lifestyle Adjustments
    Dietary Choices
    Regular Check-Ups
    Financial Planning
    Track Expenses
    Support Groups and Resources
    Emergency Fund

    All Schemes Secondary Categories:
    NPCDCS
    NHM
    PM-JAY
    RBSK
    MNDY
    DDPCU
    SHP
    NPCB
    IEC

    Karnataka Diabetes Government Healthcare Schemes Secondary Categories:
    NCD Control
    Mukhyamantri Aarogya Bhagya Scheme
    HWCs
    JSSK
    Public Awareness Campaigns
    School Health Programs
    Rural Health Services

    Karnataka Government Healthcare Schemes Up To That Point Secondary Categories:
    Vajpayee Arogyashree Scheme
    Mukhyamantri Arogya Bhagya Scheme
    RSBY
    Arogya Sanjeevini Scheme
    JSSK
    KHFWS
    HWCs
    NTCP
    Mukhyamantri Anila Bhagya Scheme
    Public Health Campaigns

    India Government Healthcare Schemes Up To That Point Secondary Categories:
    PM-JAY
    NHM
    JSY
    RBSK
    PMMVY
    NRDWP
    NTCP
    NVBDCP
    NMHP
    NACP
    NTBCP
    NPCBVI
    NPCDCS
    NOTTO
    NPPA

    Pranayama Tertiary Categories:
    Kapalbhati Pranayama
    Anulom Vilom Pranayama
    Bhastrika Pranayama
    Ujjayi Pranayama
    Surya Bhedana
    Bhramari
    Sheetali Pranayama

    Yoga Asanas Tertiary Categories:
    Paschimottanasana
    Dhanurasana
    Ardha Matsyendrasana
    Vrikshasana
    Trikonasana
    Shalabhasana
    Setu Bandhasana
    Ardha Halasana
    Bhujangasana
    Matsyasana
    Surya Namaskar
    Eka and dwipadothanadana
    Janu shirashasan
    Sarvangasana
    Halasana
    Vajrasana
    Bharadwajasana
    Balasana
    Pavanamuktasana
    Shavasana
    Mashamudrasana
    Yogamudrasana

    Mudras for Diabetes Management Tertiary Categories:
    Prana Mudra
    Apan Vayu Mudra
    Gyan Mudra
    Apana Mudra
    Rudra Mudra
    Hrudaya mudra
    LingaÂ mudra
    Surya Mudra
    Raga Bilawal
    Raga Bhairav
    Raga Kalyani
    Raga Yaman
    Raga Bhupali
    Raga Darbari
    Raga Madhyamavati
    Raga Bhupeshwari

    Color Therapy Tertiary Categories:
    Blue Color
    Yellow and Green Colors

    Seed Therapy Tertiary Categories:
    Fenugreek Seeds

    Nutrition & Diet Tertiary Categories:
    Whole Grains (Brown rice, oats, quinoa)
    Fresh Vegetables (especially bitter vegetables)
    Legumes (lentils, chickpeas)
    Lean Proteins (chicken, fish, tofu)
    Healthy Fats (avocado, nuts, seeds)
    Fiber-rich Foods (beans, broccoli, whole fruits)

    Health Insurance Review Tertiary Categories:


    Budget for Medical Expenses Tertiary Categories:


    Medication Costs Tertiary Categories:


    Lifestyle Adjustments Tertiary Categories:


    Dietary Choices Tertiary Categories:


    Regular Check-Ups Tertiary Categories:


    Financial Planning Tertiary Categories:


    Track Expenses Tertiary Categories:


    Support Groups and Resources Tertiary Categories:


    Emergency Fund Tertiary Categories:
    """
    
    messages =  [  
    {'role':'system', 
    'content': system_message_context},    
    {'role':'user', 
    'content': f"{delimiter}{user_message}{delimiter}"},  
    ]
    
    category_output = gpt3(messages)
    if category_output:
        category = json.loads(category_output)
    else:
        category = {"primary": "None", "secondary": "None", "tertiary": "None"}
        
    primary_category = category.get("primary", "None")
    secondary_category = category.get("secondary", "None")
    tertiary_category = category.get("tertiary", "None")
    
    # Load category_info from JSON file
    with open("content_categories.json", "r") as f:
        category_info = json.load(f)
    
    def get_context_by_name(context, primary, secondary, tertiary):
        secondary_dict = context.get(primary, {})
        tertiary_list = secondary_dict.get(secondary, [])
        for item in tertiary_list:
            if item.get("name") == tertiary:
                return item
        return None

    context = get_context_by_name(category_info, primary_category, secondary_category, tertiary_category)
    
    if context is not None and primary_category != "None":
        return context
    
    return "There is no additional information for this query, so respond to the user's query with your own knowledge. Make it very rich in information."

print(get_info("Health Insurance Review"))
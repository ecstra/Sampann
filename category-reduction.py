# Importing the json library to work with JSON data
import json

# Sample JSON data
with open(r"C:\InfinityX\Automa\Sampann\content_categories.json", 'r') as f:
        json_data = json.load(f)

# Function to extract categories from the JSON data
def extract_categories(data):
    primary_categories = []
    secondary_categories = {}
    tertiary_categories = {}
    
    # Extract Primary Categories
    for primary in data.keys():
        primary_categories.append(primary)
        
        # Extract Secondary Categories
        if isinstance(data[primary], dict):
            secondary_categories[primary] = []
            for secondary in data[primary].keys():
                secondary_categories[primary].append(secondary)
                
                # Extract Tertiary Categories
                if isinstance(data[primary][secondary], list):
                    tertiary_categories[secondary] = []
                    for item in data[primary][secondary]:
                        if "name" in item:
                            tertiary_categories[secondary].append(item["name"])
                            
    return primary_categories, secondary_categories, tertiary_categories

# Extracting the categories from the sample JSON data
primary, secondary, tertiary = extract_categories(json_data)

# Formatting the categories into a string representation
output_str = "Primary Categories : " + ", ".join(primary) + "\n\n"

for primary_key in secondary.keys():
    output_str += f"{primary_key} Secondary Categories:\n"
    output_str += "\n".join(secondary[primary_key]) + "\n\n"

for secondary_key in tertiary.keys():
    output_str += f"{secondary_key} Tertiary Categories:\n"
    output_str += "\n".join(tertiary[secondary_key]) + "\n\n"

print(output_str)
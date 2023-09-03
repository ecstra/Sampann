question = "What is the best way to treat a cold?"
info = "{'name': 'Blood sugar monitoring', 'images': ['url1', 'url2'], 'links': ['link1', 'link2'], 'video': 'video_url', 'text': 'Information text'}"

user_message = f"""Here is the user message: \
{question} \
And Here is some information on the topic context: \
{info}"""

user_message_for_model = f"""User message, \
remember that you respond only if the message is Ayurvedic or Medical related: \
{user_message}
"""

print(user_message_for_model)
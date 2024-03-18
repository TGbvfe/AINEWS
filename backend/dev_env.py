import json
from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
EMAIL = "Kuzeshell69@gmail.com"
PASSWD = "Wordpass197900"
cookie_path_dir = "New./cookies"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

# Read the JSON file and extract the values of content1 through content5
with open("New/news_store.json", "r") as f:
    articles = json.load(f)
    contents = [articles[i].get("content1") for i in range(5)]

# Parse the contents to the Hugging Face chatbot
summaries = []
for i, content in enumerate(contents):
    query_result = chatbot.query(f"Summarize the following article in bullet points:{content}", web_search=True)
    summaries.append(query_result)

# Print the summaries
for i, summary in enumerate(summaries):
    print(f"Summary of article {i+1}:")
    print(summary)

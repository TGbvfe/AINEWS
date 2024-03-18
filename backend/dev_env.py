import json
from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
EMAIL = "Kuzeshell69@gmail.com"
PASSWD = "Wordpass197900"
cookie_path_dir = "New."
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

# Read the JSON file and extract the article contents
with open("New/news_store.json", "r") as f:
    articles = json.load(f)
    contents = [article.get("content") for article in articles.values()]

# Parse the contents to the Hugging Face chatbot
summaries = []
for i, content in enumerate(contents, start=1):
    query_result = chatbot.query(f"Summarize the following article in bullet points:{content}", web_search=True)
    summaries.append(query_result)

# Print the summaries
for i, summary in enumerate(summaries, start=1):
    print(f"Summary of article {i}:")
    print(summary)

import json
import os
from rich import print
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data")

def list_topics():
    topics = []
    if not os.path.exists(DATA_PATH):
        return topics

    for filename in os.listdir(DATA_PATH):
        if filename.endswith(".json"):
            topics.append(filename[:-5])
    return sorted(topics)

def load_topic(topic):
    file_path = os.path.join(DATA_PATH, f"{topic}.json")
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def format_response(data):
    output = []
    output.append(f"/*/ {data['title']}")
    output.append("-" * 40)
    output.append(data["description"])

    output.append("\n - user:")
    for use in data.get("user:", []):
        output.append(f"• {use}")

    output.append("\n- basic_commands:")
    for name, cmd in data.get("basic_commands", {}).items():
        output.append(f"{name}: {cmd}")

    output.append("\! notes:")
    output.append(data.get("note", "no notes"))

    return "\n".join(output)
print("___________octopus liberey chatbot________")
print("write list to see it or write exit to turn off")

while True:
    user_input = input("\nueser: ").strip().lower()

    if user_input == "exit":
        print("good bye")
        break

    if user_input == "list":
        topics = list_topics()
        if topics:
            print("\n For available topics")
            for t in topics:
                print(f"• {t}")
        else:
            print("no data !")
        continue

    topic_data = load_topic(user_input)
    if topic_data:
        print("\n" + format_response(topic_data))
    else:
        print("There is no information on this topic. Type 'list' to see available topics.")

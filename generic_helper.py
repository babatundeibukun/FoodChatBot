def extract_session_id(session_str: str):
    import re
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    return ""


def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])


if __name__ == "__main__":
    print(get_str_from_food_dict({'samose': 2, 'pizza': 5}))
    # print(extract_session_id("projects/nang-chatbot-nbic/agent/sessions/dd3ce136-034d-4d50-d132-c4c8dd04e876/contexts/ongoing_order"))

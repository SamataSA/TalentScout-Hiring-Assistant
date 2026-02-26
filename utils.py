from prompts import EXIT_KEYWORDS

def is_exit(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in EXIT_KEYWORDS)

def safe_json_parse(text: str):
    import json
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        return json.loads(text[start:end])
    except:
        return None
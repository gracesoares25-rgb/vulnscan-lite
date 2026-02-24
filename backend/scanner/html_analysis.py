def analyze_html(content):
    content = content.lower()

    result = {}

    result["Inline Scripts"] = "<script>" in content
    result["TODO Comments"] = "todo" in content

    if "wp-content" in content:
        result["CMS"] = "WordPress"
    elif "joomla" in content:
        result["CMS"] = "Joomla"
    else:
        result["CMS"] = "Not Detected"

    return result
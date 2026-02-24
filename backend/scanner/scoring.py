def calculate_score(headers, ssl_data, html):

    score = 100
    passed = []
    failed = []

    # Header scoring
    for key, value in headers.items():
        if value:
            score += 10
            passed.append(key)
        else:
            score -= 10
            failed.append(key)

    # SSL scoring
    if ssl_data.get("SSL Valid"):
        passed.append("SSL Valid")
    else:
        score -= 20
        failed.append("SSL Valid")

    # HTML checks
    if html.get("Inline Scripts"):
        score -= 10
        failed.append("Inline Scripts")
    else:
        passed.append("Inline Scripts")

    if html.get("TODO Comments"):
        score -= 10
        failed.append("TODO Comments")

    score = max(min(score, 100), 0)

    return score, passed, failed
from fastapi import FastAPI
from fastapi.responses import FileResponse
import requests

from scanner.headers_check import check_headers
from scanner.ssl_check import check_ssl
from scanner.html_analysis import analyze_html
from scanner.scoring import calculate_score
from scanner.remediation import get_remediation

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("static/index.html")


def scan_website(url: str):

    # If user forgets https
    if not url.startswith("http"):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        content = response.text

    except Exception as e:
        return {"Error": str(e)}

    # 🔥 THIS IS STEP 6 (Integration Part)
    headers_result = check_headers(headers)
    ssl_result = check_ssl(url)
    html_result = analyze_html(content)

    score, passed, failed = calculate_score(
        headers_result,
        ssl_result,
        html_result
    )

    remediation = get_remediation(failed)

    final_report = {
        "Score": score,
        "Passed Checks": passed,
        "Failed Checks": failed,
        "SSL Details": ssl_result,
        "CMS": html_result.get("CMS"),
        "Remediation": remediation
    }

    return final_report


@app.get("/scan")
def scan(url: str):
    return scan_website(url)
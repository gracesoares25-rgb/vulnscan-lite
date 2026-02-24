def check_headers(headers):
    result = {}

    result["HSTS"] = "Strict-Transport-Security" in headers
    result["CSP"] = "Content-Security-Policy" in headers
    result["X-Frame-Options"] = "X-Frame-Options" in headers

    return result
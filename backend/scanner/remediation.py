def get_remediation(failed_checks):

    fixes = []

    for issue in failed_checks:

        if issue == "HSTS":
            fixes.append("Enable Strict-Transport-Security header in server configuration.")

        elif issue == "CSP":
            fixes.append("Add Content-Security-Policy header to prevent XSS attacks.")

        elif issue == "X-Frame-Options":
            fixes.append("Add X-Frame-Options header to prevent clickjacking.")

        elif issue == "SSL Valid":
            fixes.append("Install a valid SSL certificate from a trusted CA.")

        elif issue == "Inline Scripts":
            fixes.append("Avoid inline scripts. Use external JS files.")

        elif issue == "TODO Comments":
            fixes.append("Remove development TODO comments before production.")

    return fixes
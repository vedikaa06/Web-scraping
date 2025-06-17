def load_headers():
    """
    Returns a dictionary of HTTP headers for the request.
    Modify the User-Agent to mimic a real browser.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.88 Safari/537.36"
    }
    return headers

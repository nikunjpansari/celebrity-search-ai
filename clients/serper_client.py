import os
import requests

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_ENDPOINT = "https://google.serper.dev/search"


def fetch_search_snippet(query: str) -> str | None:
    """
    Use SerperAPI to perform a Google search for `query` and
    return the top organic result's snippet, or None if unavailable.
    """
    headers = {"X-API-KEY": SERPER_API_KEY}
    payload = {"q": query, "num": 1}
    try:
        resp = requests.post(SERPER_ENDPOINT, json=payload, headers=headers, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        organic = data.get("organic", [])
        if organic and "snippet" in organic[0]:
            return organic[0]["snippet"]
    except Exception:
        return None
    return None

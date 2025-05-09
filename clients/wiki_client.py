import wikipedia


def fetch_image_url(query: str) -> str | None:
    """
    Return the first image URL from the Wikipedia page for `query`,
    or None if not found.
    """
    try:
        page = wikipedia.page(query)
        # filter for common image formats
        for img in page.images:
            if img.lower().endswith((".jpg", ".jpeg", ".png")):
                return img
    except Exception:
        return None
    return None

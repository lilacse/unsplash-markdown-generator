import requests


def get_photo(access_token: str, url: str):
    unsplash_prefix = "https://unsplash.com/photos/"
    if url.startswith(unsplash_prefix):
        photo_id = url.removeprefix(unsplash_prefix)
    else:
        raise ValueError(f"`{url} is not an Unsplash photo url`")

    api_url = f"https://api.unsplash.com/photos/{photo_id}"
    headers = {"Authorization": f"Client-ID {access_token}"}

    response = requests.get(api_url, headers=headers)
    return response.content.decode()

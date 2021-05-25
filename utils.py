import requests


def download_and_save_file(url, local_path):
    """
    Downloads a file from given url and saves it to local location.
    Returns the file path of the locally saved file.
    """
    r = requests.get(url)
    with open(local_path, "wb") as f:
        f.write(r.content)

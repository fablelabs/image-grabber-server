import requests

def download_and_save_file(url):
    """
    Downloads a file from given url and saves it to local location.
    Returns the file path of the locally saved file.
    """
    r = requests.get(url)  
    file_path = "/path/I/want/to/save/file/to/file_name"
    with open(file_path, 'wb') as f:
        f.write(r.content)

    return file_path
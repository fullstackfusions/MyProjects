import threading
import requests
from urllib.parse import urlparse
from os.path import basename

class FileDownloader:
    def __init__(self, urls):
        self.urls = urls

    def download_file(self, url):
        """Download a file from a URL."""
        try:
            response = requests.get(url, stream=True)
            filename = basename(urlparse(url).path)
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
            print(f"{filename} downloaded.")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    def run(self):
        threads = []
        for url in self.urls:
            thread = threading.Thread(target=self.download_file, args=(url,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()  # Wait for all threads to complete

# Example usage
urls = [
    "https://example.com/file1.jpg",
    "https://example.com/file2.jpg",
    # More URLs...
]
downloader = FileDownloader(urls)
downloader.run()
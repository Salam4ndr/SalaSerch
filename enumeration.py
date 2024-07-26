import requests
import concurrent.futures
from rich import print
from tqdm import tqdm

def check_url(url):
    try:
        # Make a HEAD request to the specified URL
        response = requests.head(url, timeout=0.5, allow_redirects=False)
        # Check if the response status code is 200 or 301 OK
        if response.status_code == 200 or response.status_code == 301:
            # Print a message indicating a successful request
            print(f"[yellow][+] {url}")
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        # Ignore any exceptions raised by the request
        pass

# Function for enumeration
def enumeration(url_template, wordlist):
    print("[bold green][+] Enumeration is about to start...\n")

    # Open the wordlist file with UTF-8 encoding, ignoring errors
    with open(wordlist, "r", encoding="utf-8", errors='ignore') as file:
        # Read and strip each line in the file to get words
        words = [line.strip() for line in file]

    # Create a ThreadPoolExecutor with 100 maximum workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        # Use tqdm to create a progress bar
        with tqdm(total=len(words), desc="Progress", unit="word", leave=True) as pbar:
            futures = []
            for word in words:
                # Replace "SALAMANDER" in the URL template with the current word
                url = url_template.replace("SALAMANDER", word)
                future = executor.submit(check_url, url)
                futures.append(future)

            # Update the progress bar as each future completes
            for future in concurrent.futures.as_completed(futures):
                pbar.update(1)
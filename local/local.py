# Request a local copy of HTML content from a given URL and store it in a local FILE.
import requests


URL = "https://core.telegram.org/bots/api"
FILE = "core_telegram_org_bots_api.html"


def fetch_page(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def save_to_file(content: str, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    html_content = fetch_page(URL)
    save_to_file(html_content, FILE)


# Last requested on 2024-11-21
if __name__ == "__main__":
    main()

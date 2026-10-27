
import time
from urllib.parse import urljoin, urlparse

import pandas as pd
import requests
from bs4 import BeautifulSoup


HOME_PAGE = "https://indianexpress.com/"
INTERN_NAME = "Shine_paul" 
NUMBER_OF_ARTICLES = 25
WAIT_BETWEEN_REQUESTS = 1
CSV_FILE = "indian_express_news.csv"

columns = [
    f"NEWS_TITLE_{INTERN_NAME}",
    "NEWS_LINK",
    "FULL_SCRAPED_TEXT",
]

# A session reuses the connection and keeps the request settings in one place.
session = requests.Session()
session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/129.0.0.0 Safari/537.36"
    )
})


def get_html(url):
    """Return the page HTML. If the request fails, return None."""
    try:
        response = session.get(url, timeout=20)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as error:
        print(f"Could not open {url}: {error}")
        return None


def get_news_links(html):
    """Find news links on the homepage and remove duplicates."""
    soup = BeautifulSoup(html, "html.parser")
    news_links = []
    visited = set()

    # News headlines are usually inside heading tags. Article cards are also
    # checked because the homepage layout can vary.
    headline_links = []
    for heading in soup.find_all(["h1", "h2", "h3", "h4"]):
        headline_links.extend(heading.find_all("a", href=True))

    for article in soup.find_all("article"):
        headline_links.extend(article.find_all("a", href=True))

    # Use all links as a fallback if the page has a different layout.
    if not headline_links:
        headline_links = soup.find_all("a", href=True)

    skip_words = (
        "/videos/", "/photos/", "/web-stories/", "/podcasts/",
        "/author/", "/topic/", "/tag/", "/liveblog/", "/live-blog/"
    )

    for link in headline_links:
        href = link.get("href", "").strip()
        title = " ".join(link.get_text(" ", strip=True).split())

        if not href or len(title) < 15:
            continue

        url = urljoin(HOME_PAGE, href)
        parsed_url = urlparse(url)

        if parsed_url.netloc.lower() not in {
            "indianexpress.com", "www.indianexpress.com"
        }:
            continue

        if parsed_url.path in ("", "/"):
            continue

        if any(word in parsed_url.path.lower() for word in skip_words):
            continue

        if parsed_url.path.lower().endswith(
            (".jpg", ".jpeg", ".png", ".gif", ".pdf", ".xml")
        ):
            continue

        # Remove query strings and fragments so the same article is not
        # collected more than once.
        url = parsed_url._replace(
            scheme="https",
            netloc="indianexpress.com",
            query="",
            fragment=""
        ).geturl().rstrip("/")

        if url not in visited:
            visited.add(url)
            news_links.append({"title": title, "url": url})

        if len(news_links) >= NUMBER_OF_ARTICLES * 3:
            break

    return news_links


def get_article_details(html):
    """Extract the article title and its main text."""
    soup = BeautifulSoup(html, "html.parser")

    title = ""
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        title = og_title["content"].strip()
    elif soup.title:
        title = soup.title.get_text(" ", strip=True)

    # Try common article-body selectors first. If none work, try the main
    # article area instead.
    article_body = None
    possible_selectors = [
        '[itemprop="articleBody"]',
        ".story_details",
        ".full-details",
        ".story-content",
        ".article-content",
        ".articles",
        "article",
        "main",
    ]

    for selector in possible_selectors:
        section = soup.select_one(selector)
        if section and len(section.get_text(" ", strip=True)) > 250:
            article_body = section
            break

    if article_body is None:
        return title, ""

    # Remove page elements that are not part of the story.
    for element in article_body.select(
        "script, style, nav, aside, footer, form, button, "
        ".advertisement, .related, .social-share"
    ):
        element.decompose()

    paragraphs = []
    for paragraph in article_body.find_all(["p", "h2", "h3"]):
        text = " ".join(paragraph.get_text(" ", strip=True).split())
        if text and text not in paragraphs:
            paragraphs.append(text)

    article_text = "\n".join(paragraphs).strip()

    # Some pages do not use paragraph tags for the main content.
    if len(article_text) < 100:
        article_text = " ".join(article_body.get_text(" ", strip=True).split())

    return title, article_text


def main():
    print("Opening the Indian Express homepage...")
    home_html = get_html(HOME_PAGE)

    if home_html is None:
        print("The homepage could not be loaded. Please check your internet connection.")
        return

    news_links = get_news_links(home_html)

    if not news_links:
        print("No news links were found. The website layout may have changed.")
        return

    print(f"Found {len(news_links)} possible news links.")

    rows = []
    saved_urls = set()

    for item in news_links:
        if len(rows) >= NUMBER_OF_ARTICLES:
            break

        url = item["url"]
        if url in saved_urls:
            continue
        saved_urls.add(url)

        # Wait between requests instead of sending them all at once.
        if rows:
            time.sleep(WAIT_BETWEEN_REQUESTS)

        print(f"Reading article {len(rows) + 1}: {item['title']}")
        article_html = get_html(url)

        if article_html is None:
            continue

        title, article_text = get_article_details(article_html)

        if not title:
            title = item["title"]

        # Skip pages that do not appear to contain a full news story.
        if len(article_text) < 200:
            print("  Skipped: not enough article text was found.")
            continue

        rows.append({
            columns[0]: title,
            columns[1]: url,
            columns[2]: article_text,
        })

    if not rows:
        print("No article text was collected. Please check the page selectors.")
        return

    news_df = pd.DataFrame(rows, columns=columns)
    news_df.to_csv(CSV_FILE, index=False, encoding="utf-8-sig")

    print(f"\nFinished. Saved {len(news_df)} articles to {CSV_FILE}.")

    if len(news_df) < 20:
        print(
            "The file contains fewer than 20 articles. You may need to run it "
            "again or adjust the selectors to match the current website."
        )


if __name__ == "__main__":
    main()

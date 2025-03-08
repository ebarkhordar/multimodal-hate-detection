import os
import re
import instaloader
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve your Instagram credentials
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")


def extract_shortcode(url):
    """
    Extracts the shortcode from an Instagram reel URL.
    Example URL: "https://www.instagram.com/reel/DDz1G3qvEuz/?igsh=MWNkdzV1dXE0NW1saQ=="
    """
    match = re.search(r"instagram\.com\/reel\/([^\/\?]+)", url)
    if match:
        return match.group(1)
    raise ValueError("Shortcode not found in URL")


# Your Instagram reel URL
url = "https://www.instagram.com/reel/DDz1G3qvEuz/?igsh=MWNkdzV1dXE0NW1saQ=="
shortcode = extract_shortcode(url)
print("Extracted shortcode:", shortcode)

# Create an instance of Instaloader and log in
L = instaloader.Instaloader()
L.login(USERNAME, PASSWORD)

# Load the post using the extracted shortcode
post = instaloader.Post.from_shortcode(L.context, shortcode)

# Print post details
print("Caption:", post.caption)
print("Likes:", post.likes)
print("Number of Comments:", post.comments)

# Retrieve and print all comments (if needed)
# Note: Fetching a large number of comments might take some time.
all_comments = list(post.get_comments())
print("\nAll Comments:")
for comment in all_comments:
    print("-", comment.text)

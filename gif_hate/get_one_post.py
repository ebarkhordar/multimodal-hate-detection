import os
import instaloader
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve credentials from environment variables
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Log in using your credentials
L.login(USERNAME, PASSWORD)

# Use the shortcode from the Instagram reel URL (e.g., "DDz1G3qvEuz")
shortcode = "DDz1G3qvEuz"
post = instaloader.Post.from_shortcode(L.context, shortcode)

# Print basic post information
print("Caption:", post.caption)
print("Likes:", post.likes)
print("Number of Comments:", post.comments)

# Retrieve all comments (ensure you're logged in for posts with many comments)
all_comments = list(post.get_comments())
print("\nAll Comments:")
for comment in all_comments:
    print("-", comment.text)

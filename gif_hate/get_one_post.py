import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Optionally, log in if the post isn’t public
# L.login("your_username", "your_password")

# Extract the shortcode from the URL:
# For "https://www.instagram.com/reel/DDz1G3qvEuz/?igsh=MWNkdzV1dXE0NW1saQ==", the shortcode is "DDz1G3qvEuz"
shortcode = "DDz1G3qvEuz"

# Load the post using the shortcode
post = instaloader.Post.from_shortcode(L.context, shortcode)

# Print basic post info
print("Caption:", post.caption)
print("Likes:", post.likes)
print("Number of Comments:", post.comments)

# Retrieve all comments
all_comments = list(post.get_comments())
print("\nAll Comments:")
for comment in all_comments:
    print("-", comment.text)

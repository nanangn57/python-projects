import requests


class Post:

    def __init__(self):
        self.blog_posts = None
        self.get_blog()

    def get_blog(self):
        blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(blog_url)
        self.blog_posts = response.json()
        return self.blog_posts


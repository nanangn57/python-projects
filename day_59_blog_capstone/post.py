import requests


class Post:

    def __init__(self):
        self.blog_posts = None
        self.get_blog()

    def get_blog(self):
        blog_url = "https://api.npoint.io/2378d3d8e0262f7e23d3"
        response = requests.get(blog_url)
        self.blog_posts = response.json()
        return self.blog_posts

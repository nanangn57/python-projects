from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    post = Post()
    return render_template("index.html", posts=post.blog_posts)


@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    post = Post()
    return render_template("post.html", posts=post.blog_posts, blog_id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/home')
def home():
    post = Post()
    return render_template("index.html",  posts=post.blog_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    post = Post()
    return render_template("post.html", posts=post.blog_posts, blog_id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
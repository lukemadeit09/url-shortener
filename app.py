import os
import string
import random

from flask import Flask, request, redirect, render_template_string
import redis

app = Flask(__name__)
cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True,
)

HTML = """
<!doctype html>
<title>URL Shortener</title>
<h1>🔗 URL Shortener</h1>
<form action="/shorten" method="post">
  <input name="url" placeholder="https://example.com" size="40" required>
  <button type="submit">Shorten</button>
</form>
{% if short_url %}
<p>Short URL: <a href="{{ short_url }}">{{ short_url }}</a></p>
{% endif %}
"""


def generate_code(n=6):
    """Return a random alphanumeric short code."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/shorten", methods=["POST"])
def shorten():
    url = request.form["url"]
    code = generate_code()
    cache.set(code, url)
    short_url = request.host_url + code
    return render_template_string(HTML, short_url=short_url)


@app.route("/<code>")
def follow(code):
    url = cache.get(code)
    if url:
        return redirect(url)
    return "Short code not found", 404


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
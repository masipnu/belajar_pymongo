from flask import Flask

app = Flask(__name__)

@app.route("/me")
def me_api():
	user = get_current_user()
	return {
	"username": user.username,
	"theme": user.theme,
	"image": url_for("user_image", filename=user.image)
	}

if __name__ == '__main__':
	app.run(debug=True)
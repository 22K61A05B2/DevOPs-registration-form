from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

@app.route("/")
def index():
    """Render the registration form."""
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    """Handle form submission and validation."""
    full_name = request.form.get("full_name")
    username = request.form.get("username")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    gender = request.form.get("gender")

    # Basic validation
    if not full_name or not username or not email or not phone or not password or not confirm_password:
        flash("All fields are required!")
        return redirect(url_for("index"))

    if len(password) < 6:
        flash("Password must be at least 6 characters long!")
        return redirect(url_for("index"))

    if password != confirm_password:
        flash("Passwords do not match!")
        return redirect(url_for("index"))

    if not phone.isdigit() or len(phone) != 10:
        flash("Phone number must be 10 digits!")
        return redirect(url_for("index"))

    # On successful validation
    return render_template("success.html", full_name=full_name)

if __name__ == "__main__":
    app.run(debug=True)

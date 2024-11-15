from flask import Flask, request, render_template_string

app = Flask(__name__)

# Inline HTML form
form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Form with File Output</title>
</head>
<body>

<h2>Registration Form</h2>
<form action="/submit" method="post">
    <label for="name">Full Name:</label>
    <input type="text" id="name" name="name" required>
    <br><br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <br><br>

    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <br><br>

    <label>Gender:</label>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Male</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>
    <input type="radio" id="other" name="gender" value="other">
    <label for="other">Other</label>
    <br><br>

    <label>Hobbies:</label>
    <input type="checkbox" id="hobby1" name="hobby" value="reading">
    <label for="hobby1">Reading</label>
    <input type="checkbox" id="hobby2" name="hobby" value="sports">
    <label for="hobby2">Sports</label>
    <input type="checkbox" id="hobby3" name="hobby" value="music">
    <label for="hobby3">Music</label>
    <br><br>

    <label for="country">Country:</label>
    <select id="country" name="country" required>
        <option value="us">United States</option>
        <option value="uk">United Kingdom</option>
        <option value="in">India</option>
        <option value="au">Australia</option>
    </select>
    <br><br>

    <button type="submit">Submit</button>
</form>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(form_html)

@app.route("/submit", methods=["POST"])
def submit():
    # Retrieve form data
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    gender = request.form.get("gender")
    hobbies = request.form.getlist("hobby")
    country = request.form.get("country")

    # Format the data
    data = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Password: {password}\n"
        f"Gender: {gender}\n"
        f"Hobbies: {', '.join(hobbies)}\n"
        f"Country: {country}\n\n"
    )

    # Write data to file
    with open("data.txt", "a") as file:
        file.write(data)

    return "Thank you! Your information has been saved."

if __name__ == "__main__":
    app.run(debug=True)

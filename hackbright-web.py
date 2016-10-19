from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    grades_by_title = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github, grades_title= grades_by_title)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def get_display_student_form():
    """Show form for searching for a student."""

    return render_template("student_add.html")


@app.route("/student-add", methods=["POST"])
def get_confirm_added_student():
    """Confirm student was added."""

    first = request.form.get("first")
    last = request.form.get("last")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)

    return html

@app.route("/project/<title>")
def get_project(title):
  """Display project information"""

  title, description, max_grade = hackbright.get_project_by_title(title)


  html = render_template("project_info.html",
                           title=title,
                           description=description,
                           max_grade=max_grade)

  return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

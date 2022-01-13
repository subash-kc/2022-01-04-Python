"""
192.168.30.22 hostA.localdomain # hostA
192.168.30.33 hostB.localdomain # hostB
192.168.30.44 hostC.localdomain # hostB

"""

"""
groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

"""

from flask import Flask, request, redirect, url_for, session, render_template
# from flask import request
# from flask import redirect
# from flask import url_for
# from flask import session
# from flask import render_template

app = Flask(__name__)

app.secret_key= "random random RANDOM!"

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/", methods= ["GET","POST"])
def hosts():
    # GET returns the rendered hosts
    # POST adds new hosts, then returns rendered hosts
    if "username" in session and session["username"] == "admin":
        if request.method == "POST":
            # pull all values from posted form
            hostname = request.form.get("hostname")
            ip = request.form.get("ip")
            fqdn = request.form.get("fqdn")
            # create a new dictionary with values, add to groups
            groups.append({"hostname": hostname, "ip": ip, "fqdn": fqdn})
    return render_template("hosts.j2", groups=groups)

@app.route("/form", methods=["GET","POST"])
def form():
    # HTML form that collects hostname, ip, and fqdn values
    if request.method == "POST":
        session["username"] = request.form.get("username")
    if "username" in session and session["username"] == "admin":
        return render_template("formcollector.html.j2")
    else:
        return """
   <form action = "" method = "post">
      <p>Invalid Login.</p>
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/logout")
def logout():
    # accessing this page pops the value of username of the session
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

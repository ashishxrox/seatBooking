import csv
from flask import Flask
from flask import render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("landing.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv1(data):
    with open('database.csv','a', newline='') as database:
        name1 = data["name"]
        age1 = data["age"]
        contact = data["contact"]
        name2 = data["name2"]
        age2 = data["age2"]
        name3 = data["name3"]
        age3 = data["age3"]
        name4 = data["name4"]
        age4 = data["age4"]
        sNo = data["sNo"]

        writer = csv.writer(database)

        if sNo == "1":
            writer.writerow([name1, age1, contact])
        elif sNo == "2":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
        elif sNo == "3":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
            writer.writerow([name3, age3])
        elif sNo == "4":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
            writer.writerow([name3, age3])
            writer.writerow([name4, age4])
        else:
            writer.writerow(["INVALID"])

def write_to_csv2(data):
    with open('database2.csv','a', newline='') as database:
        name1 = data["name"]
        age1 = data["age"]
        contact = data["contact"]
        name2 = data["name2"]
        age2 = data["age2"]
        name3 = data["name3"]
        age3 = data["age3"]
        name4 = data["name4"]
        age4 = data["age4"]
        sNo = data["sNo"]

        writer = csv.writer(database)

        if sNo == "1":
            writer.writerow([name1, age1, contact])
        elif sNo == "2":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
        elif sNo == "3":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
            writer.writerow([name3, age3])
        elif sNo == "4":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
            writer.writerow([name3, age3])
            writer.writerow([name4, age4])
        else:
            writer.writerow(["INVALID"])

def write_to_csv3(data):
    with open('database3.csv','a', newline='') as database:
        name1 = data["name"]
        age1 = data["age"]
        contact = data["contact"]
        name2 = data["name2"]
        age2 = data["age2"]
        name3 = data["name3"]
        age3 = data["age3"]
        name4 = data["name4"]
        age4 = data["age4"]
        sNo = data["sNo"]

        writer = csv.writer(database)

        if sNo == "1":
            writer.writerow([name1, age1, contact])
        elif sNo == "2":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
        elif sNo == "3":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
            writer.writerow([name3, age3])
        elif sNo == "4":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
            writer.writerow([name3, age3])
            writer.writerow([name4, age4])
        else:
            writer.writerow(["INVALID"])

def write_to_csv4(data):
    with open('database4.csv','a', newline='') as database:
        name1 = data["name"]
        age1 = data["age"]
        contact = data["contact"]
        name2 = data["name2"]
        age2 = data["age2"]
        name3 = data["name3"]
        age3 = data["age3"]
        name4 = data["name4"]
        age4 = data["age4"]
        sNo = data["sNo"]

        writer = csv.writer(database)

        if sNo == "1":
            writer.writerow([name1, age1, contact])
        elif sNo == "2":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
        elif sNo == "3":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
            writer.writerow([name3, age3])
        elif sNo == "4":
            writer.writerow([name1, age1, contact])
            writer.writerow([name2, age2])
            writer.writerow([name3, age3])
            writer.writerow([name4, age4])
        else:
            writer.writerow(["INVALID"])



@app.route('/form1', methods=['POST', 'GET'])
def get_info1():
    if request.method == 'POST':
        data = request.form.to_dict()
        s_no = request.form.get('sNo')
        write_to_csv1(data)

        return render_template("confirmation.html")

    else:
        return "Something Went Wrong!!!"

@app.route('/form2', methods=['POST', 'GET'])
def get_info2():
    if request.method == 'POST':
        data = request.form.to_dict()
        s_no = request.form.get('sNo')
        write_to_csv2(data)

        return render_template("confirmation.html")

    else:
        return "Something Went Wrong!!!"

@app.route('/form3', methods=['POST', 'GET'])
def get_info3():
    if request.method == 'POST':
        data = request.form.to_dict()
        s_no = request.form.get('sNo')
        write_to_csv3(data)

        return render_template("confirmation.html")

    else:
        return "Something Went Wrong!!!"

@app.route('/form4', methods=['POST', 'GET'])
def get_info4():
    if request.method == 'POST':
        data = request.form.to_dict()
        s_no = request.form.get('sNo')
        write_to_csv4(data)

        return render_template("confirmation.html")

    else:
        return "Something Went Wrong!!!"

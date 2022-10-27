from datetime import date, datetime
from urllib import request
from flask import Flask, render_template, request
import math


app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = {}

@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    date=datetime.now()
    currentDate = date.strftime("%d-%m-%Y %h:%M:%S")
    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    global number
    global results
    global null
    null = ' '
    # Display "Number {Number} is even" if given number is even on result.html page
    number = request.form['number']
    if (int(number)%2==0):
        results="Number "+number+" is even"
        return render_template('result.html', results=results)
       # Display "Number {Number} is odd" if given number is odd on result.html page
    elif (int(number)%2==1):
        results="Number "+number+" is odd"
        return render_template('result.html', results=results)
    # Display "No number provided" if value is null or blank on result.html page
    elif (number== null):
        results="Provided input is not an integer!"
        return render_template('result.html', results=results)
    # Display "" if value is not a number on result.html page
    elif (math.isnan (number)== True):
        results=""
        return render_template('result.html', results=results)
    # Write your to code here to check whether number is even or odd and render result.html page


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrganisation = request.form['organisation']

    # Append this value to studentOrganisationDetails
    studentOrganisationDetails[studentName]= studentOrganisation

    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentOrganisationDetails=studentOrganisationDetails)

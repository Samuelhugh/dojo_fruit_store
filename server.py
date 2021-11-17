from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         # Methods is a list that can hold other Values like "GET" and more. Also if I don't Provide a Method for METHODS the default is "GET" (Which is Not Secure). I also have to Specify what Kind of Method I want for my Form. I use Forms to Gather data from Users, and Inputs to get the values, The Label is just a title for my input, And then <input type="submit"> or <button>submit</button> to send or submit that Information.
def checkout():
    values = request.form['strawberry'] # I use request.form to access the form data for example the Input, select/options data and other data. The Inputs "NAME" Specifically. So the Naming of the "NAME" I have for my Input is VERY Important. I also have to set the request.info to a Variable (Like Most Things) if I want to use the Value elsewhere, Otherwise it will just SHOW me the Value thats being logged.
    # print(request.form['strawberry']) # Print Statement to make sure I am receiving the correct Information from my request.form.
    amount = request.form['raspberry']
    # print(request.form['raspberry'])
    quantity = request.form['apple']
    # print(request.form['apple'])
    first = request.form['first_name']
    # print(request.form['first_name'])
    last = request.form['last_name']
    # print(request.form['last_name'])
    id = request.form['student_id']
    # print(request.form['student_id'])
    print(f"Charging {first} {last} for {int(values) + int(amount) + int(quantity)} fruits")
    return render_template("checkout.html", values=request.form['strawberry'], amount=request.form['raspberry'], quantity=request.form['apple'], first=request.form['first_name'], last=request.form['last_name'], id=request.form['student_id']) # Rendering Template causes the information to be Resubmitted, Causing problems because it can mean that if a User clicks continue on the dialogue prompt that comes up on the page then that means the Form will Resubmit and Process all of the Transactions again Charging the Credit Card over and over again or result in Duplication of data on my Application (i.e storing multiple Users in the DAtabase!!).

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
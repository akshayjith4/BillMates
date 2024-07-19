from flask.views import MethodView
from wtforms import Form, StringField, IntegerField
from flask import Flask, render_template, request
from wtforms.fields.simple import SubmitField
from Flatmates_bill import flat

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)

        bill_amount = float(billform.amount.data)
        period = billform.period.data
        num_flatmates = int(billform.num_flatmates.data)

        # Create Bill object
        the_bill = flat.Bill(bill_amount, period)

        # Collect flatmates' data
        flatmates = []
        for i in range(num_flatmates):
            name = request.form.get(f'name{i + 1}')
            days = float(request.form.get(f'days_in_the_house{i + 1}'))
            flatmate = flat.Flatmate(name, days)
            flatmates.append(flatmate)

        # Calculate shares
        shares = [(flatmate.name, "{:.2f}".format(flatmate.calculate_share(the_bill, flatmates))) for flatmate in flatmates]

        return render_template('results.html', shares=shares)

class BillForm(Form):
    amount = StringField("Bill Amount:")
    period = StringField("Bill Period")
    num_flatmates = IntegerField("Number of Flatmates:")
    button = SubmitField("Calculate")

app.add_url_rule('/', view_func=HomePage.as_view('Homepage'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('Bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

if __name__ == '__main__':
    app.run(debug=True)

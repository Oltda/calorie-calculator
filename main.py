from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature


app = Flask(__name__)






class CalorieFormPage(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template('calorie_form_page.html', calorieForm=calorie_form)
    def post(self):
        calorie_form = CalorieForm(request.form)
        try:
            weight = float(calorie_form.weight.data)
            height = float(calorie_form.height.data)
            age = float(calorie_form.age.data)
            city = calorie_form.city.data
            country = calorie_form.country.data
            city = city.replace(" ", "-").lower()
            country = country.replace(" ", "-").lower()




            weather = Temperature(country, city)
            calorie = Calorie(weight, height, age, weather.get())
            my_intake = calorie.calculate()
        except:
            calorie_form = CalorieForm(request.form)
            return render_template('calorie_form_page.html',
                                   calorieForm=calorie_form,
                                   noresult=True)





        return render_template('calorie_form_page.html',

                               calorieForm=calorie_form,
                               my_intake=my_intake,
                               result=True
                               )




class CalorieForm(Form):
    weight = StringField("Weight: ")
    height = StringField("Height: ")
    age = StringField("Age: ")
    country = StringField("Country: ")
    city = StringField("City: ")
    button = SubmitField("Calculate ")



app.add_url_rule('/', view_func=CalorieFormPage.as_view('calorie_form_page'))

app.run(debug=True)
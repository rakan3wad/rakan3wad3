from flask import Flask, render_template, url_for, redirect
# أول ما تبدأ مشروع فلاسك لازم تسوي هذي الخطوات في التيرمنال لبنا virtual enviroment
# pip install virtualenv
# virtualenv myEnv -p python3
# env\Scripts\activate.bat
# ______________________________________________________________________________________________________
# بعدين كتبت ابسط كود ممكن
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return "Rakan is GREAT 👍👍👍😉🤨😊 "
# if __name__ == "__main__":
#     app.run(debug=True)
# واذا تبغى تشوفه على المتصفح اكتب في التيرمنال
# python *.py
# *هو اسم ملف بايثون الي حطيته
# وبيطلع لك الرابط
# ______________________________________________________________________________________________________
# inheritance عشان ماتكرر الكود كامل حق  الفوتر والهيدر
# {% block name_of_block %} TEXT {% endblock %}
# ^ الي عليها خط قابله للتغيير
# ______________________________________________________________________________________________________ aش
# ^ 2nd line is an explanation of Flask ^
# السطر الثاني شرح للبداية في فلاسك من تثبيت وغيره




app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

# لو تحط بعد الهاش اي اسم .. مثلا راكان راح يفتح صفحة مكتوب فيها أهلا راكان
@app.route('/<name>')
def user(name):
    return f"helo {name} 👍"

@app.route('/signin')
def signin():
    return "helo frined 👍"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')

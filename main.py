from flask import Flask, render_template, request, redirect, url_for
from create_employee import create_employee
from db_connection import get_connection
from read_employee import read_employees
from update_employee import update_employee
from delete_employee import delete_employee
from read_employee_by_id import read_employee_by_id
app = Flask(__name__)

@app.route('/')
def index():
    employees = read_employees()
    return render_template('index.html', employees=employees)

# Page to create a new user
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        id = request.form['id_employee']
        name = request.form['name']
        departement = request.form['departement']
        salary = int(request.form['salary'])
        create_employee(id, name, departement, salary)
        return redirect(url_for('index'))
    return render_template('create.html')

# Page to update a user
@app.route('/update/<int:employee_id>', methods=['GET', 'POST'])
def update(user_id):
    employee = read_employee_by_id
    if request.method == 'POST':
        id = request.form['id_employee']
        name = request.form['name']
        departement = request.form['departement']
        salary = int(request.form['salary'])
        update_employee(id, name, departement, salary)
        return redirect(url_for('index'))
    return render_template('update.html', employee=employee)

# Page to delete a user
@app.route('/delete/<int:employee_id>', methods=['POST'])
def delete(employee_id):
    delete_employee(employee_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

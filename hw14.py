@app.route("/register", methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        username = ['username']
        password = ['password']
        email = ['email']
        first_name = ['first_name']
        surname = ['surname']
        return render_template('register_form.html',
                               username=username,
                               password=password,
                               email=email,
                               first_name=first_name,
                               surname=surname
                               )

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        first_name = request.form['first_name']
        surname = request.form['surname']
        with Session(al_db.engine) as session:
            registration = models_db.User(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                surname=surname
            )
        session.add(registration)
        session.commit()

        return 'Зареєстровано успішно!'
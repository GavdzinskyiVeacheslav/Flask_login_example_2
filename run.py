from blog import create_app, create_user

app = create_app()

if __name__ == '__main__':
    create_user()
    app.run(debug=True)

from app import create_app

#INSTANTIATE THE APP

app =create_app()


#RELOAD  EXECUTION IN CASE OF ERROR TO DEBUG MODE

if __name__ == "__main__":
    app.run(debug=True)

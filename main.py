from website import create_app

app = create_app()

#run flask app, start web server, any change to code will rerun web server
#automatic debugger
#entry point for app

if __name__ == '__main__':
    app.run(debug=True) #execute this line ONLY if we run this file



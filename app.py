from flask import Flask, render_template, request  # NOT the same as requests 
from github_api import get_github_user
app = Flask(__name__)

@app.route('/') #home page
def homepage():
    return render_template('index.html')

@app.route('/get_user')
def get_user_info():
    #get info from github api, displays on page
    print('form data is', request.args)
    username = request.args.get('username') #returns none if no username
#    username = request.args['username'] is more common, errors if there is no username
    user_info, error_message = get_github_user(username) #returns a dict
    if error_message:
        return render_template('error.html', error=error_message)
    else:
        return render_template('github.html', user_info=user_info)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, session, redirect
app = Flask(__name__)  
app.secret_key = 'this is a secret key'  
@app.route('/')          
def counter():
    if "counter" not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template ('counter.html')  

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect ('/')

@app.route('/addition')
def addition():
    session['counter'] += 1
    return redirect ('/')

@app.route('/reset')
def reset():
    if session['counter'] > 1:
        session['counter'] = 0
    return redirect('/destroy_session')








if __name__=="__main__":      
    app.run(debug=True)    


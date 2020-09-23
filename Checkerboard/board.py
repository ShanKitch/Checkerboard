from flask import Flask, render_template
app=Flask(__name__)

@app.route ("/")
def initial_render():
    return render_template('checkerboard.html')

@app.route("/<x>/<y>")
def box(x,y):
    return render_template('checkboard.html', x=int(x), y=int(y))

@app.route('/<x>/<y>/<c1>/<c2>')
def resize_with_color(x, y, c1, c2):
    return render_template('checkboard.html', x=int(x), y=int(y), color1=c1, color2=c2)

if __name__ == "__main__":
    app.run(debug = True)
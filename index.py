from flask import Flask, render_template, request

app = Flask(__name__)

images = ['static/images/Artceram.jpg', 'static/images/AXOR.jpg', 'static/images/AZZURRA.jpg']
counter = 0


@app.route('/', methods=['GET', 'POST'])
def news():
    global counter
    print(request.method)
    if request.method == 'POST':
        img = request.files['file']
        name = f'static/images/user_images_{counter}.jpg'
        counter += 1
        with open(name, 'wb') as f:
            f.write(img.read())
        images.append(name)
    return render_template('header.html', title='Миссия колонизации марса', images=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

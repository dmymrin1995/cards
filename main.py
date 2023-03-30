from flask import Flask, render_template, request

import pandas as pd
import random as rnd

app = Flask(__name__)
CARD_PATH = 'img/cards/'
data = list(pd.read_csv('static/card.csv').T.to_dict().values())
rnd.shuffle(data)
pile1 = data[:27]
pile2 = data[27:54]
pile3 = data[54:]

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cards')
def index():
    i = 0
    pile1_face, pile1_back = pile1[i+1]['face_img'], pile1[i]['back_img']
    pile2_face, pile2_back = pile2[i+1]['face_img'], pile2[i]['back_img']
    pile3_face, pile3_back = pile3[i+1]['face_img'], pile3[i]['back_img'] 
    path_pile1_face, path_pile1_back = CARD_PATH + pile1_face,  CARD_PATH + pile1_back
    path_pile2_face, path_pile2_back = CARD_PATH + pile2_face,  CARD_PATH + pile2_back
    path_pile3_face, path_pile3_back = CARD_PATH + pile3_face,  CARD_PATH + pile3_back
    return render_template('array.html', 
                           index=i, 
                           pile1_face = path_pile1_face, 
                           pile1_back = path_pile1_back,
                           pile2_face = path_pile2_face, 
                           pile2_back = path_pile2_back,
                           pile3_face = path_pile3_face, 
                           pile3_back = path_pile3_back
                           )

@app.route('/cards/next', methods=['POST'])
def next_item():
    i = int(request.form['index']) + 1
    pile1_face, pile1_back = pile1[i+1]['face_img'], pile1[i]['back_img']
    pile2_face, pile2_back = pile2[i+1]['face_img'], pile2[i]['back_img']
    pile3_face, pile3_back = pile3[i+1]['face_img'], pile3[i]['back_img'] 
    path_pile1_face, path_pile1_back = CARD_PATH + pile1_face,  CARD_PATH + pile1_back
    path_pile2_face, path_pile2_back = CARD_PATH + pile2_face,  CARD_PATH + pile2_back
    path_pile3_face, path_pile3_back = CARD_PATH + pile3_face,  CARD_PATH + pile3_back
    if i >= len(pile1):
        i = 0
    return render_template('array.html', 
                           index=i, 
                           pile1_face = path_pile1_face, 
                           pile1_back = path_pile1_back,
                           pile2_face = path_pile2_face, 
                           pile2_back = path_pile2_back,
                           pile3_face = path_pile3_face, 
                           pile3_back = path_pile3_back
                           )
    
if __name__ == '__main__':
    app.run(debug=True)
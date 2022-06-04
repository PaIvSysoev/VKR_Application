#прогноз показателя "Прочность при растяжении"
import flask
from flask import render_template
import pickle
import sklearn

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])

def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open('vkr_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        f1 = float(flask.request.form['Соотношение матрица-наполнитель'])
        f2 = float(flask.request.form['Плотность, кг/м3'])
        f3 = float(flask.request.form['модуль упругости, ГПа'])
        f4 = float(flask.request.form['Количество отвердителя, м.%'])
        f5 = float(flask.request.form['Содержание эпоксидных групп,%_2'])
        f6 = float(flask.request.form['Температура вспышки, С_2'])
        f7 = float(flask.request.form['Поверхностная плотность, г/м2'])
        f8 = float(flask.request.form['Модуль упругости при растяжении, ГПа'])
        f9 = float(flask.request.form['Потребление смолы, г/м2'])
        f10 = float(flask.request.form['Угол нашивки, град'])
        f11 = float(flask.request.form['Шаг нашивки'])
        f12 = float(flask.request.form['Плотность нашивки'])

        y_pred = loaded_model.predict([[f1, f2, f3, f4, f5, f6,
                                        f7, f8, f9, f10, f11, f12]])

        return render_template('main.html', result=y_pred)

if __name__ == '__main__':
    app.run()

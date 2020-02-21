import dash

from layout import layout
from router import call_back

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = layout.index_layout


# APP_MODE == "DEBUG" => load model inside
# APP_MODE != "DEBUG" => load model outside
APP_MODE = "DEBUG"
filePath_preTrainModel = 'pre-Train_model/my_customNetV3.h5'

call_back.register_callback(app, APP_MODE, filePath_preTrainModel)

if __name__ == '__main__':
    app.run_server(debug=APP_MODE == "DEBUG", threaded=APP_MODE == "DEBUG")

import dash
from dash.dependencies import Input, Output, State

from layout import layout
from preprocess import preprocess
from inference import inference

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = layout.index_layout

filePath = 'pre-Train_model/my_customNetV3.h5'

# APP_MODE == "DEBUG" => load model inside
# APP_MODE != "DEBUG" => load model outside
APP_MODE = "DEBUG"

if APP_MODE != "DEBUG":
    model = inference._load_model(filePath)

@app.callback(Output('output-image-upload', 'children'),
              [Input('upload-image', 'contents')],
              [State('upload-image', 'filename')])
def update_output(contents, filenames):
    global model, labelNames, APP_MODE
    if contents is not None:

        image = preprocess.process_image(contents)
        shape = image.shape

        # processing input image to (1, 32, 32, 3)
        InputModel_image = preprocess.prepare_model_input(image)

        # loading model
        if APP_MODE == "DEBUG":
            model = inference._load_model(filePath)
        
        predictLabel = inference.predict(InputModel_image, model)
        
        if APP_MODE == "DEBUG":
            # Clear session
            inference.debug_mode_clear_session()

        children = [
            layout.parse_contents(contents, filenames, shape, predictLabel)
        ]
        return children

if __name__ == '__main__':
    app.run_server(debug=APP_MODE == "DEBUG", threaded=APP_MODE == "DEBUG")

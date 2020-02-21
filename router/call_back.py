import dash
from dash.dependencies import Input, Output, State

from layout import layout
from preprocess import preprocess
from inference import inference

def register_callback(app, _APP_MODE, filePath_preTrainModel):
    APP_MODE = _APP_MODE
    filePath = filePath_preTrainModel
    
    if APP_MODE != "DEBUG":
        model = inference._load_model(filePath)
    @app.callback(Output('output-image-upload', 'children'),
              [Input('upload-image', 'contents')],
              [State('upload-image', 'filename')])
    def update_output(contents, filenames):
        nonlocal model
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
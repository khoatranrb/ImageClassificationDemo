import dash_html_components as html
import dash_core_components as dcc
index_layout = html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Dop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-image-upload'),
])

def parse_contents(contents, filename, shape, predictName):
    return html.Div([
        html.H5(filename),
        html.H6('Shape: ' + str(shape[0]) + ' x ' + str(shape[1])
                + ' x ' + str(shape[2])),
        html.H2(predictName),
        html.Img(src=contents),
        html.Hr(),
        html.Div('Raw Content'),
    ])
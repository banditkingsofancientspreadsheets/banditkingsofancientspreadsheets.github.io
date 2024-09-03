import plotly.graph_objects as go
import plotly.io as pio


# Specify Custom Color Map for NVIDIA
nvidia_colors = ['rgb(118, 185, 0)',
                 'rgb(0,113,197)',
                 'rgb(0,133,100)',
                 'rgb(93,22,130)',
                 'rgb(137,12,88)',
                 'rgb(250,194,0)',
                 'rgb(94,94,94)']

nvidia_fonts = 'NVIDIA Sans, Helvetica, Sans-serif'

pio.templates["nvidia"] = go.layout.Template(
    # LAYOUT
    layout = {
        # Fonts
        # Note - 'family' must be a single string, NOT a list or dict!
        'title':
            {'font': {'family': nvidia_fonts,
                      'size':25,
                      'color': '#333'}
            },
        'font': {'family': nvidia_fonts,
                      'size':16,
                      'color': '#333'},
        # Colorways
        'colorway': nvidia_colors,
        # Keep adding others as needed below
        'hovermode': 'x unified'
    },
    # DATA
    data = {
        #Each graph object must be in a tuple or list for each trace
        # 'bar': [go.Bar(texttemplate = '%{value:$.1f}',
        #                textposition='none',
        #                textfont={'family': nvidia_fonts,
        #                          'size': 20,
        #                          'color': '#FFFFFF'
        #                          })]
    }
)

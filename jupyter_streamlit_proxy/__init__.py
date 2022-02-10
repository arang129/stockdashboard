"""
Return config on servers to start for streamlitlab

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os

def setup_streamlit_proxy():
    return {
        'command': [
            "streamlit",
            "hello",
            "--browser.serverAddress", "0.0.0.0",
            "--server.enableCORS", "False",
            "--server.headless", "True",
            "--server.port", "{port}",
#            "run",
#            "streamlit_app.py",
        ],
        'environment': {},
        'launcher_entry': {
            'title': 'streamlit',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'streamlit-favicon.svg')
        }
    }

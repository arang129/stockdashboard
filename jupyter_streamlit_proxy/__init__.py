"""
Return config on servers to start for streamlitlab

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os

def setup_streamlit_proxy():
    #cookieSecret="P59nUp2LN9AjawT0"
    return {
        'command': [
            "streamlit",
            "run",
            "--browser.serverAddress", "0.0.0.0",
            "--server.port", "{port}",
            "--server.headless", "true",
            #"--server.cookieSecret", cookieSecret,
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false",
            "--server.maxUploadSize", "32",
            "--server.maxMessageSize", "32",
            "webapp.py",
        ],
        'environment': {},
        'launcher_entry': {
            'title': 'streamlit',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'streamlit-favicon.svg')
        }
    }

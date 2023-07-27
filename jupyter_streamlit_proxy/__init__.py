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
            "/home/jovyan/run_streamlit.sh",
            "--browser.gatherUsageStats", "false",
            "--browser.serverAddress", "0.0.0.0",
            "--server.port", "{port}",
            "--server.headless", "true",
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false",
            #"--server.cookieSecret", cookieSecret,
            #"--server.maxUploadSize", "50",
            #"--server.maxMessageSize", "50",
        ],
        'environment': {},
        'timeout': 30.0,
        'launcher_entry': {
            'title': 'streamlit',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'streamlit-favicon.svg'),
        }
    }

def setup_httpserver_proxy():
    return {
        'command': [
            "python3", "-m", "http.server", "{port}"
        ],
        'environment': {},
        'timeout': 30.0,
        'launcher_entry': {
            'title': 'httpserver',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'streamlit-favicon.svg'),
        }
    }


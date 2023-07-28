"""
Return config on servers to start for streamlitlab

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os

# proxy for Streamlit
def setup_streamlit_proxy():
    return {
        'command': [
            "/home/jovyan/run_streamlit.sh",
            "--browser.gatherUsageStats", "false",
            "--browser.serverAddress", "0.0.0.0",
            "--server.port", "{port}",
            "--server.headless", "true",
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false",
        ],
        'environment': {},
        'timeout': 30.0,
        'launcher_entry': {
            'title': 'streamlit',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'streamlit-favicon.svg'),
        }
    }

# another proxy to enable efficient downloading of files
def setup_download_proxy():
    return {
        'command': [
            "python3", "-m", "http.server", "{port}"
        ],
        'environment': {},
        'timeout': 30.0,
        'launcher_entry': {
            'title': 'download',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'generic-download-icon.svg'),
        }
    }


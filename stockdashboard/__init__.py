"""
Return config on servers to start web services from JupyterLab

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""

import os


def setup_stockdashboard():
    """
    Proxy wrapper to launch Streamlit from JupyterHub on Binder

    Note that a shell script that launches the actual Streamlit application is expected at
    /home/jovyan/run_streamlit.sh
    The script must accept additional command line flags being passed to streamlit, see below.
    """
    return {
        'command': [
            "streamlit", "run", "/home/jupyter-data/webapp/stockdashboard.py",
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
            'title': '股價觀測',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'stockdashboard.svg'),
        }
    }

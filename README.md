# Simple proxy that allows to run Streamlit on top of Jupyter/Binder

This small package was adapted from

https://jupyter-server-proxy.readthedocs.io/en/latest/convenience/new.html

It launches and exposes Streamlit via the directory 'streamlit',
thereby enabling Streamlit-based web applications being launched on
top of an existing Binder infrastructure.
In addition it provides a button within JupyterLab to launch
a Streamlit web app via the GUI.

As the entry point for the launch it expects a script at
'/home/jovyan/run_streamlit.sh' which has the actual streamlit
command inside, including the actual file name of the web application.

A usage example is available here:

https://gitlab.mpcdf.mpg.de/MPIBP-Hummer/glycoshield-md


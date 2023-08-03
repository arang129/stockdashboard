# jupyter-streamlit-proxy : A proxy that enables Streamlit on top of JupyterLab/Binder

jupyter-streamlit-proxy exposes and launches Streamlit via the relative URL
'streamlit', thereby enabling Streamlit-based web applications being launched
on top of an existing Binder infrastructure.  In addition it provides a button
within JupyterLab to launch a Streamlit web app via the GUI.

As the entry point for the webapp launch it expects a script at

`/home/jovyan/run_streamlit.sh`

which has the actual streamlit launch command inside,
including the actual file name of the web application.

A usage example is available here:

https://gitlab.mpcdf.mpg.de/MPIBP-Hummer/glycoshield-md

The package is provided as-is, see 'LICENSE'.

This package was adapted from
https://jupyter-server-proxy.readthedocs.io/en/latest/

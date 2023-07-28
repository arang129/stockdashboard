# jupyter-streamlit-proxy : A proxy that enables Streamlit on top of JupyterLab/Binder

jupyter-streamlit-proxy exposes and launches Streamlit via the relative URL
'streamlit', thereby enabling Streamlit-based web applications being launched
on top of an existing Binder infrastructure.  In addition it provides a button
within JupyterLab to launch a Streamlit web app via the GUI.

As the entry point for the webapp launch it expects a script at

`/home/jovyan/run_streamlit.sh`

which has the actual streamlit command inside,
including the actual file name of the web application.

In addition to the Streamlit proxy, a second proxy is installed that runs the
simple internal Python http server to expose the working directory for
downloading files. This is a workaround since the Streamlit-internal download
button uses buffering in memory which breaks, starting from a certain size.

A usage example is available here:

https://gitlab.mpcdf.mpg.de/MPIBP-Hummer/glycoshield-md

The package is provided as-is, see 'LICENSE'.
This package was adapted from
https://jupyter-server-proxy.readthedocs.io/en/latest/

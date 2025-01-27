import setuptools

setuptools.setup(
    name="jupyter-streamlit-proxy",
    version='0.0.3',
    url="https://gitlab.mpcdf.mpg.de/khr/jupyter-streamlit-proxy",
    author="Klaus Reuter",
    description="klaus.reuter@mpcdf.mpg.de",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'streamlit = jupyter_streamlit_proxy:setup_streamlit_proxy',
        ]
    },
    package_data={
        'jupyter_streamlit_proxy': ['icons/*'],
    },
)

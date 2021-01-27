#!/bin/bash
sudo rm /usr/local/lib/python3.8/dist-packages/streamlit/static/static/css/main.134c989d.chunk.css
sudo rm /usr/local/lib/python3.8/dist-packages/streamlit/static/static/js/main.8e5e11c8.chunk.js
sudo rm /usr/local/lib/python3.8/dist-packages/streamlit/static/assets/streamlit.css
sudo rm /usr/local/lib/python3.8/dist-packages/streamlit/static/index.html
sudo rm /usr/local/lib/python3.8/dist-packages/streamlit/report_thread.py

sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/static/static/css/main.134c989d.chunk.css /usr/local/lib/python3.8/dist-packages/streamlit/static/static/css/main.134c989d.chunk.css
sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/static/static/js/main.8e5e11c8.chunk.js /usr/local/lib/python3.8/dist-packages/streamlit/static/static/js/main.8e5e11c8.chunk.js
sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/static/assets/streamlit.css /usr/local/lib/python3.8/dist-packages/streamlit/static/assets/streamlit.css
sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/static/index.html /usr/local/lib/python3.8/dist-packages/streamlit/static/index.html
sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/report_thread.py /usr/local/lib/python3.8/dist-packages/streamlit/report_thread.py

sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/static/static/js/quantml-init.js /usr/local/lib/python3.8/dist-packages/streamlit/static/static/js/quantml-init.js
sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/static/static/js/quantml.js /usr/local/lib/python3.8/dist-packages/streamlit/static/static/js/quantml.js
sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/static/favicon.png /usr/local/lib/python3.8/dist-packages/streamlit/static/favicon.png

sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/static/img/cover.webp /usr/local/lib/python3.8/dist-packages/streamlit/static/img/cover.webp
sudo cp ./Streamlit-Changes/Python38/Lib/site-packages/streamlit/static/img-dark/cover.webp /usr/local/lib/python3.8/dist-packages/streamlit/static/img-dark/cover.webp

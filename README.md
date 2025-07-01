# cosmotic

A Django app for managing candles and room sprays.

##Setup Using Virtual Environment

```cmd
python -m venv venv
source venv/bin/activate       # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

docker setup:
docker build -t queensql/cosmotic-app .
docker run --name cosmotic-container -p 8000:8000 queensql/cosmotic-app


HTML documentation generated using Sphinx is located in:
docs/build/html/index.html

<<<<<<< HEAD
# Cosmotic

A Django app for managing and displaying products such as candles and room sprays.
=======
# cosmotic

A Django app for managing candles and room sprays.
>>>>>>> e0b93fe (Save local changes before rebase)

##Setup Using Virtual Environment

<<<<<<< HEAD
## Setup Using Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Django development server
python manage.py runserver
=======
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
>>>>>>> e0b93fe (Save local changes before rebase)

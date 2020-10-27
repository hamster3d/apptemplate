
# Python web app template
Features:
* Uses Flask
* Uses Flask REST Plus to build REST API
* *(optional)* Uses Docker
* *(optional)* Heroku app (Docker workflow)

## Setup
If you need some environment variables set, use `.env` file.
For example ifwe are going to use AWS S3.
Create `.env` file with the following contents:
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
S3_BUCKET=
```
## Installation

It is always a good idea to create a virtual environment
```bash
python3 -m venv venv
```
It will create a `venv` directory with isolated copy of Python
To activate the created virtual environment run
```bash
source venv/bin/activate
```
After virtual environment activation we don't need to use `python3` and `pip3`, we can normally use `python` and `pip`

Update pip
```bash
pip install --upgrade pip
```
Install dependencies
For deployment.
```bash
pip install -r requirements.txt
```

## Run server api localy
Development server
```bash
python api/app.py --debug
```
Open browser at the address shown.
The `debug` options force the server automatically reload the app if any sources are changed.

Alternatively run via gunicorn (as it run on Heroku)
```bash
cd api
gunicorn --bind 0.0.0.0:5000 app:app
```
## Docker
### Build
```bash
docker build -t appname:latest .
```
### Run
```bash
docker run -t -i --env-file .env -p 5000:5000 -e PORT=5000 appname:latest
```

## Deploy on Heroku
Option 1. Locally build docker image and push it to Heroku
```bash
heroku container:push web --app herokuappname
heroku container:release web --app herokuappname
```
Option 2. Remotely build on Heroku
```bash
git push heroku master
```

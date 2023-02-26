# django-rest-apikey-auth

An application that use [Simple REST API Key package](https://github.com/koladev32/djangorestframework-simple-apikey) for authentication. 

## Project Setup 

Create a `.env` file with the following command.

```bash
cp .env.example .env
```

Use the `python manage.py generate_fernet_key` to generate a value for the `fernet` key.

### Directly

Create a python virtual environment. 

```bash
python3.11 -m venv venv
```

Then, install the dependencies and run the migrations.

```bash
pip install -r requirements.txt
python manage.py migrate
```

Then start the server. 

```bash
python manage.py runserver
```

The server will start on http://localhost:8000.

### Docker

First you need to build an image. 

```bash
docker build -t django-api-key .
```

Then run a container with the create image. 

```bash
docker container run -p 8000:8000 django-api-key --env-file=.env
```

Happy coding!🚀

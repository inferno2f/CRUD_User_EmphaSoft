# CRUD_User_EmphaSoft
Test task for a Junior Python position at EmphaSoft

## Deploy project locally

 1. Clone the project 
 ```git clone <insert_your_link>```
 
 2. Switch to the project folder and create virtual environment 
 ```python3 -m venv env```

 3. Activate virtual env and install all packages
 `. env/bin/activate`
 
 `pip install -r requirements.txt`

 4. Swith to ```app/``` directory and make migrations

 ```python manage.py makemigrations```

 ```python manage.py migrate```

 5. Start the server

 ```python manage.py runserver```


## API documentation

 All available endpoints, request methods and models can be found in the docs section: 
 
 http://127.0.0.1:8000/swagger/

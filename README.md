# TalkOut


Welcome to TakOut. It built using Django, Python, and Bootstrap. It allows users to post their thoughts (*referred to as "talks*"), create unique usernames and passwords, and build personalized profiles including details such as name, mobile number, email, bio, and profile picture. Users also have the ability to edit and delete their own user accounts. Additionally, users can view other people's profiles, like and unlike talks, and view recently added talks on the homepage.


## Features

- *User Authentication:* Users can create unique usernames and passwords to access the platform.
- *Profile Building:* Users can build their profiles by adding details such as name, mobile number, email, bio, and upload a profile picture.
- *Talks Posting:* Users can post their thoughts, referred to as "talks".
- *User Account Management:* Users have the ability to edit and delete their own user accounts.
- *View Other Profiles:* Users can view profiles of other users who have created accounts.
- *Like/Unlike Talks:* Users can like and unlike talks posted by others.
- *Recent Talks Display:* Recently added talks are displayed on the homepage.
- *CRUD Operations:* Users can perform CRUD (Create, Read, Update, Delete) operations on their own talks.
- *Welcome Email for New Users:* A welcome email is sent to users whenever a new account is created. This feature is implemented using *Django Celery and signals*.

## Technologies Used

- Django Python framework
- Bootstrap
- Python Pillow Library
- Django Celery
- Redis

## Installation

1. Clone the repository:

```bash
  https://github.com/devanshptl/TalkOutProject.git

```

2. Create a virtual environment (optional but recommended):
```bash
 python -m venv venv
 ```

3. Activate the virtual environment:
  * On Windows:
  ```bash
  venv\Scripts\activate
  ```

* On macOS and Linux:
```bash
source venv/bin/activate
```


4. Navigate to the project directory:

```bash
cd TalkOut
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Email Configuration :


    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your-email@gmail.com'
    EMAIL_HOST_PASSWORD = 'your-email-password'
    DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
    ```


7. Apply migrations:
```bash
python manage.py migrate
```

8. Run the development server:
```bash
python manage.py runserver
```


9. Setup Celery and Start Celery Worker :
```bash
celery -A project3 worker --loglevel=info
```


   
10. Open your web browser and go to http://localhost:8000 to access the application.
   
## Usage

1. Register a new account with a unique username and password.
2. Build your profile by providing details such as name, mobile number, email, bio, and upload a profile picture.
3. Start posting your thoughts (talks) on the platform.
4. Explore other user profiles and like or unlike their talks.
5. View recently added talks on the homepage.
6. Edit or delete your own user account or talks as needed.

## Preview

- *Project Video*


## Contributing
We welcome any and all contributions! Here are some ways you can get started:
1. Report bugs: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.
2. Contribute code: If you are a developer and want to contribute, follow the instructions below to get started!
3. Suggestions: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or imporvements you would like to see!
4. Documentation: If you see the need for some additional documentation, feel free to add some!

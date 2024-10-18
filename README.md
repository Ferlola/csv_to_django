This project insert csv file into sqlite3 using pandas with django

### 📎 <span style="color: blue;">Features</span>:
-------------------------------------------------------
- Search field based on book title, author, publisher and price range.

### 🔍 <span style="color: blue;">Requirements</span>:
--------------------------------------------------------
- virtual environment (highly recommended)

### 🚀 <span style="color: blue;">Installation</span>:
--------------------------------------------------------
- Create virtual environment.
```
$ python3 -m venv .venv
```

- Activate virtual environment.
```
$ source .venv/bin/activate
```

- Install requeriments.
```
(.venv) $ pip3 install -r requirements.txt
```
- Run the project.
```
(.venv) $ python3 manage.py makemigrations
(.venv) $ python3 manage.py migrate
(.venv) $ python3 manage.py runserver
```

- Open browser.

<pre><a href="http://localhost:8000">http://localhost:8000</a></pre>
- Reload homepage to insert csv file into sqlite3

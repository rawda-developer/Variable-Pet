# Variable-Pet

## Introduction

Variable-Pet is an animal shelter adoption system. It enables the user to view pets details. It allows the admistrator to add, update, delete pets data using the Django admin interface.

## Dependencies

### 1. Backend Dependencies

Our tech stack will include the following:

- **virtualenv** as a tool to create isolated Python environments
- **PostgreSQL** as our database of choice
- **Python3** and **Django** as our server language and server framework
  You can download and install the dependencies mentioned above using `pip` as:

```
pip3 install django
```

## Development Setup

1. **Download the project starter code locally**

```
git clone https://github.com/rawda-developer/Variable-Pet.git
cd Variable-Pet
```

2. **Initialize and activate a virtualenv using:**

```
python -m virtualenv env
source env/bin/activate
```

**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:

```
source env/Scripts/activate
```

3. **Install the dependencies:**

```
pip3 install -r requirements.txt
```

4. **Run the development server:**

```
./manage.py runserver
```

6. **Verify on the Browser**<br>
   Navigate to project homepage [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://localhost:8000](http://localhost:8000)

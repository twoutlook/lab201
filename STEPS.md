
# Install python3.5 and python3.5-venv
    sudo apt-get install -y python3.5 python3.5-venv
    
# Create and activate myvenv

    python3.5 -m venv myvenv
    source myvenv/bin/activate
    
# Install django
    pip install django
    pip install --upgrade pip
    
# Create project mysite
    django-admin startproject mysite
    
    
    
# Run dev server on c9
    ./manage.py runserver $IP:$PORT
    
# Open a new terminal
    source myvenv/bin/activate
    cd mysite
    
    ./manage.py migrate
    
    ./manage.py createsuperuser
    ubuntu / Kunshan at 2016
    
    
    
# Migrage db
    ./manage.py makemigrations
    ./manage.py migrate
    
# Collect static
    ./manage.py collectstatic
    
# Visit admin and login

# Create app lab
    ./manage.py startapp lab


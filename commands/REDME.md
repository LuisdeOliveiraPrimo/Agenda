# Iniciar o projeto Django

python -m venv venv
.\venv\Scripts\activate
pip install django
django-admin startproject project .
python manage.py startapp contact

# Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore

git init
git add .
git commit -m 'Sua Mensagem'
git remote add origin URL_DO_GIT 
git push -u origin main   

# django superuser

python manage.py createsuperuser
python manage.py changepassword USERNAME
pyrhon manage.py changepassword USERNAME

# Migrando a base de dados do Django

python manage.py makemigrations
python manage.py migrate
Criando e modificando a senha de um super usuário Django


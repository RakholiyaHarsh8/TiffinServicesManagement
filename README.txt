Django Framworks
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built
by experienced developers, it takes care of much of the hassle of web development, so you can focus
on writing your app without needing to reinvent the wheel. It’s free and open source.
Install Django
You can install Django using pip, the Python package manager. Here are the steps to install Django:
1. Open your terminal or command prompt.
2. Type the following command to install Django: pip install django
3. Once the installation is complete, you can verify that Django has been installed correctly by typing th
e following command: python -m django --version
Django Project Structure
A Django project is structured into several directories and files. Here's an overview of the main components:
1. manage.py: This is the command-line utility that lets you interact with your Django project in
various ways (e.g., creating database tables, starting the development server, etc.).
2. projectname/: This is the root directory of your project, which contains the main project files
3. projectname/settings.py: This file contains project-wide settings and configuration options.
4. projectname/urls.py: This file defines the URL configuration for your project.
5. projectname/wsgi.py: This file is used to configure the WSGI application for
your project.

Create For SuperUser Account
You can create a superuser account using the following command:
python manage.py createsuperuser

Run For Project Client
You can run the project client using the following command:
python manage.py runserver
http://127.0.0.1:8000



New Admin Page Login:
http://127.0.0.1:8000/admin/ 
Run For Project Server 
You can run the project server using the following command:
python manage.py runserver

Old Admin Page Login:
You can access the admin page by visiting the following URL in your browser:
http://127.0.0.1:8000/admin/
UserName: admin
Password: 12345678







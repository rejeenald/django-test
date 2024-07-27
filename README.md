# django-portal-template

This open-source repository is to get started quickly with a portal-type application. 

Courtesy of www.buzzerboy.com

# Requirements

The following tools must be installed on your Windows machine:
1. Vagrant (https://www.vagrantup.com) - We use this as a virtualization tool to run linux as a development server
2. VisualStudio Code (https://code.visualstudio.com/) - We use this as an IDE
3. Docker (https://www.docker.com/) - We use this as a virtualization tool for deploying the QA and Production environments
4. Oracle VirtualBox virtualization environment (https://www.virtualbox.org/) - This is the underlying provider that Vagrant uses to support a virtualized development environment.

# Special Acknowledgements

In development of this portal template, I leveraged MIT Licensed AppSeed.us UI Aargon Dashboard Freeware.

# Directory Structure


```bash
$ /root/
```
> This is the root directory where you cloned the repository. You can name is what ever you like.

```bash
$ /root/environments
```
> This is the directory where the Vagrantfile and Vagrant setup is located. Vagrant is specifically helpful in setting up a linux based virtual environment. But,
> if you're using python on your Windows or Mac, then you can ignore this directory.

```bash
$ /root/Graphics
```
> This is the directory where the saw images are located for use within the portal. You can use it to store your raw images as well. Exported PNG or SVG files are located inside the static directory as described later on.

```bash
$ /root/portalapp
```
> This is the directory where the django project is located for the portal itself. 

```bash
$ /root/portalapp/apps
```
> This is the directory contains all the apps that are part of the project. If you add additional apps to your project, use django-admin here to add additional apps. 

```bash
$ /root/portalapp/core
$ /root/portalapp/apps/static/core
$ /root/portalapp/html5_ui/core
```
> These are the directories that contains all core functionality, static assets like CSS, JS etc and html5-based user interfacee of the portal. It is not recommended to update code in here. This is beacuse you can update the core as new version come to augment functionality for your portal.

```bash
$ /root/portalapp/html5_ui
```
> This is the directory contains the HTML5-based theme, and user-interfaces for the app. To create code-specialization segregation, this is where the front-end engineers can focus.

```bash
$ /root/portalapp/nginx
$ /root/portalapp/staticfiles
```
> These are system directories. If your hosting environment requires nginx, you can augment your context specific configuration in here.
> The staticfiles folder holds all the static files here if they are hosted on the app server.

```bash
$ /root/portalapp/apps/authentication
$ /root/portalapp/html5_ui/authentication

$ /root/portalapp/apps/sample
$ /root/portalapp/apps/html5_ui/sample

```
> These are applications supplied with this template. The sample app contains example views, models, and urls that demonstrate how to use this framework template. The authentication app faciliates secure user-login and related functionalities.

```bash
$ /root/portalapp/apps/main
$ /root/portalapp/static/main
$ /root/portalapp/html5_ui/main
```
> These are the main application directories that are for your context-specific system. This is like the core of your system. You can either develop your entire application in here, or add additional applications using django-admin startapp, but trigger them from main.

# Getting Started
> This project is designed to be operating system agnostic. It leverages Vagrant and VirtualBox-based virtualization environment to create development application server. Therefore, it is important to make sure that Vagrant is properly installed and operational.

```bash
Launch in Command Prompt or Terminal 
$ cd/to/the/root/directory
$ cd environments 

Launch Vagrant in terminal where we can run the development server
$ vagrant up
$ vagrant ssh

Depending on your system, you may have to wait pass the established time-out. 
$ vagrant ssh
$ cd /project_data/
$ cd portalapp

If you get an error here, then try these steps to shutdown vagrant and start it again, otherwise, skip these.
$ exit
$ vagrant halt
$ vagrant up
$ vagrant ssh

Continue if you did not get a directory not found error on cd portalapp, install the requirements using PIP:
$ pip install -r requirements.txt

Make migrations and collect static files
$ python3 manage.py makemigrations
$ python3 manage.py collectstatic --no-input

Enter 'yes' to continue loading up the static files.
$ python manage.py migrate
$ python manage.py runserver

Now open up a web-browser, and go to http://localhost/
```

# Starting a new portal project using this template framework

To start a new portal project, you must first create a new git repository where base off the code from here. Once you've created your own git repository, and cloned the code from here, you can then get started with the following steps:

## Configure Application Configuration Settings in Main Application
If you upgrade the portal template, you will only upgrade the core, so the main application is for your to use. Therefore you start by first updating the configuration in the main/apps.py
> /root/portapp/apps/main/apps.py

## Configure the database while in development
This area is still pending.

## Create a System Super User, and Load Seed Data in the Database
To run the application smoothly, some seed data has to be loaded. The core comes with some Seed Data already. To load seed data for core only:

```bash
$ python manage.py createsuperuser 

Follow the steps and create a user and give this user a strong password. This is the user account that will be used to create SeedData below

$ python3 manage.py shell
$ from core.SeedData.Loader import SeedDataLoader
$ SeedDataLoader.load(True)

Now, load application settings that we described earlier in Main App

$ from apps.main.apps load ApplicationSettings
$ ApplicationSettings.load()

```

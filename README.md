Django Article-Based Application

Site-Link : https://zeysnepk.pythonanywhere.com/

This project is a Django-based web application that allows users to create, edit, and delete articles. The articles can be about any topic, providing a flexible platform for content creation. This application is ideal for anyone looking to set up a personal blog or a simple content management system (CMS).

Features

Create Articles:
Users can add new articles on any topic.

Edit Articles:
Existing articles can be updated with new content.

Delete Articles: 
Users have the ability to remove articles that are no longer needed.

Rich Text Editing: 
Articles can include formatted text, images, and other media.

User Authentication: 
Secure login and registration system to manage content creation.

Getting Started

Prerequisites

!Before you start, ensure you have the following installed:

Python 3.x
Django 4.x
Virtualenv (optional but recommended)

Installation

Clone the Repository: 

-git clone https://github.com/zeysnepk/DJANGO.git

-cd DJANGO

Set Up a Virtual Environment:

-python -m venv env

-source env/bin/activate

Install Dependencies:

-pip install -r requirements.txt

Apply Migrations:

-python manage.py migrate

Create a Superuser:

-python manage.py createsuperuser

Run the Development Server:

-python manage.py runserver

Access the Application:
Open your web browser and go to http://127.0.0.1:8000/ to see the application in action.

Usage

Creating a New Article
1. Log in to the application using your credentials.
2. Navigate to the "Add Article"(PANEL) page.
3. Enter the title, content, and any images you'd like to include.
4. Click "Save" to publish the article.

Editing an Article
1. Go to the article you want to edit.
2. Click the "Edit" button.
3. Make your changes to the content.
4. Click "Save" to update the article.

Deleting an Article
1. Navigate to the article you want to delete.
2.Click the "Delete" button.
3.Confirm the deletion when prompted.

File Structure
/articles: Contains the main application logic, including views, models, and URLs.
/templates: HTML templates for rendering the frontend of the application.
/static: Static files like CSS, JavaScript, and images.
/media: Directory for user-uploaded content like images.


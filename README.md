# TUNEWS

TüNews International data back end for Integreat.

These apps offer a user interface to create, edit or delete messages (news), which can be retrieved via an simple [API](api.md).

## Dependencies

* You can use Ubuntu 18.04
  * Also Windows or [WSL](https://docs.microsoft.com/de-de/windows/wsl/install-win10) or other distributions maybe possible
* install python3
    * sudo apt-get install pyhton3
    * sudo apt-get install python3-pip
    * if an error occur, maybe run: sudo sh -c 'apt update && apt upgrade'
* install virtual env for python
    * sudo apt-get install python3-venv
* install sqlite3 for developing
    * 

## Setup

* clone the repository in your workspace
* change in the project folder
    * cd tunews/
* Create a virtual environment
    * python3 -m venv .venv
* Activate the virtual envoironment
    * source .venv/bin/activate
* run setup.py for development
    * python3 setup.py develop
* Migrate the project
    * manage.py migrate
* Create a superuser for testing
    * manage.py createsuperuser
* Run the demo server
    * manage.py runserver

## Usage

After starting the server you can reach the user interace via http://localhost:8001/admin/ and log in with the previus created superuser.

There you are able to create **groups** or **users** and gave them required permissions to interact with the system.

You can also add **News**, **News-Categories** and **Languages**.

Over the [API](api.md) you can access the stored data.

## General

### News - item overview

A news item has a **title**, **content**, **e-news-number** (a unique number I guess), **datetime**, **news-category** and **language**.

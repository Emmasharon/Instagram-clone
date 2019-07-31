# Instagram-Clone

## Description
A django application where a user can create an account, login and share photos with other users. The users can also like and comment on ther people's pictures.

#### Link to deployed site
https://Instagram254.herokuapp.com/

## Table of content
1. [Description](#description)
2. [Setup and installations](#setup-and-installations)
3. [Contributing](#contributing)
4. [Bugs](#bugs)
5. [Contact me](#support-and-contact-details)
6. [Licensing](#license)

## BDD
| Behavior           | Input                 | Outcome                            |
| -------------------|-----------------------| -----------------------------------|
| request page       | click horuku link url | view images          |                    
|sign up      | registration form  | login page         |
|login        | login form  | timeline page         |
|view images accorging | click on timeline  |    user goes to page containing all images|  

## Setup and installations

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django

#### Clone the Repo and rename it to suit your needs.
```bash
git clone git@github.com:emmasharon/Instagram-clone.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <https://github.com/Emmasharon/Instagram-clone.git>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:5000](http://127.0.0.1:5000/)


## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs
None

#### Known bugs
 - N/A



## Support and contact details
Contact [Emmasharon](emmasharon19@gmail.com) for further help/support

### License

The project is licensed under MIT license https://opensource.org/licenses/MIT
Copyright (c) 2019, emma
Emmasharon/Instagram-clone


Copyright (c)2018 **Emmasharon**

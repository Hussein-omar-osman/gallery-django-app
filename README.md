## Gallery-Web-App

This is a Gallery Web-App page which shows several pictures in collection with the location it was taken and also description of picture.Once you click any picture, you will be able to find all its description there.

## Author Information

Written by Hussein Omar.

## Installation

Clone the repository
Create a virtual environment
Install Django and other requirements in my requirements.txt file in your repository folder
Run the IP address on the browser

## User Stories

These are the behaviours/features that the application implements for use by a user.

As a user I would like to:

- Can upload images to the web app
- Can view the already uploaded images in the web app
- Can search images with location , name and categories
- Can copy the images address to his or her clipboard to share with others

## Behaviour Driven Development

| Behavior      | Input description | Output description                            |
| ------------- | ----------------- | --------------------------------------------- |
| Upload image  | None              | The image will be posted to the home page     |
| Search images | None              | Results will be displayed on the results page |

## SetUp / Installation Requirements

### Prerequisites

- python3.10.4
- pip
- virtualenv

## Running the Application

- Creating the virtual environment

        $ python3.10.4 -m venv --without-pip env
        $ source env/bin/activate

- Installing Django

        $ python3.10.4 -m pip install Django
        $ python3.10.4 -m pip install cloudnary
        $ python3.10.4 -m pip install psycopg2

## Technologies Used

- Python3.10.4
- Django
- Bootstrap
- Javascript

Live Link: > https://breezway-gallery.herokuapp.com/

## Contact Information

To reach me, email me at: > husseinomar6190@gmail.com

License
MIT License

Copyright (c) [2022] [**Hussein Omar**]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

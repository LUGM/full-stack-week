## Deploy on [Heroku](https://heroku.com)

- Sign Up
- Create a new app, fill up the details
- Create a `Procfile`, similar to one in this repo.
    - The `Procfile` structure is as follows
    `web: gunicorn API:app` where `API` is the python file and `app` is the name of Flask object
- Run `pip install -r requirents.txt`
- Push your code to your github repo
- Attach your github repo to your heroku app under the 'Deploy' section
- See your code get deployed!

> Do not clone and deploy this repo, it won't work. Make sure you have the Procfile and the python file in the root of the repo
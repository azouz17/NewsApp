Group 13

Group Members - What they were assigned and some of the things they completed throughout development

Yassin Ezzat Mostafa Soubhi M Awad - Assigned Backend. Created the backend, such as: the models needed and majority of the views as well as other facets of the backend, fixing and restructuring where needed as the project developed. Also worked on favouriteArticles in frontend and fixes to article and account page.

Mostafa Mohamed Azouz Salama Abdelmaksoud - Assigned Frontend.
Created frontend pages( html, tailwind and typescript), mainPage,expandedArticle,Account
Made the interfaces 
Created and setup pinia stores
Got the edit and delete comment working
Editing a user( apart from profile picture and fav categories)

Charles Copas - Assigned working on both with a greater focus on frontend. 
Adding comments and viewing comments
Beginning of edit and deleting comments
Articles on main page.
Setting up openshift and github.
Created and changed views depending on requests from the frontend so that they are correctly handled based on how methods were created in the frontend and vice versa. 
Creating forms
ExpandedArticle page


A lot of the work was interchangeable with different people testing and providing minor updates/fixes for different features

Admin Account:
Username - admin
Password - admin

Test User Accounts
1
Username: charlie
Password: charlie
2
Username: malak
Password: malak123
3
Username: Thomas
Password: th123
4
Username: Bob
Password: BobBob
5
Username: Katie
Password: Katie32


Openshift URL - https://group13-web-apps-ec21391.apps.a.comp-teach.qmul.ac.uk 
Worked in terms of building successfully and directing you to login however once this occurred run into problems not encountered locally

Running locally
After using python manage.py runserver and npm run dev, use the development server link generated using django with python manage.py runserver.


# Template for ECS639U Group Coursework

This template should be used as the starting point for your group coursework in the module ECS639U Web Programming (at Queen Mary University of London). Use Git (github.qmul.ac.uk) to collaborate on the coursework with your group members. Module leader: Paulo Oliva <[p.oliva@qmul.ac.uk](mailto:p.oliva@qmul.ac.uk)>

## Local development

To run this project in your development machine, follow these steps:

1. Create and activate a conda environment

2. Download this repo as a zip and add the files to your own private repo.

3. Install Pyhton dependencies (main folder):

    ```console
    $ pip install -r requirements.txt
    ```

4. Create a development database:

    ```console
    $ python manage.py migrate
    ```

5. Install JavaScript dependencies (from 'frontend' folder):

    ```console
    $ npm install
    ```

6. If everything is alright, you should be able to start the Django development server from the main folder:

    ```console
    $ python manage.py runserver
    ```

7. and the Vue server from the 'frontend' sub-folder:

    ```console
    $ npm run dev
    ```

8. Open your browser and go to http://localhost:5173, you will be greeted with a template page.

## OpenShift deployment

Once your project is ready to be deployed you will need to 'build' the Vue app and place it in Django's static folder.

1. The build command in package.json and the vite.config.ts files have already been modified so that when running 'npm run build' the generated JavaScript and CSS files will be placed in the mainapp static folder, and the index.html file will be placed in the templates folder:

    ```console
    $ npm run build
    ```

2. You should then follow the instruction on QM+ on how to deploy your app on EECS's OpenShift live server.

## License

This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to [CC0](http://creativecommons.org/publicdomain/zero/1.0/).

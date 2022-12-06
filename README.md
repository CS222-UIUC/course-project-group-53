# course-project-group-53
course-project-group-53 created by GitHub Classroom

Summary: We wanted to create a website that was easy to access for students across campus where they can easily find recipes for their dietary necessities
and preferences. We found that a lot of students struggle with ideas on what to make at home, so we created a website that provides three complete recipes
(as a sample) for each dietary restriction, which include dairy free, gluten free, vegetarian, and no dietary preference. The way our website works is that
first it takes the user to the log in page and once the user has put in their information, they hit submit and it takes them to the home page. On the home
page, there are 4 buttons for preferences. Once one of the buttons is clicked, it takes the user to another page which has three recipes on it. 

Technical Architecture: With the log in information, we have used SQL Server Management Studio in order to make a link between the log in information and
the database. For the recipe pages, we used the Django framwork and Python/HTML to take signals from the buttons on the home page and link to the correct
recipe pages. For the log in page, we want to store the users preferences by linking it to their email in the databse. We used Python/HTML, flask, and 
Django for the user models. In our user model, we have stored an id, email, password, and first name and the fields are columns in the database.

Reproducible Installation: We imported flask, Django, PyLint, and pip in order to make our website work. First, we created the log in page, then the main
and recipe pages. After making the separate pages, we created a link between them. Lastly, we attached the log in information to the database.

Group Members and Roles: 
  Rucha- Part of front end and created each page and their functionalities 
  Twinkle- Part of front end and created each page and their functionalities
  Aarya- Part of back end and worked with database and connecting page to page
  Jennifer- Part of back end and worked with database and connecting page to page

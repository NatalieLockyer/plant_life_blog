# [Plant Life](https:)
(Developer: Natalie Lockyer)

## Demo
[To view live website, click here](https:)

# Purpose of the Project
Plant Life is a ficticious website dedicated to sharing plant based recipes and health benefits with with its followers. The website has been designed to to inform users of how beneficial it is to switch to a plant-based diet. Not only is it great for your health, the recipes are delicious too. 
This is a full stack frame work built using the Django framework. The wesbsite provides its followers with an 'about us' page, a benefits page, a recipes page which can be filtered into categories so the user doesnt have to wade through all the recipes if they just wanted a breakfast recipe. Users can also comment on the recipes, edit and delete their comment. Users are required to register in order to comment. 

# Contents
+ [User Experience](#user-experience)
    + [Key Project Goals](#key-project-goals)
    + [Target Audience](#target-audience)
    + [User Requirements and Expectations](#user-requirements-and-expectations)
    + [User Stories](#user-stories)
    + [Wireframes]
    + [Entity Relationship Diagram (ERD)](#entity-relationship-diagram)
+ [Design](#design)
    + [Typography ](#typography)

+ [Features](#features)
    + [Main Start Page](#main-start-page)
    + [About Me Pageg](#about-me-page)
    + [Benefits Page](#benefits-page)
    + [Recipe Page](#recipe-page)
    + [Method Page](#method-page)
    + [Category Page](#category-page)
    + [SignUp Page](#signup-page)
    + [Logout Page](#log-out-page)
    + [Login Page](#login-page)
    + [Comments Section](#comments-section)
+ [Future Features](#future-features)
+ [Technologies Used](#technologies-used)
    + [Languages Used](#language)
    + [Frameworks Used](#frameworks-and-tools)
   


+ [Testing](#testing)
  + [Code Validation](#code-validation)
  + [Full Testing](#full-testing)
  + [Bugs](#bugs)
  + [Supported Browsers](#supported-browsers)
  + [Deployment and Local Deployment](#deployment-and-local-deployment)
  + [Deployment](#deployment)
  + [Local Deployment](#local-deployment)
  + [How to Clone](#how-to-clone)
+ [Credits](#credits)
+ [Acknowledgement](#acknowledgements)

***
***

# User Experience

### Key Project Goals

* To write and develop an informative, interactive, enjoyable website that users will want to return to.
* The user should be able to navigate around the website with ease, whether on a mobile or desktop device. 
* The main homepage will explain to the user what the website is about and detail what they can expect to find. 
* Users will be able to find out about the team who are behind the blog.
* Users will be able to find the numerous benefits to switching to a plant based diet. 
* Users will be able to see recipes, and be able to filter them to their desired category (e.g. Breakfast Recipes) to enhance the user experience, especially if they dont have the time to go through all the recipes. 
* Users will be able to register for an account. Once this is complete, users can be interactive and comment on the recipe blog and edit or delete their comments. 
* Users will be able to get in touch by sending a collaboration request, users do not need to have a register account to do this. 

### Target Audience

* Users of any age that would like to find out more about switching to a plant based diet 
* Users who like to browse different recipes and interact by giving feedback
* Users who enjoy researching before diving into something

### User Requirements and Expectations 

* An accessable website, that is clear and easy to navigate and understand.
* The ability to see who is behind the blog
* The ability to find numerous health benfits to the plant based diet.
* The ability to register for an account.
* The ability to get in touch, if they wish
* Users are able to filter recipes to a particular category
* Users are able to add a comment on the recipe blog, edit or remove thier comments. 

### User Stories

As a site visitor, 

* Navigate around the site with ease. When clicking a page option the relevant page should load. 
* When the homepage is loaded I should see sliding images
* I can locate the social media icons on the footer. When clicking on the icon the relevan page should load.
* I can see a paginated list of recipes. If there is 1 or more post the recipes are listed (vetically on a mobile device, or in groups of 6 on a larger device) The is a link on the homepage to the recipe section. I am then able to filter the recipes into different categories, to make it simple to see the category I want. 
* I am able to click on a recipe and a detailed description loads on another page. 
* I am able to view comments, I or other users have added to the blog post.
* I am able to register for a plant life account. Once I have registered and logged in, I am able to add numerous comments, reply, edit or delete my comments.
* I am able to access a collaboration form, enter my details and submit the form. 

As a site Admin,

* On the homepage, I am able to add/change/delete images within the sliding carousel of images.
* I am able to view comments users have made and authorise them if appropriate or disapprove if not. 
* I am able to able to manange the content of the recipe blogs.
* I am able to create a draft recipe that can be updated at a later date. 
* Via the admin section, I am able to edit any content on the website.
* I am able to store collaboration requests and access them when I want to review them. I can mark them once they have been read. 

### WireFrames

These are images of my wireframe designs. 

* Homepage Mobile and Desktop

<p align="center">
<img src="./static/images/readme/homepage_mobile.jpg">
</p>

<p align="center">
<img src="./static/images/readme/homepage_desktop.jpg">
</p>

* About Me page Mobile and Desktop

<p align="center">
<img src="./static/images/readme/aboutme_mobile.jpg">
</p>

<p align="center">
<img src="./static/images/readme/aboutme_desktop.jpg">
</p>

* Benefits page Mobile and Desktop

<p align="center">
<img src="./static/images/readme/benefits_mobile.jpg">
</p>

<p align="center">
<img src="./static/images/readme/benefits_desktop.jpg">
</p>

* Recipe page Mobile and Desktop

<p align="center">
<img src="./static/images/readme/recipes_mobile.jpg">
</p>

<p align="center">
<img src="./static/images/readme/recipes_desktop.jpg">
</p>

### Entity Relationship Diagram

I created the following graphical representation used to model the data for each individual application. 

* Mainhp ERD
<p align="center">
<img src="./static/images/readme/mainhp_erd.png">
</p>

* About Me ERD
<p align="center">
<img src="./static/images/readme/aboutme_erd.png">
</p>

* Collaborate ERD
<p align="center">
<img src="./static/images/readme/collaborate_erd.png">
</p>

* Benefits ERD
<p align="center">
<img src="./static/images/readme/benefits_erd.png">
</p>

* Recipe ERD
<p align="center">
<img src="./static/images/readme/recipe_erd.png">
</p>

* Comment ERD
<p align="center">
<img src="./static/images/readme/comment_erd.png">
</p>

## Design 

### Typography 

For my main titles on the pages I used a font called Dancing Script, I particulary like this font and think it looks professional. 

<p align="center">
<img src="./static/images/readme/dancing_script.png">
</p>

For the remaining text i used a font called Lato, I used he thin italic version which i felt goes really well with the main title font. 

<p align="center">
<img src="./static/images/readme/lato.png">
</p>


## Features

### Main Start Page (Plant Life)

This is an image of the main homepage. The page constists of a navigation bar, a login status, main title, sliding carousel images, content on the website, category images which are links to other pages in the website and a footer. 

<p align="center">
<img src="./static/images/readme/mainpage.png">
</p>

Dependent on the device you are using depends on how they appear on the screen. 

* Navigation Bar - On a mobile device you will see a 'burger' menu on the right hand side, and when clicked a drop down list will appear of the pages within the website. 

<p align="center">
<img src="./static/images/readme/nav_mobile.png">
</p>

On a larger device you will see that the list appears at the top of the screen and the burger icon disappers. 

<p align="center">
<img src="./static/images/readme/nav_desktop.png">
</p>

* Category Images - On a mobile device the images are listed in a vertical line, and on larger images they will appear horizontal in a row of 4.

<p align="center">
<img src="./static/images/readme/category_mobile.png">
</p>


<p align="center">
<img src="./static/images/readme/category_desktop.png">
</p>


### About Me Page

This is an image of the about me page. The page gives the user information about the team behind the scene. The page is seperated in 3 parts. Firstly the about me section which details about the creator of the business, a behind the scenes section which details other members of the team, and finally a collaboration form were users can send their details to get in touch. The page is responsive and will alter the size of the text and images depending on the device being used to view the site.  

<p align="center">
<img src="./static/images/readme/aboutme_page.png"> 
</p>

### Benefits Page

This is an image of the benefits page. The page gives infomation about some of the health benefits of a plant based diet. The page is seperated into 2 parts. Firstly a title section and secondly an image and text section. Each of the images have been placed at opposite ends of the screen to seperate them and make it more appealing to look at. The page is fully responsive and will alter the size of the text and images depending on what device is being used to view the site. 
If a mobile device is being used the images will display vertically with the relevent text being show underneath the image. 

<p align="center">
<img src="./static/images/readme/benefits_page.png"> 
</p>


### Recipe Page

This is an image of the recipe page. The page is serperated in 3 parts, firstly a title section, secondly a filter section where the user can select a category of the types of recipes they wish to view eg. 'breakfast' once clicked the screen will load with the relevant recipes. Finally the recipe section, which displays a paginated list of 6. On a mobile device the recipes are displayed vertically and on a larger device there will be 2 rows of 3 recipes. In each recipe section, there is an image, the title of the recipe, how long it takes to make, how many it serves, if it has any source of protien, etc and if anyone has commented on the recipe. These go into more detail when you click on the image. There is also a next and prev button so the user can move through the recipes easily. The page is fully responsive and will alter the size of the text and images depending on what device is being used to view the site.

<p align="center">
<img src="./static/images/readme/recipe_page.png"> 
</p>

### Method Page

This is an image of the method page. When the user selects a recipe, this page will load with all the information they need to make the recipe. The page is seperated into 3 parts. The first section displays the name of the recipe, and image and details of how long it will take to make, how many the recipe will serve, if there are sources of protien, antioxidants etc and if anyone has commented on the recipe blog.
The second section shows the ingredients need to make the recipe and a numbered list of the steps in order to make it. 
The final section is where users can leave comments on the recipes, users are able to edit or delete their own comments, and there is no limit as to how many comments they leave. User do however have to be registed with the website in order to have this interaction. 

<p align="center">
<img src="./static/images/readme/method_page.png"> 
</p>

### Category Page

This is an image of the category page. When a user selects one of the category images from the homepage or selects one of the filters on the recipe page, the category which they have chosen will appear and the relevent recipes listed. The screen is displayed in the same way as the recipes section, however only recipes relating to that cateogry will appear. 
If there are more than 6 recipes, a next and prev button will appear at the bottom allowing the user to move through the recipes easily. 

<p align="center">
<img src="./static/images/readme/category_page.png"> 
</p>

### SignUp Page

This is an image of the sign up page. User are required to register an account if they wish to comment on the recipes. To do this, they are required to provide a Username, email is optional, and a password.  

<p align="center">
<img src="./static/images/readme/signup_page.png"> 
</p>

Once the manditory fields and steps have been completed their registration is complete and there will be a message confirming this. There is also text on the right hand side to inform the user that they are logged in. 

<p align="center">
<img src="./static/images/readme/registration_successful.png"> 
</p>

### Log Out Page

This is an image of the log out page. When a user requests to log out, a defensive screen will appear making sure the user definately wants to log out. 

<p align="center">
<img src="./static/images/readme/logout_page.png"> 
</p>

If the user selects No, they return to the site, however if they select yes, the user is returned to the homepage and the following message will appear.

<p align="center">
<img src="./static/images/readme/logout_message.png"> 
</p>

### Login Page

This is an image of the login page. If a user has registered and account, they can click on the login section where they will be asked to confirm their username and password. Once this has been authorised the user will see the following message and can go ahead and make comments of any of the recipes.  

<p align="center">
<img src="./static/images/readme/login_page.png"> 
</p>

If the user selects No, they return to the site, however if they select yes, the user is returned to the homepage and the following message will appear.

<p align="center">
<img src="./static/images/readme/login_message.png"> 
</p>

### Comments Section

This is an image of the comments section which appears in each of the recipes. If a user is logged in they are able to comment on the post. They enter this in the white box on the right and once completed they click submit. 
The comments will not go live on the site until the admin has approved them, however while they are waiting to be approved the user is able to edit or delete their comment.

<p align="center">
<img src="./static/images/readme/comments_section.png"> 
</p>

### Future Features

In the future I would like to add the following features:

* I would like the user to be able to 'like' the recipe, this will then add the recipe into a favourite account which can be access via the navigation page. 
* I would like to add other apps, that include exercise, wellbeing and relaxation pages.
* I would also like to add a shopping list section where users can click on the recipe item and they will collect in a shopping list, once at the shop the user would be able to 'tick' off the item so it disappears from the list.

### Technologies Used

* HTML
* CSS
* JavaScript
* Python
* Django

### Frameworks and Tools Used

* [Balsamiq](https://balsamiq.com/)
* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Django Project](https://www.djangoproject.com/)
* Microsoft Word - To make my ERD designs
* [W3C Validator](https://validator.w3.org/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* [CI Linter Code Checker](https://pep8ci.herokuapp.com/)



## Deployment and Local Deployment

### Deployment 

All code was written within GitPod development environment. I used GitHub for version control and was finally deployed to Heroku from GitHub.

To deploy this site on Heroku the following steps were performed:

After the initial account setup
* Click the "create new app" button on heroku
* Create a unique name for the app
* Select region (Europe was selected for this project)
* Click "create app"
* Go to settings tab
* Set config vars using the creds1.json file. In the field for key, "CREDS1" should be entered and in the field for value, the entire creds1.json file content is entered
* Then click "add buildpack"
* Use python and nodejs buildpacks
* The buildpack order should be python on top and nodejs underneath
* Go to the deploy tab
* Select the deployment method (github was used for this project)
* Search for the github repository name ( In this instance I selected Hangman)
* Then click on Connect
* There is an option to use manual deployment or automatic deployment. Make sure main branch is selected
* After the first deployment you will see a message saying "your app was successfully deployed" and there will be a "view" button to take you to your deployed application

### Local Deployment
  How to Fork 
  * Login to Github
  * Open repository
  * Click fork button in the top right corner.

### How to clone 
  * Login to Github
  * Open repository 
  * Click on the 'code' button, select which you would like with HTTPS, SSH or GitHib CLI and copy
  * Open terminal in code editor and change the current directory to the location you want to use is
  * Type 'git clone' and paste link that you copied in step 3, press enter

## Credits

* [Django Blog CI Walk through Project]() - Code was adatpted from the CI love sandwiches project. 
* [W3Schools](https://www.w3schools.com/) - was used as a refresher to explain loops/while loops when I was unsure why my code wasnt working.
* [Deliciously Ella](www.figlet.org/examples) - was used to source some of the recipes.
* [Eating Well ](https://www.eatingwell.com/article/291622/the-health-benefits-of-eating-a-plant-based-diet-and-how-to-get-started/) was used to source the health benefits of a plant based diet.
* [Python](#https://www.python.org/about/help/) was used as a general source of knowledge
Slack - Was use to troubleshoot ideas with my CI colleagues

## Acknowledgements
 * I would like to thank my colleagues on Slack who provided help, support and essential feedback.
 * Finally I would like to thank my husband and daughter for always pushing me, supporting me and allowing me the time to code.
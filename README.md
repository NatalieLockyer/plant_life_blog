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
    + [Entity Relationship Diagram (ERD)](#entity-relationship-diagram)
+ [Design](#design)
    + [Typography ](#typography)





+ [Features](#features)
    + [Main Start Page](#main-start-page)



+ [Future Features](#future-features)
+ [Wireframes]
+ [ERD]
+ [Technologies Used](#technologies-used)
    + [Languages Used](#language)
    + [Frameworks Used](#frameworks-and-tools)
    + [Python Libraries](#python-libraries)
    + [My Python Files ](#my-python-files)

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
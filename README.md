
# [![List of Links](docs/screenshots/logo.jpg)](https://list-of-links-sdj-aa4cc1def405.herokuapp.com/)

[![List of Links shown on a iPhone, MacBook and iPad](docs\screenshots\responsive_L_of_L.jpg)](https://list-of-links-sdj-aa4cc1def405.herokuapp.com/)


## Introduction
List of Links is a curated collection of useful resources for web developers. The site contains links, screenshots and descriptions of websites, tools, tutorials, and more. Whether you're looking for inspiration, learning a new skill, or searching for a solution to a coding problem, List of Links has you covered. 
 
Users can browse the collection of resources by category or search for specific topics. The site aims to provide value to web developers of all skill levels. Each resource has been hand-picked and organized to save developers time searching the web. List of Links makes discovering high-quality web development resources simple and efficient.   
 
 Users can view resources, like posts and comment on resources. List of Links is a community platform where web developers can share knowledge and help each other improve their skills.

 The project was built keeping the Agile management principles in mind, and I utilised many of GitHub's features such as Issue and Projects to implement Scrum methodology.

[Kanban Board for project](https://github.com/users/satogako/projects/5)

[Closed Issues on GitHub for the project](https://github.com/satogako/list-of-links/issues?q=is%3Aissue+is%3Aclosed)

I used [GitHub issues](https://github.com/satogako/list-of-links/issues) for the product backlog containing the user stories.

CRUD functionality:
- All Categories - displays a list of resources and their approved comments
- Categories - shows resource details and its verified comments
- Approve comments - displays comments that need approval and allows the administrator to approve or delete them.
- resource_details.htm - shows details of the resource and its confirmed comments and also allows the registered user to send comments.
- class ResourseAdmirers - handles liking and disliking resources.
- class ApprovalCommentsView - displays comments that need approval and allows the administrator to approve or delete them.

<details>
<summary>Screenshot of the product backlog</summary>

![](docs\screenshots\user_story.jpg)

</details>


I used the tags feature in GitHub Issues for assigning story points, prioritising features based on [the MoSCoW method](https://en.wikipedia.org/wiki/MoSCoW_method), and categorising the user stories.

I used the [Milestones feature](https://github.com/satogako/list-of-links/milestones) to plan sprints and set deadlines.


## User Stories
User Stories can been seen below under [User Story Testing](#user-story-testing), and in the [GitHub Issues](https://github.com/satogako/list-of-links/issues?q=is%3Aissue+is%3Aclosed) for full details including screenshots, story points and associated sprints.


# UX Design 
The UX design for this project aims to provide an intuitive and engaging experience for users. The layout and flow of the site focuses on simplicity while still maintaining an aesthetic appeal.

### Layout 
The layout utilizes a standard three-column design with a fixed navigation bar at the top. This ensures that all content is easily accessible while keeping the interface clean and minimal. The navigation links in the bar correspond to the main sections of the site. 
 
The content on each page is centered for easy reading and divided into cards for visual appeal. Important information like titles and authors are clearly displayed at the top of each card. A screenshot and brief description are also included to give users a quick overview and help them determine what resources are most relevant or interesting.

### Wireframes

![](docs\screenshots\layot.jpg)


### Colors
<div style="width: 30px; height: 30px; background-color: #2196F3;"></div>
The color palette utilizes shades of blue, teal and grey to give the site a clean and minimal feel. The primary color used is a medium blue which is applied to interactive elements such as links and buttons. 

<div style="width: 30px; height: 30px; background-color: #26a69a;"></div>
Teal shades are incorporated as accent colors to highlight important elements or convey meaning. For example, a teal sticker is used to prominently display the author of each resource on the main page. Teal is also used for the “sent for approval” chips on the comments page. 
 
Various shades of grey are used throughout the site for text, dividers and backgrounds.

<div style="width: 30px; height: 30px; background-color: #616161;"></div>
<div style="width: 30px; height: 30px; background-color: #424242;"></div> 
Darker greys are applied to text.

<div style="width: 30px; height: 30px; background-color: #f5f5f5;"></div>
<div style="width: 30px; height: 30px; background-color: #eeeeee;"></div> 
While lighter greys are used for backgrounds and dividers. The specific shades of grey were chosen to provide sufficient contrast between elements while maintaining an understated and minimal style.

<div style="width: 30px; height: 30px; background-color: #e53935;"></div>
The vibrant shade of red color, is used sparingly to draw attention. This includes comments, delete button and logout. Its striking contrast against the primarily cool color palette ensures users notice and respond to these important elements.

<div style="width: 30px; height: 30px; background-color: #2c3e50;"></div>
<div style="width: 30px; height: 30px; background-color: #26a69a;"></div>
The navigation bar utilizes shades of blue and teal to visually separate it from the rest of the page. The teal shade is used for the active link to clearly show the user their current location.  
The footer uses the same blue shade as the navigation bar for the background. The GitHub icon in the footer use teal on hover to match the accent color used throughout the site. This helps create a cohesive style across sections.
 
The selected color scheme aims to give the site a simple yet polished feel that focuses users’ attention on content over visual flair. The primarily neutral palette is accentuated with vibrant shades of blue and teal to highlight interactive elements and convey meaning in an intuitive fashion. Overall, the color choices reflect the clean and minimal aesthetic maintained throughout the design and layout of the site.
Requirements:
1. Everyone in the group must check something in to the git repo
2. You must have a Flask back end and a HTML/JS/JQuery/Bootstrap front end.
3. You must have a home screen with some kind of “start” button so you know when a
new user has started the learning process.
4. On the back end, you must store important information about users’ choices on every
page. For the quiz, you should store their quiz answers. For the learning activity, you
should store important selections they make (or at least what time they enter the page). 5. We highly recommend that you don’t hard-code the data or media of the pages into the
HTML. Rather, it’s much more modular to represent the data in a JSON object, then
render each page with the correct data (As shown in class Monday 4/8).
6. Although your implementation may vary, you will probably need ~4 routes.
a. A home page (with a start button)
b. A learning route that takes a variable for what number lesson the user is on.
i. E.g. /learn/1
c. A quiz route that takes a variable for what number quiz question the user is on.
i. E.g. /quiz/1 d. A quiz result page.
7. Each page should show some data, have a few instructions, record some user data, and at least be able to go to advance to the next page.
a. You should be able to enter your quiz information and receive a score at the end that reflects your correct/incorrect answers.
8. Your app does not need to work for more than one person at a time. You can assume you only have one user at a time who ever uses the app. In real life, you wouldn’t do this – you’d use a package that implements user accounts and then store all the user data on the user object.
9. During your TA feedback session, every team member needs to have the app running on their laptop.
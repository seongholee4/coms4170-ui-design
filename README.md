# coms4170-ui-design
The [`COMS 4170 UI Design`](http://coms4170.cs.columbia.edu/2024-spring/) course is designed to teach students how to design and implement user-centric interfaces for web applications.


## Overview
Our project focuses on creating a learning platform that includes both a `learning activity` and a `quiz`.
Throughout the project development, we engaged in iterative prototyping, conducted user interviews, and received feedback from our TA and classmates to enhance our design.


## Team Members
| Name                 | GitHub Profile                           |
|----------------------|------------------------------------------|
| Lee, Seongho     | [@seongholee4](https://github.com/seongholee4) |
| RajGirish, Ananya| [@ananya41309](https://github.com/ananya41309) |
| Zhang, Shiyu     | [@Shiyuuu530](https://github.com/Shiyuuu530)   |


## Key Project Features:

- **Frontend Development**: HTML, CSS, and JavaScript
- **Backend Development**: Python Flask
- **Iterative Prototyping**: Low-fidelity and high-fidelity prototypes
- **User Feedback**: Continuous improvements based on feedback sessions

## Project Structure

- **static/**: Contains static files such as CSS, and images.
- **templates/**: Contains HTML templates.
- **data.py**: Contains data dictionaries.
- **image_url.py**: Contains image URLs.
- **server.py**: server script built with python flask.

## Branches
This repository contains the source codes for the `COMS 4170 UI Design` course.
Each assignment is stored in its respective branch.

- **main**: Contains the latest source code updated since the final project.
- **hw10**: Contains the source code for `hw10`.
- **hw11**: Contains the source code for `hw11`.
- **hw12**: Contains the source code for `hw12`.
- **coms4170-final-project**: Contains the source code for the `final project`.


## How to Use

### Clone the Repository
```bash
git clone https://github.com/seongholee4/coms4170-ui-design.git
cd coms4170-ui-design
```
* After cloning the repository, change the directory to `coms4170-ui-design`.

### Clone a Specific Branch
```bash
git branch -a # View all branches

git checkout -b <branch-name> origin/<branch-name>
# Replace `<branch-name>` with `hw10`, `hw11`, `hw12`, etc.
# For example:
git checkout -b hw10 origin/hw10
git checkout -b hw11 origin/hw11
git checkout -b hw12 origin/hw12
git checkout -b coms4170-final-project origin/coms4170-final-project

git branch # View current branch

# To run the server.py in a branch
python server.py

git checkout main # Switch to main branch

```

### Open the Browser
Open the browser and navigate to `http://localhost:5000/` or `http://0.0.0.0:5000/`.

**Pull and Push Changes**:
```bash
git pull origin main # Pull Latest Changes from Main
git push origin main # Push Changes to Main
```

## Acknowledgements
We would like to thank our instructor, `Prof. Lydia Chilton`, our classmates, and our TA, `Asia B. Gray`, for their guidance and support throughout the course and project development.

* The project structure was inspired by the [COMS 4170 UI Design](http://coms4170.cs.columbia.edu/2024-spring/) course.

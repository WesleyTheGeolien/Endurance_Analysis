[![Build Status](https://travis-ci.org/WesleyTheGeolien/Endurance_Analysis.svg?branch=master)](https://travis-ci.org/WesleyTheGeolien/Endurance_Analysis) [![Join the chat at https://gitter.im/Endurance_Analysis/community](https://badges.gitter.im/Endurance_Analysis/community.svg)](https://gitter.im/Endurance_Analysis/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# Endurance_Analysis
Tools like Strava Summit and Training Peaks are great but can be inflexible when analysing data. Other tools like elevate exist but are part extension of strava summit part application. The goal of this project is to propose different tools for analysing endurance sports and create a standalone containerized tool.

# Getting Started
## Prerequisites
### Docker
Whether this be in prototyping phase or the final application this project relies on [Docker](https://www.docker.com/). For installation instructions see [Docker install documentation](https://docs.docker.com/install/), in particular:
* [Windows](https://docs.docker.com/docker-for-windows/install/)
* [MacOS](https://docs.docker.com/docker-for-mac/install/)
* [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

### Git (Optional)
This project is hosted on Github you can download a static version as a Zip but the preferred method is to use [Git](https://git-scm.com/) to keep a source controlled version. For installation instructions see the [official documentation](https://git-scm.com/book/en/v2/etting-Started-Installing-Git).
## Installation
### Clone this directory
```
git clone https://github.com/WesleyTheGeolien/Endurance_Analysis.git
```
### .env
Create a `.env` file in the route directory and enter the following parameters:
* _fit_files_src_

(The format should be one variable/value per line with the format _parameter=value_)

### Launch Containers
Before launching the containers for the first time they need to be built by adding the --build flag we ensure that the containers are always up to date. If the source code has not changed then building should be quick.
```
docker-compose -f "Docker\docker-compose.yml" up  --build
``` 

### Interacting with containers
If there are any problems check the ports in "Docker\docker-compose.yml".
Open a browser and navigate to:
* Prototyping: `localhost:8081`

# Help
## Gitter
Feel free to reach out for help on [Gitter](https://gitter.im/Endurance_Analysis/community)
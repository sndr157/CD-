# Contineous Deployment with GitHub Actions to a Flask Application on a Droplet
---

This project chronicles an endeavor to implement a robust Continuous Integration/Continuous Deployment (CI/CD) pipeline by leveraging the efficient capabilities provided by GitHub Actions and a Virtual Private Server (VPS) on DigitalOcean. The complexities of the project included mastering the orchestration and interconnected processes of multiple technological systems.

The initial phase involved the establishment of the foundational elements: deploying a Droplet on DigitalOcean, understanding the rudiments of GitHub Actions, and successfully running a Flask application on the said Droplet.

Subsequently, the .yaml file was systematically extended from a plain run-test section to incorporate a 'deploy' module. This strategic augmentation was designed to trigger the deployment process only upon successful completion of predefined tests, thereby safeguarding system integrity and reliability.

A noteworthy challenge faced during the project was the configuration of an SSH login to the Droplet, bypassing the traditional necessity for a password. This issue was resolved by utilizing GitHub's secrets capability, in conjunction with an online tutorial on [medium](https://medium.com/swlh/how-to-deploy-your-application-to-digital-ocean-using-github-actions-and-save-up-on-ci-cd-costs-74b7315facc2), that provided step-by-step guidance for optimal registration of keys with the Droplet.

In essence, this project served not only as an exploration of how to fuse diverse technological components into a functional CI/CD pipeline but also offered invaluable insights into the complexities of managing a VPS-based project environment with tools such as DigitalOcean and GitHub Actions.

# 🎯 Issues & Solutions: Implementing a CI/CD Pipeline with GitHub Actions on DigitalOcean

## 1️⃣ Issue: SSH Login to DigitalOcean Droplet 

### 🔐 Solution: 

Implementing the SSH login to our DigitalOcean droplet without the need for a password posed a significant challenge. We leveraged GitHub Secrets to securely store our SSH private key, eliminating the need for password-based authentication. A Medium tutorial was utilized to guide us through the process of registering the SSH keys with the Droplet.

### 🔧 Components: 

   - 🔑 GitHub Secrets : Provided a secure storage for our SSH private key.
   - 📒 Medium Tutorial: Offered comprehensive step-by-step instructions for configuring the SSH login.
   - 🌊 DigitalOcean Droplet: Served as our VPS where we configured the SSH login.

## 2️⃣ Issue: Configuration and Extension of .yaml File 

### 🔐 Solution: 

Our second challenge was to extend our .yaml file. Initially, its sole function was running tests, so we extended it to include a 'deploy' module. This change ensured deployments were triggered only after successful test runs, thereby maintaining the system's stability.

### 🔧 Components:

   - 📑 .yaml File: The document used by GitHub Actions to determine our workflow.
   - ⚡ GitHub Actions: The CI/CD tool we leveraged to automate our deployment pipeline.
   - 🔍 Testing Suite: Executed before the deploy module to ensure the code works as intended before deployment.

## 3️⃣ Issue: Automatic Code Pull from GitHub

### 🔐 Solution: 

The third issue, revolved around keeping our Droplet updated with the latest code changes from our GitHub repo. To ensure automatic code pulls, we added the droplet's public key to the GitHub's SSH keys. This allowed for automatic code pulls each time a new commit was pushed to our repo.

### 🔧 Components: 

   - 📚 GitHub Repo: The repository that houses our Flask app's codebase.
   - 🖥️ Bash Script: Run on our Droplet, this script pulls the latest GitHub code updates and restarts the Flask service.
   - 🔐 Server's Public Key: Authenticated our Droplet with GitHub, allowing for automatic code pulls.

I registered the following 3 secrets:
![](/Images/secrets.png?raw=true)

Then I added the following code to my .yml file:
![](/Images/yml.png?raw=true)

I struggled a bit here. Even though I followed the tutorial closely, I made some small copy paste or typos that prevented this from working correctly. After carefully backchecking I finally got it working. 


# The Script on Droplet Ubuntu Server
---
I wrote the bash script which goes into my flask app directory and pulls the code from github. To pull code from GitHub automatically I added the server public key on my GitHub SSH keys. Next, the script restarts the Flask app service so the app loads the latest code
To create public and private key I used the code below
ssh-keygen 

![](/Images/script.png?raw=true)

# Flask Service File
---

![](/Images/service.png?raw=true)



# Deployment (cicd)
---
![](/Images/cicd.png?raw=true)

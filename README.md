# Contineous Deployment with GitHub Actions to a Flask Application on a Droplet
---

This project recapitulates the intricate journey of implementing a robust Continuous Integration/Continuous Deployment (CI/CD) pipeline, utilizing GitHub Actions' power and a DigitalOcean hosted Virtual Private Server (VPS). The challenge lay not just in mastering multiple technological systems but also in architecting their interconnected processes to function seamlessly.

The adventure started with three crucial steps 🚶:

1. Deploying a DigitalOcean Droplet ☁️. 
2. Understanding the essentials of GitHub Actions 💡.
3. Successfully deploying a Flask application 🚀 on the VPS.

As much as it was an exciting expedition, it was equally not short of complexities. To put a finger on one, configuring an SSH login to the VPS without relying on a password login was a steep hill to climb🧗‍. However, thanks to GitHub's secrets feature and a detailed [Medium article](https://medium.com/@avilash/google-cloud-run-deploy-application-via-ci-cd-pipeline-with-github-actions-6a96795563d), configuring an SSH key-login became approachable.

Another primary task was refining the .yaml file, extending it from running simple tests to efficiently incorporating a 'deploy' module. This augmentation was not just a strategic move but a necessity, ensuring that only after successful test completion, the deployment process is triggered. The transition added a strong veil of reliability, preventing any system instability.

Notwithstanding the challenges, we leveraged a [YouTube tutorial video](https://www.youtube.com/watch?v=YFBRVJPhDGY&t=421s) on deploying Flask apps that proved to be a helpful guide to lighting our path. Hours of extensive online research, brainstorming, and testing went into crafting this fusion of technology 📚🔍.

In the grand scheme of things, the project served as a great exploration venture into fusing diverse technological entities into a functional CI/CD pipeline while providing an in-depth understanding of managing a VPS-based project environment using tools like DigitalOcean and GitHub Actions.

A wrap-up would be incomplete without acknowledging that such projects, far from being a walk in the park, fire up the neurons and leave one with a rich wealth of knowledge and experience 🧠💡. Thus ensuring that each stumbling block only opens up doors to further exploration.

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

My second challenge was to extend our .yaml file. Initially, its sole function was running tests, so we extended it to include a 'deploy' module. This change ensured deployments were triggered only after successful test runs, thereby maintaining the system's stability.

### 🔧 Components:

   - 📑 .yaml File: The document used by GitHub Actions to determine our workflow.
   - ⚡ GitHub Actions: The CI/CD tool we leveraged to automate our deployment pipeline.
   - 🔍 Testing Suite: Executed before the deploy module to ensure the code works as intended before deployment.

## 3️⃣ Issue: Automatic Code Pull from GitHub

### 🔐 Solution: 

The third issue revolved around keeping our Droplet updated with the latest code changes from our GitHub repo. To ensure automatic code pulls, we added the droplet's public key to the GitHub's SSH keys. This allowed for automatic code pulls each time a new commit was pushed to our repo.

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

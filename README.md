# Contineous Deployment with Github Actions to a Flask Application on a Droplet
---
I ran into quite some problems while doing this assignment. Most of them really had to do with how a lot of the systems run and communicate with each other. I learned a lot from this.

Before starting this assignment I had already succesfully walked through the previous theory and exercises. So I had my Droplet running, understood the basics of GitHub Actions and had managed to succesfully run a flask application on my Droplet. However combining all of these in a smooth CICD pipeline was quite the challenge. I tried to tackle this step by step, while contineously checking my results.  
 
First I extended my previous .yaml file (that consisted of a run-tests section) with a 'deploy' section that would only deploy if the app passed the tests. I had to figure out how to log in to my Droplet over ssh without a password. For this I used the secrets option in Github while following a small tutorial online about properly registering your keys in the Droplet [medium] (https://medium.com/swlh/how-to-deploy-your-application-to-digital-ocean-using-github-actions-and-save-up-on-ci-cd-costs-74b7315facc2).

I registered the following 3 secrets:
![](/Images/secrets.png?raw=true)

Then I added the following code to my .yml file:
![](/Images/yml.png?raw=true)

I struggled a bit here. Even though following the tutorial closely, I made some small copy paste or typo's that prevented this from working properly. After carefully backchecking I finally got it working. 


# The Script on Droplet Ubuntu Server
---
I wrote the bash script which goes into my flask app directory and pull the code from github. To pull code from github automatically i added the server public key on my github ssh keys. Next the script restarts the flaskapp service so the app loads latest code
To create public and private key i used the code below
ssh-keygen 

This is the script
![](/Images/script.png?raw=true)

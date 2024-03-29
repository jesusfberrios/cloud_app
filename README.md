# cloud_app

## Summary
This repository is intended to deploy a web application hosted in a Cloud VM which connects to a Database and a Storage service. The infrastructure was deployed in Azure; however, it can be replicated in other clouds by changing the connection libraries/parameters. All the dependencies are in the *install_reqs.sh* and *requirements.txt* files. 
![alt text](image.png)


Note that the credentials are stored in the environment variables of the machine, so then they are not shared through this repository. It is important to mention that more security concerns such as secure SSL connections should be covered for a production environment, as in this cas ethe focus is just a quick deployment.


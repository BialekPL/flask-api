# Deploy a Python (Flask) web app to Azure App Service - Sample Application

This is the sample Flask application for the Azure Quickstart [Deploy a Python (Django or Flask) web app to Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python). For instructions on how to create the Azure resources and deploy the application to Azure, refer to the Quickstart article.

Sample applications are available for the other frameworks here:

* Django [https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart)
* FastAPI [https://github.com/Azure-Samples/msdocs-python-fastapi-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-fastapi-webapp-quickstart)

If you need an Azure account, you can [create one for free](https://azure.microsoft.com/en-us/free/).

# Deploy app to Azure Container App

Go to the root folder where the Dockerfile is. 
`az containerapp up -n [your ACA name] -g [resource group name where your ACA is] --source .\`
This will also create Azure Container Registry in your resource group, but in my case it was created in East US region, while all my other resources were in Europe. So alternatively you can create an acr by yourself in desired region and then do
`az containerapp up -n [your ACA name] -g [resource group name where your ACA is] --source .\ --registry-server [URL of your ACR, so xxxx.azurecr.io] --registry-username [acr username from Access Keys blade on ACR page] --registry-password [acr password from Access Keys blade on ACR page - admin user]`


# Deploy new version

`az containerapp update -n [your ACA name] -g [resource group name where your ACA is] --source .`

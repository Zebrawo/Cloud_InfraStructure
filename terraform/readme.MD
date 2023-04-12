# Azure Kubernetes Service (AKS) Terraform Deployment

This repository contains Terraform code to deploy an AKS cluster on Azure with a resource group, random suffix name, default node pool, identity and network profile configurations

## Prerequisite

Before you begin, make sure you have:
- An Azure account with sufficient permissions to create AKS clusters and related resources.
  - Note that you can use a Service Principal. If you want to use a Service Principal you need to create a Service Principal in Azure Active Directory.
  - Also you need to a Block in your Terraform file under provider:
  ```tf
  client_id       = "<your-service-principal-app-id>"
  client_secret   = "<your-service-principal-password>"
  ```
- Terraform install on your machine. [Download](https://developer.hashicorp.com/terraform/downloads)
- An SSH key pair for use with the AKS cluster. You can generate a SSH Key with '**SSH-keygen**' or with [PuTTY RSA & DSA Generator](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

## Deployment

Login in your Azure CLI on your terminal
```bash
az login 
```

Open the directory with the Terraform file.
Run the following command for initializes a working directory containing Terraform configuration files.
```bash
terraform init
```

Apply the Terraform configuration to create your resource
```bash
terraform apply
```

## Cleaning up
To delete your resources, run:
```bash
terraform destroy
```

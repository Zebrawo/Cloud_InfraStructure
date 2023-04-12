provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "CLI-${random_string.random_suffix.result}"
  location = "West Europe"
}

resource "random_string" "random_suffix" {
  length  = 6
  special = false
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "Cloudinfrastructure-${random_string.random_suffix.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = azurerm_resource_group.rg.name
  kubernetes_version  = "1.25.5"
  tags = {
    Environment = "dev/test"
  }

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_B2s"
  }

  identity {
    type = "SystemAssigned"
  }

  linux_profile {
    admin_username = "azureuser"

    ssh_key {
      key_data = "<your public SSH KEY>"
    }
  }

network_profile {
  network_plugin      = "azure"
  network_policy      = "calico" # Update to calico if you want to use custom pod_cidr
  network_plugin_mode = "Overlay" # Add this line
  service_cidr        = "10.0.0.0/16"
  dns_service_ip      = "10.0.0.10"
  pod_cidr            = "10.244.0.0/16"
}

}

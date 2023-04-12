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
      key_data = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCVf0nttI/P2OyNYcAWXDErhSwupd9o2fNin2gOL8R7YBz3se1HCsXMYa7scZyFBzH3XGgaUAXIc0AvHXllUaws2aLZLycB50+7W0yii6P0bUTMZmCNeFx2h6qIkmDc09NMlNdHwtD9rSMElV8gdU/66Um83okJKqu5XQZufxrZ0vw2ea98XUxURojkivWetYoEBPaYHjHlZjxyEFcRk4x8E0esDmhwO4S37cHlv7fGq9y5e3fsWytbQMEiNNx5/hKbYqJxmWXrGMGBUuNshOuyalGrJ04T3ePGhzX+eYoPIue17IQScSPiV35gsdZP1fJvhedpIR41PMY8DB5SNXnN rsa-key-20230411"
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

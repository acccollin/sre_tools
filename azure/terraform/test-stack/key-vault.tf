
locals {
    azure_tenant_id = var.azure_tenant_id
    azure_object_id = var.azure_object_id

}


resource "azurerm_key_vault" "kv" {
  name                        = "golden-kv"
  location                    = azurerm_resource_group.rg.location
  resource_group_name         = azurerm_resource_group.rg.name
  enabled_for_disk_encryption = true
  tenant_id                   = local.azure_tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false

  sku_name = "standard"

  access_policy {
    tenant_id = local.azure_tenant_id
    object_id = local.azure_object_id

    key_permissions = [
      "Get",
    ]

    secret_permissions = [
      "Get",
    ]

    storage_permissions = [
      "Get",
    ]
  }
}
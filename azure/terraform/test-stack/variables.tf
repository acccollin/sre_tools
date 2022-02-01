variable "azure_subscription_id" {
  type        = string
  description = ""
}

variable "azure_client_id" {
  type        = string
  description = "SPN Client ID"
}

variable "azure_client_secret" {
  type        = string
  description = "SPN Client Secret"
}

variable "azure_tenant_id" {
  type        = string
  description = "SPN Tenant ID"
}

variable "address_space" {
    type        = list(string)
    description = "VNET address space"
}

variable "web_subnet_prefix" {
    type        = list(string)
}

variable "admin_username" {
  type = string

}

variable "admin_password" {
  type = string
}

variable "vm_size" {
  type = string
  
}
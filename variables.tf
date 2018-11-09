variable "ssh_key_name" {
  default = "dk_rescale_key"
}

variable "public_key_content" {
  default = "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEA473TyvkZaz3c24txEszcXOf5HdtjcYVT7RMVxti95AGxvMxrc8Bs6plaXmIS9pvuXitTqQvYxiK9LaBz8i9odKp7ccyV1Nxdxu5tbfZC22xubxxfkN1uzyzqlKSozWaVynGdcofOO5r1aVnHS4svY31WSVn6raM06teId2XRepOk6hppx+xxf8mcsJPB3j/NV3nGePY+eeCdQwLLQp8cIED4LlWkr0LV+kYigC1W3WK4T7n2VsWs3uqwMDU1C91CpcoLkjkhuFF85qzQ6Aq6TUzFwceVgXxYWzxshHkY6nc4UHlttDMjl0wyeesqOzagMITcKUfFgHJRawMqZbAvgQ=="
}

variable "profile" {
  default = "default"
}

variable "myip" {
  default = "68.58.229.60"    #"192.168.0.7"
}

variable "rescale_account_for_public_ami" {
  default = "604329154527"    #default = "604329154527" rescale account
}

variable "region" {
  default = "us-west-2"
}

variable "az1" {
  default = "us-west-2a"
}

variable "az2" {
  default = "us-west-2b"
}

# ci_cd/Terraform/variables.tf
variable "folder_id" {}
variable "cloud_id" {}
variable "token" {}
variable "ram" {
  default = 4
}
variable "cpu" {
  default = 4
}
variable "count_master" {
  default = 1
}
variable "count_worker" {
  default = 1
}
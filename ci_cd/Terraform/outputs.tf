# ci_cd/Terraform/outputs.tf
output "ip" {
  value = [for vm in yandex_compute_instance.vm-1 : vm.network_interface.0.nat_ip_address]
}
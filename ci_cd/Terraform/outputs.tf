# ci_cd/Terraform/outputs.tf
output "master_ip" {
  value = yandex_compute_instance.master.*.network_interface.0.nat_ip_address
}

output "worker_ip" {
  value = yandex_compute_instance.worker.*.network_interface.0.nat_ip_address
}

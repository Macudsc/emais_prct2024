terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token     = var.token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = "ru-central1-a"
}

# Сеть
resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

# Подсеть
resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["10.10.10.0/24"]
}

# мастер
resource "yandex_compute_instance" "master" {
  count       = var.count_master
  name        = "k8s-master-${count.index}"
  platform_id = "standard-v1"

  resources {
    cores  = var.cpu
    memory = var.ram
  }

  boot_disk {
    initialize_params {
      image_id = "fd80d7fnvf399b1c207j" # Ubuntu 22.04
      size     = var.disk_size_master # Размер диска
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = file("${path.module}/cloud-config")
  }
}

# воркер
resource "yandex_compute_instance" "worker" {
  count       = var.count_worker
  name        = "k8s-worker-${count.index}"
  platform_id = "standard-v1"

  resources {
    cores  = var.cpu
    memory = var.ram
  }

  boot_disk {
    initialize_params {
      image_id = "fd80d7fnvf399b1c207j" # Ubuntu 22.04
      size     = var.disk_size_worker # Размер диска
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = file("${path.module}/cloud-config")
  }
}
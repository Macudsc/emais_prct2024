# Определение кнфигурации самого терраформа. Указываются провайдеры, путь до бекенда (до хранения файла состояния). При локальном хранении tfstate не конфигурируем здесь.
terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

# Описание провайдера.
provider "yandex" {
  token     = var.token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = "ru-central1-a"
}

resource "yandex_compute_instance" "vm-1" {
  count       = var.count_vm
  name        = "linux-vm-${count.index}"
  platform_id = "standard-v1"

  resources {
    cores  = var.cpu
    memory = var.ram
  }

  boot_disk {
    initialize_params {
      image_id = "fd80d7fnvf399b1c207j" # ubuntu 20.04
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    #ssh-keys = "${var.name_user}:${var.ssh_key}"
    # берем файл
    user-data = file("${path.module}/cloud-config")
  }
}

# Создаём сеть
resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

# Подсеть
resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  network_id     = yandex_vpc_network.network-1.id # Это аутпут. Обратимся к создаваемому значению
  v4_cidr_blocks = ["10.10.10.0/24"]
}
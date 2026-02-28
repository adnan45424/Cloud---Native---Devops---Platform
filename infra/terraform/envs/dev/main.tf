module "network" {
  source       = "../../modules/network"
  project_name = var.project_name
  env          = var.env
}

module "iam" {
  source       = "../../modules/iam"
  project_name = var.project_name
  env          = var.env
}

module "k8s" {
  source       = "../../modules/k8s"
  project_name = var.project_name
  env          = var.env
  network_id   = module.network.network_id
}
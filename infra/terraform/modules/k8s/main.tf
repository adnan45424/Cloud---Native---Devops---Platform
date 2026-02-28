resource "null_resource" "k8s" {
  triggers = {
    project    = var.project_name
    env        = var.env
    network_id = var.network_id
  }
}
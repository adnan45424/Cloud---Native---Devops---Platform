resource "null_resource" "network" {
  triggers = {
    project = var.project_name
    env     = var.env
  }
}
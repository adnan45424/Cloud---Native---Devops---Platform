resource "null_resource" "iam" {
  triggers = {
    project = var.project_name
    env     = var.env
  }
}
locals {
  service_name = "graphql-proxy-${var.testnet}"
}


resource "aws_cloudwatch_log_group" "graphql-proxy" {
  name              = local.service_name
  retention_in_days = 1
}

data "template_file" "container_definition" {
  template = "${file("${path.module}/templates/container-definition.json.tpl")}"

  vars = {
    log_group = local.service_name
    region    = "us-west-2"
    # graphql-proxy Vars
    proxy_container_version = var.proxy_container_version
    coda_graphql_host = var.coda_graphql_host
    coda_graphql_port = var.coda_rest_port
    # Daemon Vars
    coda_container_version = var.coda_container_version
    coda_wallet_keys   = var.coda_wallet_keys
    aws_access_key     = var.aws_access_key
    aws_secret_key     = var.aws_secret_key
    aws_default_region = var.aws_default_region
    coda_peer          = var.coda_peer
    coda_rest_port     = var.coda_rest_port
    coda_external_port = var.coda_external_port
    coda_metrics_port  = var.coda_metrics_port
    coda_privkey_pass  = var.coda_privkey_pass
  }
}

resource "aws_ecs_task_definition" "faucet" {
  family = local.service_name
  network_mode = "host"
  container_definitions = data.template_file.container_definition.rendered
}

resource "aws_ecs_service" "faucet" {
  name            = local.service_name
  cluster         = var.ecs_cluster_id
  task_definition = aws_ecs_task_definition.faucet.arn

  desired_count = 1

  deployment_maximum_percent         = 100
  deployment_minimum_healthy_percent = 0
}
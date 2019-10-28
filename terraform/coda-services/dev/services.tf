data "aws_secretsmanager_secret" "discord_api_key" {
  name = "coda-services/faucet/discord_api_key/staging"
}

data "aws_secretsmanager_secret_version" "current_discord_api_key" {
  secret_id = "${data.aws_secretsmanager_secret.discord_api_key.id}"
}

data "aws_secretsmanager_secret" "daemon_aws_access_keys" {
  name = "coda-services/daemon/daemon_aws_access_keys"
}

data "aws_secretsmanager_secret_version" "current_daemon_aws_access_keys" {
  secret_id = "${data.aws_secretsmanager_secret.daemon_aws_access_keys.id}"
}

# data "aws_secretsmanager_secret" "service_daemon_privkey_pass" {
#   name = "coda-services/daemon/service_daemon_privkey_pass"
# }

# data "aws_secretsmanager_secret_version" "current_service_daemon_privkey_pass" {
#   secret_id = "${data.aws_secretsmanager_secret.service_daemon_privkey_pass.id}"
# }

<<<<<<< Updated upstream
## Graphql Proxy
=======
## GraphQL Proxy
>>>>>>> Stashed changes
module "graphql-proxy" {
    #source = "github.com/codaprotocol/coda-automation/terraform/modules/services/prometheus"
    source = "../../modules/services/graphql-proxy"

    # Global Vars
    ecs_cluster_id = "coda-services"
    environment = "dev"
    testnet = "van-helsing"

    # Proxy Variables
    proxy_container_version = "0.0.10"
    coda_graphql_host = "localhost"
    coda_graphql_port = "10900"

    # Daemon Variables
    coda_container_version = "0.0.10-beta4"
    coda_wallet_keys = ""
    aws_access_key = jsondecode(data.aws_secretsmanager_secret_version.current_daemon_aws_access_keys.secret_string)["AWS_ACCESS_KEY_ID"]
    aws_secret_key = jsondecode(data.aws_secretsmanager_secret_version.current_daemon_aws_access_keys.secret_string)["AWS_SECRET_ACCESS_KEY"]
    aws_default_region = "us-west-2"
    coda_peer = "seared-kobe.o1test.net:8303"
    coda_rest_port = 10900
    coda_external_port = 10101
    coda_metrics_port = 10000
    coda_privkey_pass = "testnet"
}

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

data "aws_secretsmanager_secret" "user_privkey_pass" {
  name = "coda-services/daemon/user_privkey_pass"
}

data "aws_secretsmanager_secret_version" "current_user_privkey_pass" {
  secret_id = "${data.aws_secretsmanager_secret.user_privkey_pass.id}"
}

## Conners SnarkWorker
module "conner-snarkworker" {
    #source = "github.com/codaprotocol/coda-automation/terraform/modules/services/prometheus"
    source = "../../modules/services/daemon"

    # Global Vars
    ecs_cluster_id = "coda-services"
    environment = "dev"
    testnet = "van-helsing"

    # Daemon Variables
    daemon_name = "conners-snarkworker"
    coda_container_version = "0.0.10-beta4"
    coda_wallet_keys = "testnet/keys/affectionate_mauve_ape"
    aws_access_key = jsondecode(data.aws_secretsmanager_secret_version.current_daemon_aws_access_keys.secret_string)["AWS_ACCESS_KEY_ID"]
    aws_secret_key = jsondecode(data.aws_secretsmanager_secret_version.current_daemon_aws_access_keys.secret_string)["AWS_SECRET_ACCESS_KEY"]
    aws_default_region = "us-west-2"
    coda_peer = ""
    coda_rest_port = 10200
    coda_external_port = 10201
    coda_discovery_port = 10202
    coda_metrics_port = 10203
    coda_privkey_pass = jsondecode(data.aws_secretsmanager_secret_version.current_user_privkey_pass.secret_string)["coda_privkey_pass"]
    coda_snark_key = "tdNE5hh3P5aq8A9nZehrrKxsvoovxEHx9t2hDec2Novay4N6Pdq89W2YNkBbruYrhdLppwVZPqYLf1ChQiZg98MbJmcAKVfmbpeuQmn9WBmgTwD8a7SwTd1MfqPGHLon9GYVA2aw35C9mr"
}

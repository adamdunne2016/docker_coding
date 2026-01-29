## Run Kestra

docker run --pull=always --rm -it -p 8080:8080 --user=root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp kestra/kestra:latest server local



##  use this to encode the service account json
echo SECRET_GCP_SERVICE_ACCOUNT=$(cat service-account.json | base64 -w 0) >> .env_encoded

## need to change the .yaml to use secret(GCP_SERVICE_ACCOUNT) instead of kv(GOOGLE_CREDS)
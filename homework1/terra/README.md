# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan -var="project=<your-gcp-project-id>"
# Create new infra
terraform apply -var="project=<your-gcp-project-id>"
# Delete infra after your work, to avoid costs on any running services
terraform destroy

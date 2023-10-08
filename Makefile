export AWS_ENDPOINT_URL=http://localhost:4566
export LOCALSTACK_ENV=true

testing:
	@echo "Hello"

run docker:
	docker-compose up

stop docker:
	docker-compose down

start localstack:
	terraform init
	terraform apply

list-tables:
	aws dynamodb list-tables --endpoint-url http://localhost:4566

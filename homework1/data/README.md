## build the ingest data image

docker build -t green_ingest:v001 .


## run docker compose
docker-compose up


### load data
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet -O /tmp/green_tripdata_2025-11.parquet



docker run -it --rm \
  --network=data_default \
  -v /workspaces/docker_coding:/data \
  green_ingest:v001 \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=pgdatabase \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=green_taxi_trips_2025_11 \
  --chunksize=100000
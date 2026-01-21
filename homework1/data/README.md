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

  ## SQL Code

  #Q3
  select count(1) 
from green_taxi_trips_2025_11 
where lpep_pickup_datetime between '2025-11-01' and '2025-12-01'
and trip_distance <= 1;

8007

  # Q4
SELECT 
    DATE(lpep_pickup_datetime) AS pickup_date,
    MAX(trip_distance) AS max_trip_distance
FROM green_taxi_trips_2025_11
WHERE trip_distance < 100
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY max_trip_distance DESC
;

2025-11-14

# Q5
SELECT 
    count(*) as num_trips,
	"PULocationID"
FROM green_taxi_trips_2025_11
WHERE DATE(lpep_pickup_datetime) = '2025-11-18'
GROUP BY "PULocationID"
ORDER BY num_trips DESC
limit 10;

## need to import and merge the other csv

# build the image
docker build -f Dockerfile.zones -t zone_ingest:v001 .

run the docker
docker run -it --rm \
  --network=data_default \
  -v /workspaces/docker_coding:/data \
  zone_ingest:v001 \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=pgdatabase \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=taxi_zone_lookup \
  --chunksize=100000

  # Now redo the SQL
  SELECT 
    g."PULocationID" AS pickup_location_id,
	t."Zone" AS pickup_location,
    COUNT(*) AS num_trips
FROM green_taxi_trips_2025_11 g
LEFT JOIN taxi_zone_lookup t
       ON g."PULocationID"  = t."LocationID" 
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY g."PULocationID", t."Zone"
ORDER BY num_trips DESC
LIMIT 10;

Eash Harlem North 434 trips on the 18/11/2025

# Q6 
SELECT
	t_do."Zone" AS drop_off_location,
    MAX(tip_amount) AS max_tip
FROM green_taxi_trips_2025_11 g
LEFT JOIN taxi_zone_lookup t_pu
       ON g."PULocationID"  = t_pu."LocationID" 
LEFT JOIN taxi_zone_lookup t_do
ON g."DOLocationID"  = t_do."LocationID" 
WHERE t_pu."Zone" = 'East Harlem North'
GROUP BY t_do."Zone"
ORDER BY max_tip DESC
LIMIT 10;

Yorkville West max tip was 81.89
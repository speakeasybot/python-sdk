# destination

## Overview

Operations on destinations

### Available Operations

* [create_destination](#create_destination) - Create a new destination
* [get_destinations](#get_destinations) - Get all destinations

## create_destination

Create a new destination

### Example Usage

```python
import fabra
from fabra.models import shared

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)

req = shared.DestinationInput(
    bigquery_config=shared.BigQueryConfig(
        credentials='Paste JSON from GCP',
        location='us-west1',
    ),
    connection_type=shared.ConnectionTypeEnum.WEBHOOK,
    display_name='BigQuery',
    mongodb_config=shared.MongoDbConfig(
        connection_options='retryWrites=true&w=majority',
        host='examplecluster.abc123.mongodb.net',
        password='securePassword123',
        username='jane_doe',
    ),
    redshift_config=shared.RedshiftConfig(
        database_name='your_database',
        host='examplecluster.12345.us-west-1.redshift.amazonaws.com',
        password='securePassword123',
        port='5432',
        username='jane_doe',
    ),
    snowflake_config=shared.SnowflakeConfig(
        database_name='your_database',
        host='abc123.us-east4.gcp.snowflakecomputing.com',
        password='securePassword123',
        role='your_role',
        username='jane_doe',
        warehouse_name='your_warehouse',
    ),
)

res = s.destination.create_destination(req)

if res.create_destination_200_application_json_object is not None:
    # handle response
```

## get_destinations

Get all destinations

### Example Usage

```python
import fabra


s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)


res = s.destination.get_destinations()

if res.get_destinations_200_application_json_object is not None:
    # handle response
```

# connection

## Overview

Operations on connections

### Available Operations

* [get_namespaces](#get_namespaces) - Get all namespaces
* [get_schema](#get_schema) - Get schema for table
* [get_tables](#get_tables) - Get all tables

## get_namespaces

Get all namespaces

### Example Usage

```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetNamespacesRequest(
    connection_id=592845,
)

res = s.connection.get_namespaces(req)

if res.namespaces is not None:
    # handle response
```

## get_schema

Get schema for table

### Example Usage

```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetSchemaRequest(
    connection_id=715190,
    namespace='quibusdam',
    table_name='unde',
)

res = s.connection.get_schema(req)

if res.get_schema_200_application_json_object is not None:
    # handle response
```

## get_tables

Get all tables

### Example Usage

```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetTablesRequest(
    connection_id=857946,
    namespace='corrupti',
)

res = s.connection.get_tables(req)

if res.get_tables_200_application_json_object is not None:
    # handle response
```

# Fabra Python SDK

<div align="left">
   <p>Use the Fabra API to build customer-facing data warehouse integrations to let your customers start sending data to your application. Unblock your sales pipeline in days, not months.</p>
   <a href="https://github.com/fabra-io/python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/fabra-io/python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
   <a href="https://www.fabra.io/#Email-Hero"><img src="https://img.shields.io/static/v1?label=Docs&message=Sign Up&color=2ca47c&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install fabra
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import fabra
from fabra.models import operations, shared

s = fabra.Fabra()
s.config_security(
    security=shared.Security(
        api_key_auth=shared.SchemeAPIKeyAuth(
            api_key="YOUR_API_KEY_HERE",
        ),
    )
)
   
req = operations.GetNamespacesRequest(
    query_params=operations.GetNamespacesQueryParams(
        connection_id=548814,
    ),
)
    
res = s.connection.get_namespaces(req)

if res.get_namespaces_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### connection

* `get_namespaces` - Get all namespaces
* `get_schema` - Get schema for table
* `get_tables` - Get all tables

### destination

* `create_destination` - Create a new destination
* `get_destinations` - Get all destinations

### link_token

* `create_link_token` - Create a new link token

### object

* `create_object` - Create a new object
* `get_objects` - Get all objects

### source

* `create_source` - Create a new source
* `get_sources` - Get all sources

### sync

* `create_sync` - Create a new sync
* `get_syncs` - Get all syncs
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)

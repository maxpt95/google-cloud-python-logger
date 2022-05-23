# google-cloud-python-logger

Learn how to configure a logger for writing on Google Cloud

## Requirements

1. Install google clouds google-cloud-logging client libraries for python
2. Have a Google Cloud project
3. Have a Service Account that has logging privileges

## Configure Google Cloud Logging Handler

All you need to do is instatiate a cloud logging client and a CloudLoggingHandler and finally add the handler to your logger.

```python
client = google.cloud.logging.Client()
cloud_handler = CloudLoggingHandler(client, name=logger.name)
logger.addHandler(cloud_handler)
```

## Test It Out!

Log on Google Cloud by running the hello_world module or execute log_using_setup to see how you can log on console and on the cloud by previously configuring the logger

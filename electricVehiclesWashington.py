#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy
# pip install prometheus_client

import pandas as pd
from sodapy import Socrata
from prometheus_client import start_http_server, Gauge

# Start up the server to expose the metrics.
start_http_server(8000)

# Create Prometheus metrics to track the number of registered electric vehicles.
tesla_count = Gauge('registered_tesla_vehicles', 'Number of registered Tesla electric vehicles')
model_s_count = Gauge('registered_tesla_model_s_vehicles', 'Number of registered Tesla Model S vehicles')
model_3_count = Gauge('registered_tesla_model_3_vehicles', 'Number of registered Tesla Model 3 vehicles')
model_x_count = Gauge('registered_tesla_model_x_vehicles', 'Number of registered Tesla Model X vehicles')
model_y_count = Gauge('registered_tesla_model_y_vehicles', 'Number of registered Tesla Model Y vehicles')
roadster_count = Gauge('registered_tesla_roadster_vehicles', 'Number of registered Tesla Roadster vehicles')

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.wa.gov", None)

# Retrieve the number of registered Tesla electric vehicles.
tesla_results = client.get("f6w7-q2d2", select='count(*)', where="make = 'TESLA'")
tesla_count.set(int(tesla_results[0]['count']))

# Retrieve the number of registered Tesla Model S vehicles.
model_s_results = client.get("f6w7-q2d2", select='count(*)', where="make = 'TESLA' and model = 'MODEL S'")
model_s_count.set(int(model_s_results[0]['count']))

# Retrieve the number of registered Tesla Model 3 vehicles.
model_3_results = client.get("f6w7-q2d2", select='count(*)', where="make = 'TESLA' and model = 'MODEL 3'")
model_3_count.set(int(model_3_results[0]['count']))

# Retrieve the number of registered Tesla Model X vehicles.
model_x_results = client.get("f6w7-q2d2", select='count(*)', where="make = 'TESLA' and model = 'MODEL X'")
model_x_count.set(int(model_x_results[0]['count']))

# Retrieve the number of registered Tesla Model Y vehicles.
model_y_results = client.get("f6w7-q2d2", select='count(*)', where="make = 'TESLA' and model = 'MODEL Y'")
model_y_count.set(int(model_y_results[0]['count']))

# Retrieve the number of registered Tesla Roadster vehicles.
roadster_results = client.get("f6w7-q2d2", select='count(*)', where="make = 'TESLA' and model = 'ROADSTER'")
roadster_count.set(int(roadster_results[0]['count']))

# Run the Prometheus exporter.
while True:
    pass



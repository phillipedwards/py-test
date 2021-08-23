import pulumi
import os

print("Dump environment variable PULUMI_CONFIG")
print(os.environ["PULUMI_CONFIG"])

print("Loading config...")
config = pulumi.Config("alb")

# created in yaml file as a JSON array. Eg- ['value']
print("Loading JSON subnet ids...")
config.require_object("subnet-ids-json")

print("Test string - environment")
env = config.require("environment")
print(f"ENVIRONMENT: {env}")

#reated in  yaml file as a YAML array. Eg- 
# name:
#  - value
print("Test object array - subnet ids")
subnet_ids = config.require_object("subnet-ids")
print(f"SUBNET IDS: {subnet_ids}")
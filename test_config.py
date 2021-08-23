import unittest
import pulumi
import yaml
import os
import json

class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        return {}
    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}

"""function to hydrate the PULUMI_CONFIG environment variable from our stack configuration file"""
def set_config():
    with open("./Pulumi.dev.yaml", "r") as file:
        data = yaml.full_load(file)
        os.environ["PULUMI_CONFIG"] = json.dumps(data["config"])

set_config()
pulumi.runtime.set_mocks(MyMocks(), stack="dev")

import infra

@pulumi.runtime.test
def verify_subnets():
    
    print("SUCCESS!")

if __name__ == "__main__":
    unittest.main()
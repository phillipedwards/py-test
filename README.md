# Pulumi, Python, Unit Tests, and require_object() error
When executing Pulumi Unit Tests, the Pulumi stack configuration must be set as the environment variable "PULUMI_CONFIG", in order for the tests to have access to the stack configuratiion. Unfortunately, the Pulumi configuration method, `require_object` throws an error when an array value is encountered in the configuration.  

Note: Pulumi.{stack}.yaml file included has both JSON and YAML type array values. Both should be retrievable using `require_object` during a preview/up opeeration and unit tests. Neither can be retrieved during unit tests.

## Steps to Reproduce Issue
1. Clone this repo
2. python(3) -m pip install -r requirements.txt
3. pulumi preview
4. python(3) -m unittest

## Expected
Steps 3 and 4 (`pulumi preview` and `python3 -m unittest`) should successfully execute and write configuration values to CLI.

## Actual
Step 3 `pulumi preview` successfully writes configuration values to CLI.  
Step 4 `python3 -m unittest` fails due to an error which reads, `pulumi.config.ConfigTypeError: Configuration 'alb:subnet-ids-json' value '['subnet-123']' is not a valid 'JSON object'`

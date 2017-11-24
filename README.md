# AWS MFA Authenticator

AWS MFA Authenticator tool to make using the AWS CLI with MFA easier.

## Usage

### Dependencies

This tool requires:

 * Python3.6 or higher
 * aws-cli (installed and configured)

### Configuration

Before using this script, you must configure the tool with the ARN of the MFA device for the AWS profile you wish to authenticate with.

 * `aws-mfa-auth --configure`

### Usage

Provide the token the first time you run the script:

 * `aws-mfa-auth --token <MFA_DEVICE_TOKEN>`

Then simply run `aws-mfa-auth` to output the environment variables to setup authentication.

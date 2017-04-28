# aws-mfa

AWS CLI multi-factor authentication switcher.

This script can be use to easily switch the default AWS CLI credentials to the temporarily authorized MFA session.

## Usage

### Initial Setup

First you need to set the **mfa arn** from your user in your aws-cli `credentials` settings file.

 1. Edit `~/.aws/credentials` and add the following:

 ```
[account_name]
aws_access_key_id = <insert_access_key>
aws_secret_access_key = <insert secret access key>
mfa_arn = <insert the ARN for your MFA device>
 ```
 2. Save the file.

### Authentication

Run the script like this:

```
aws-mfa.py <account_name> <MFA token>
```

The script will then retrieve the `aws_access_key_id`, `aws_secret_access_key` and `aws_session_token` for your session and set it to the **default** account in the credentials file.

You can now continue to use the aws-cli with the authenticated user.

## Developer Notes

I am aware that I need to add the following to the script:

 * Improved error handling.
 * CLI Help messages.
 * Unit Tests.

If you find this script useful please feel free to contribute to it. I'm open to Pull Requests from anyone.

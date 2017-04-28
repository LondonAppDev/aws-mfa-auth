#!/usr/bin/env python
import sys
import subprocess
import json
import os

import ConfigParser


aws_credentials_path = '{0}{1}'.format(
    os.path.expanduser('~'),
    '/.aws/credentials')


def load_config():
    """Loads the AWS Config."""

    config = ConfigParser.ConfigParser()
    config.read(aws_credentials_path)

    return config


def set_default_config(access_key_id, secret_access_key, session_token):
    """Sets the default config."""

    parser = load_config()
    parser.set('default', 'aws_access_key_id', access_key_id)
    parser.set('default', 'aws_secret_access_key', secret_access_key)
    parser.set('default', 'aws_session_token', session_token)
    parser.set('default', 'test', 'test')

    with open(aws_credentials_path, 'wb') as configfile:
        parser.write(configfile)

    print("DONE!")


def aws_auth(arn, token, profile):
    """Start AWS Auth."""

    out = subprocess.check_output([
        'aws', 'sts', 'get-session-token',
        '--serial-number', arn,
        '--token-code', token,
        '--profile', profile
    ])

    response = json.loads(out)
    creds = response.get('Credentials')
    aws_access_key_id = creds.get('AccessKeyId')
    aws_secret_access_key = creds.get('SecretAccessKey')
    aws_session_token = creds.get('SessionToken')

    set_default_config(
        aws_access_key_id, aws_secret_access_key, aws_session_token)


def process(args):
    """Process the args."""

    profile = args[1]
    token = args[2]

    config = load_config()

    arn = config.get(profile, 'mfa_arn')
    aws_auth(arn, token, profile)


if __name__ == '__main__':

    args = sys.argv

    load_config()
    process(args)

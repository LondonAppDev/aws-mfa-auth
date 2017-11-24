AWS MFA Authenticator
=====================

Abstract
--------

AWS MFA Authenticator tool to make using the AWS CLI with MFA easier.

Requirements
------------

 - Python 3.6+
 - aws-cli (installed and configured)

Installation
------------

Install using `pip install aws-mfa-auth`.

Usage
-----

Before using this script, you must configure the tool with the ARN of the MFA device for the AWS profile you wish to authenticate with.

.. code-block:: none

    aws-mfa-auth --configure

Once configured, provide the token the first time you run the script:

.. code-block:: none

    aws-mfa-auth --token <MFA_DEVICE_TOKEN>

Then simply run `aws-mfa-auth` to output the environment variables to setup authentication.

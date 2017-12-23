from setuptools import setup
import os


PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))


def relative_path(path, base_dir=PACKAGE_ROOT):
    return os.path.join(base_dir, path)


def readme():
    with open(relative_path('README.rst'), 'r') as f:
        return f.read()


setup(
    name='aws-mfa-auth',
    version='0.0.8',
    description='Easy AWS MFA Authentication',
    author='Mark Winterbottom',
    author_email='mark@londonappdeveloper.com',
    scripts=['aws-mfa-auth'],
    install_requires=['awscli', 'pytz'],
    url='https://github.com/londonappdev/aws-mfa-auth',
    long_description=readme(),
    python_requires='>=3',
    keywords='aws mfa authentication multi-factor auth'
)

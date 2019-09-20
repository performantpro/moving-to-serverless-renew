"""
    cloudalbum/tests/test_config.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    Test cases for application configuration

    :description: CloudAlbum is a fully featured sample application for 'Moving to AWS serverless' training course
    :copyright: © 2019 written by Dayoungle Jun, Sungshik Jou.
    :license: MIT, see LICENSE for more details.
"""
import unittest
from flask import current_app
from flask_testing import TestCase
from cloudalbum import create_app

app = create_app()


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('cloudalbum.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'dev_secret')
        self.assertFalse(current_app is None)

        # Required config value for DynamoDB
        self.assertIsNotNone(app.config['DDB_RCU'])
        self.assertIsNotNone(app.config['DDB_WCU'])

        # Required config value for S3
        self.assertIsNotNone(app.config['S3_PHOTO_BUCKET'])

        # Required config value for COGNITO
        self.assertIsNotNone(app.config['COGNITO_POOL_ID'])
        self.assertIsNotNone(app.config['COGNITO_CLIENT_ID'])
        self.assertIsNotNone(app.config['COGNITO_CLIENT_SECRET'])


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('cloudalbum.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'test_secret')
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])

        # Required config value for DynamoDB
        self.assertIsNotNone(app.config['DDB_RCU'])
        self.assertIsNotNone(app.config['DDB_WCU'])

        # Required config value for S3
        self.assertIsNotNone(app.config['S3_PHOTO_BUCKET'])

        # Required config value for COGNITO
        self.assertIsNotNone(app.config['COGNITO_POOL_ID'])
        self.assertIsNotNone(app.config['COGNITO_CLIENT_ID'])
        self.assertIsNotNone(app.config['COGNITO_CLIENT_SECRET'])


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('cloudalbum.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'prod_secret')
        self.assertFalse(app.config['TESTING'])

        # Required config value for DynamoDB
        self.assertIsNotNone(app.config['DDB_RCU'])
        self.assertIsNotNone(app.config['DDB_WCU'])

        # Required config value for S3
        self.assertIsNotNone(app.config['S3_PHOTO_BUCKET'], msg='S3_PHOTO_BUCKET is not set!')

        # Required config value for COGNITO
        self.assertIsNotNone(app.config['COGNITO_POOL_ID'], msg='COGNITO_POOL_ID is not set!')
        self.assertIsNotNone(app.config['COGNITO_CLIENT_ID'], msg='COGNITO_CLIENT_ID is not set!')
        self.assertIsNotNone(app.config['COGNITO_CLIENT_SECRET'], msg='COGNITO_CLIENT_SECRET is not set!')


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test import Client


class BorgTestCase(TestCase):

    def setUp(self):
        self.robots_client = Client()
        self.robots_response = self.robots_client.get("/robots.txt")

        self.humans_client = Client()
        self.humans_response = self.humans_client.get("/humans.txt")

    def test_robots_200(self):
        """Ensure robots.txt file exists"""
        self.assertEqual(self.robots_response.status_code, 200)

    def test_robots_is_text(self):
        """Robots.txt should be sent as text"""
        self.assertEqual(self.robots_response['Content-Type'], 'text/plain')

    def test_humans_200(self):
        """Ensure humans.txt file exists"""
        self.assertEqual(self.humans_response.status_code, 200)

    def test_humans_is_text(self):
        """Humans.txt should be sent as text"""
        self.assertEqual(self.humans_response['Content-Type'], 'text/plain')

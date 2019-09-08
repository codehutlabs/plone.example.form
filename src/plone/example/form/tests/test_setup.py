# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone.example.form.testing import PLONE_EXAMPLE_FORM_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plone.example.form is properly installed."""

    layer = PLONE_EXAMPLE_FORM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plone.example.form is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plone.example.form'))

    def test_browserlayer(self):
        """Test that IPloneExampleFormLayer is registered."""
        from plone.example.form.interfaces import (
            IPloneExampleFormLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneExampleFormLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_EXAMPLE_FORM_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plone.example.form'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone.example.form is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plone.example.form'))

    def test_browserlayer_removed(self):
        """Test that IPloneExampleFormLayer is removed."""
        from plone.example.form.interfaces import \
            IPloneExampleFormLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPloneExampleFormLayer,
            utils.registered_layers())

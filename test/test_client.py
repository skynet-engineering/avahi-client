import threading
from unittest import TestCase

import mock

from avahi import types
from avahi.client import AvahiClient
from avahi.client import parse_txt
from avahi.client import unescape_unicode
from avahi.service import Service
from test.fixtures import avahi


class TestClient(TestCase):
    def setUp(self):
        self.instance = AvahiClient()

    def test_unescape_unicode(self):
        self.assertEqual(
            unescape_unicode('EPSON\\032XP-410\\032Series'),
            'EPSON XP-410 Series',
        )

    def test_parse_txt(self):
        txt = '"name=name" "detail=detail"'
        self.assertEqual(
            parse_txt(txt),
            {'name': 'name', 'detail': 'detail'},
        )

    @mock.patch.object(threading, 'Thread')
    def test_publish_service(self, mock_thread):
        self.instance.publish_service('name', types.HTTP, 5000)
        _, kwargs = mock_thread.call_args

        self.assertEqual(kwargs['args'], (['-s', 'name', types.HTTP, 5000],))

    @mock.patch.object(AvahiClient, '_browse', return_value=avahi.BROWSE_OUTPUT)
    def test_browse_services(self, mock_browse):
        services = list(self.instance.browse_services())
        (args,), _ = mock_browse.call_args

        self.assertEqual(args[-1], types.HTTP)
        self.assertEqual(
            services,
            [
                Service(
                    ip='fe80::c0:76ff:fe46:7ee7',
                    name='Jenkins',
                    port=80,
                    txt={
                        'url': 'https://ci.internal.kevinlin.info/',
                        'path': '/',
                        'version': '2.89.3',
                        'server-id': 'f7c6286d2a10a8dc7c86c825a30beb31',
                    },
                ),
                Service(
                    ip='10.0.0.254',
                    name='EPSON XP-410 Series',
                    port=80,
                    txt={},
                ),
            ],
        )

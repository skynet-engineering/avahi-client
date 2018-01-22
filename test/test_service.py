from unittest import TestCase

from avahi.service import Service


class TestService(TestCase):
    def test_properties(self):
        service = Service(
            ip='ip',
            name='name',
            port=5000,
            txt={
                'detail': 'detail',
            },
        )

        self.assertEqual(service.ip, 'ip')
        self.assertEqual(service.name, 'name')
        self.assertEqual(service.port, 5000)
        self.assertEqual(service.txt, {'detail': 'detail'})

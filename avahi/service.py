class Service(object):
    """
    Class representing an Avahi service.
    """

    def __init__(self, ip, name, port, txt={}):
        """
        Create a service representation.

        :param ip: IP of the host.
        :param name: Name of the service.
        :param port: Port registered by the service.
        :param txt: Optional mapping of txt records.
        """
        self.ip = ip
        self.name = name
        self.port = port
        self.txt = txt

    def __repr__(self):
        """
        Generate a string representation of this service.

        :return: Representation of this service.
        """
        return 'Service(ip={ip}, name={name}, port={port}, txt={txt})'.format(
            ip=self.ip,
            name=self.name,
            port=self.port,
            txt=self.txt,
        )

    def __eq__(self, other):
        """
        Equality check against another Service.

        :param other: Another object to compare against.
        :return: True if the two Services are equal.
        """
        return (
            isinstance(other, Service) and
            other.ip == self.ip and
            other.name == self.name and
            other.port == self.port and
            other.txt == self.txt
        )

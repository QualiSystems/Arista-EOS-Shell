from cloudshell.networking.arista.eos.autoload.arista_eos_autoload_structure import GenericPort, GenericPortChannel, \
    AristaEOSDevice, GenericChassis, GenericModule, GenericPowerPort

from cloudshell.networking.cisco.autoload.cisco_generic_snmp_autoload import CiscoGenericSNMPAutoload


class AristaEOSAutoload(CiscoGenericSNMPAutoload):
    def __init__(self, snmp_handler, logger, supported_os, resource_name):
        super(AristaEOSAutoload, self).__init__(snmp_handler, logger, supported_os, resource_name)
        self.port = GenericPort
        self.power_port = GenericPowerPort
        self.port_channel = GenericPortChannel
        self.root_model = AristaEOSDevice
        self.chassis = GenericChassis
        self.module = GenericModule
        self._vendor = 'Arista'
        self._product_mibs = ['ARISTA-PRODUCTS-MIB']

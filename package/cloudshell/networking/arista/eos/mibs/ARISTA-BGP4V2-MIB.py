# PySNMP SMI module. Autogenerated from smidump -f python ARISTA-BGP4V2-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jan 31 10:06:36 2017,
# Python version sys.version_info(major=2, minor=7, micro=6, releaselevel='final', serial=0)

# Imports

( AristaBgp4V2AddressFamilyIdentifierTC, AristaBgp4V2IdentifierTC, AristaBgp4V2SubsequentAddressFamilyIdentifierTC, ) = mibBuilder.importSymbols("", "AristaBgp4V2AddressFamilyIdentifierTC", "AristaBgp4V2IdentifierTC", "AristaBgp4V2SubsequentAddressFamilyIdentifierTC")
( aristaExperiment, ) = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaExperiment")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressPrefixLength, InetAddressType, InetAutonomousSystemNumber, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength", "InetAddressType", "InetAutonomousSystemNumber", "InetPortNumber")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowPointer, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TimeStamp", "TruthValue")

# Objects

aristaBgp4V2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 4, 1)).setRevisions(("2014-08-15 00:00","2012-10-19 00:00","2012-03-11 00:00",))
if mibBuilder.loadTexts: aristaBgp4V2.setOrganization("Arista Networks, Inc.")
if mibBuilder.loadTexts: aristaBgp4V2.setContactInfo("Arista Networks, Inc.\n\nPostal: 5453 Great America Parkway\n        Santa Clara, CA 95054\n\nTel: +1 408 547-5500\n\nE-mail: snmp@arista.com")
if mibBuilder.loadTexts: aristaBgp4V2.setDescription("The MIB module for the BGP-4 protocol.\nThis version was published in\ndraft-ietf-idr-bgp4-mibv2-13, and\nmodified to be homed inside the Arista\nenterprise.  There were no other\nmodifications.\n\nCopyright (C) The IETF Trust (2012).  This\nversion of this MIB module is part of\ndraft-ietf-idr-bgp4-mibv2-13.txt;\nsee the draft itself for full legal notices.")
aristaBgp4V2Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 4, 1, 0))
aristaBgp4V2Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1))
aristaBgp4V2DiscontinuityTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 1))
if mibBuilder.loadTexts: aristaBgp4V2DiscontinuityTable.setDescription("Table of BGP-4 discontinuities.  Discontinuities that have\nexternal visibility occur on a per-BGP instance basis.\nTransitions by a given BGP peer will result in a consistent\nBGP view within that instance and thus do not represent a\ndiscontinuity from a protocol standpoint.")
aristaBgp4V2DiscontinuityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 1, 1)).setIndexNames((0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"))
if mibBuilder.loadTexts: aristaBgp4V2DiscontinuityEntry.setDescription("Entry repsenting information about a discontinuity event\nfor a given BGP instance.")
aristaBgp4V2DiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 1, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2DiscontinuityTime.setDescription("The value of sysUpTime at the most recent occasion at which\nthis BGP management instance has suffered a discontinuity.")
aristaBgp4V2PeerTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2))
if mibBuilder.loadTexts: aristaBgp4V2PeerTable.setDescription("BGP peer table.  This table contains, one entry per BGP\npeer, information about the connections with BGP peers.")
aristaBgp4V2PeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1)).setIndexNames((0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddrType"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddr"))
if mibBuilder.loadTexts: aristaBgp4V2PeerEntry.setDescription("Entry containing information about the connection with\na remote BGP peer.")
aristaBgp4V2PeerInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaBgp4V2PeerInstance.setDescription("The routing instance index.\n\nSome BGP implementations permit the creation of\nmultiple instances of a BGP routing process. An\nexample includes routers running BGP/MPLS IP Virtual\nPrivate Networks.\n\nImplementations that do not support multiple\nrouting instances should return 1 for this object.")
aristaBgp4V2PeerLocalAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLocalAddrType.setDescription("The address family of the local end of the peering\nsession.")
aristaBgp4V2PeerLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLocalAddr.setDescription("The local IP address of this entry's BGP connection.\n\nAn implementation is required to support IPv4 peering\nsessions in which case the length of this object is 4.\nAn implementation MAY support IPv6 peering\nsessions in which case the length of this object is 16.\nIPv6 link-local peering sessions MAY be supported by\nthis MIB.  In this case the length of this object is 20.")
aristaBgp4V2PeerRemoteAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 4), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaBgp4V2PeerRemoteAddrType.setDescription("The address family of the remote end of the peering\nsession.\n\nAn implementation is required to support IPv4 peering\nsessions in which case the length of this object is 4.\nAn implementation MAY support IPv6 peering\nsessions in which case the length of this object is 16.\nIPv6 link-local peering sessions MAY be supported by\nthis MIB.  In this case the length of this object is 20.")
aristaBgp4V2PeerRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 5), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaBgp4V2PeerRemoteAddr.setDescription("The remote IP address of this entry's BGP peer.")
aristaBgp4V2PeerLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 6), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLocalPort.setDescription("The local port for the TCP connection between the BGP\npeers.")
aristaBgp4V2PeerLocalAs = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 7), InetAutonomousSystemNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLocalAs.setDescription("Some implementations of BGP can represent themselves\nas multiple ASes. This is the AS that this peering\nsession is representing itself as to the remote peer.")
# aristaBgp4V2PeerLocalIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 8)
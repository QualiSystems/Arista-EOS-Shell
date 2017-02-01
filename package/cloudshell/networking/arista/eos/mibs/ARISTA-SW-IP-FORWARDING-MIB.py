# PySNMP SMI module. Autogenerated from smidump -f python ARISTA-SW-IP-FORWARDING-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jan 31 10:06:37 2017,
# Python version sys.version_info(major=2, minor=7, micro=6, releaselevel='final', serial=0)

# Imports

( aristaMibs, ) = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetVersion, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetVersion")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp")

# Objects

aristaSwIpForwardingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 1)).setRevisions(("2014-08-15 00:00","2011-03-31 13:00","2010-01-31 00:00","2009-03-16 00:00",))
if mibBuilder.loadTexts: aristaSwIpForwardingMIB.setOrganization("Arista Networks, Inc.")
if mibBuilder.loadTexts: aristaSwIpForwardingMIB.setContactInfo("Arista Networks, Inc.\n\nPostal: 5453 Great America Parkway\n        Santa Clara, CA 95054\n\nTel: +1 408 547-5500\n\nE-mail: snmp@arista.com")
if mibBuilder.loadTexts: aristaSwIpForwardingMIB.setDescription("This MIB contains counters for software-forwarded packets.")
aristaSwFwdIp = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1))
aristaSwFwdIpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1))
if mibBuilder.loadTexts: aristaSwFwdIpStatsTable.setDescription("The table containing system wide, IP version specific\ntraffic statistics.  This table and the ipIfStatsTable\ncontain similar objects whose difference is in their\ngranularity.  Where this table contains system wide traffic\nstatistics, the ipIfStatsTable contains the same statistics\nbut counted on a per-interface basis.")
aristaSwFwdIpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1)).setIndexNames((0, "ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsIPVersion"))
if mibBuilder.loadTexts: aristaSwFwdIpStatsEntry.setDescription("A statistics entry containing system-wide objects for a\nparticular IP version.")
aristaSwFwdIpStatsIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 1), InetVersion()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaSwFwdIpStatsIPVersion.setDescription("The IP version of this row.")
aristaSwFwdIpStatsInReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInReceives.setDescription("The total number of input IP datagrams received in software,\nincluding those received in error.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCInReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCInReceives.setDescription("The total number of input IP datagrams received in software,\nincluding those received in error.  This object counts the same\ndatagrams as aristaSwFwdIpStatsInReceives, but allows for larger\nvalues.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInOctets.setDescription("The total number of octets received in software in input IP\ndatagrams, including those received in error.  Octets from\ndatagrams counted in aristaSwFwdIpStatsInReceives MUST be\ncounted here.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCInOctets.setDescription("The total number of octets received in software in input IP\ndatagrams, including those received in error.  This object\ncounts the same octets as aristaSwFwdIpStatsInOctets, but\nallows for larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInHdrErrors.setDescription("The number of input IP datagrams discarded in software due\nto errors in their IP headers, including version number\nmismatch, other format errors, hop count exceeded, errors\ndiscovered in processing their IP options, etc.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInNoRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInNoRoutes.setDescription("The number of input IP datagrams discarded in software\nbecause no route could be found to transmit them to their\ndestination.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInAddrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInAddrErrors.setDescription("The number of input IP datagrams discarded in software\nbecause the IP address in their IP header's destination field\nwas not a valid address to be received at this entity.  This\ncount includes invalid addresses (e.g., ::0).  For entities\nthat are not IP routers and therefore do not forward\ndatagrams, this counter includes datagrams discarded\nbecause the destination address was not a local address.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInUnknownProtos.setDescription("The number of locally-addressed IP datagrams received\nsuccessfully in software but discarded because of an\nunknown or unsupported protocol.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInTruncatedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInTruncatedPkts.setDescription("The number of input IP datagrams discarded in software\nbecause the datagram frame didn't carry enough data.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInForwDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInForwDatagrams.setDescription("The number of input datagrams for which this entity was not\ntheir final IP destination and for which this entity\nattempted in software to find a route to forward them to\nthat final destination.  In entities that do not act as IP\nrouters, this counter will include only those datagrams that\nwere Source-Routed via this entity, and the Source-Route\nprocessing was successful.\n\nWhen tracking interface statistics, the counter of the\nincoming interface is incremented for each datagram.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCInForwDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCInForwDatagrams.setDescription("The number of input datagrams for which this entity was not\ntheir final IP destination and for which this entity\nattempted in software to find a route to forward them\nto that final destination.  This object counts the same\npackets as aristaSwFwdIpStatsInForwDatagrams, but allows\nfor larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsReasmReqds = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsReasmReqds.setDescription("The number of IP fragments received that needed to be\nreassembled at this interface.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsReasmOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsReasmOKs.setDescription("The number of IP datagrams successfully reassembled.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsReasmFails = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsReasmFails.setDescription("The number of failures detected by the IP re-assembly\nalgorithm (for whatever reason: timed out, errors, etc.).\nNote that this is not necessarily a count of discarded IP\nfragments since some algorithms (notably the algorithm in\nRFC 815) can lose track of the number of fragments by\ncombining them as they are received.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInDiscards.setDescription("The number of input IP datagrams received in software for\nwhich no problems were encountered to prevent their\ncontinued processing, but were discarded (e.g., for lack of\nbuffer space).  Note that this counter does not include any\ndatagrams discarded while awaiting re-assembly.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInDelivers = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInDelivers.setDescription("The total number of datagrams successfully delivered to IP\nuser-protocols (including ICMP).\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCInDelivers = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCInDelivers.setDescription("The total number of datagrams successfully delivered to IP\nuser-protocols (including ICMP).  This object counts the\nsame packets as aristaSwFwdIpStatsInDelivers, but allows for\nlarger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutRequests.setDescription("The total number of IP datagrams that local IP user-\nprotocols (including ICMP) supplied to IP in requests for\ntransmission.  Note that this counter does not include any\ndatagrams counted in aristaSwFwdIpStatsOutForwDatagrams.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCOutRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCOutRequests.setDescription("The total number of IP datagrams that local IP user-\nprotocols (including ICMP) supplied to IP in requests for\ntransmission.  This object counts the same packets as\naristaSwFwdIpStatsOutRequests, but allows for larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutNoRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutNoRoutes.setDescription("The number of locally generated IP datagrams discarded\nbecause no route could be found to transmit them to their\ndestination.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutForwDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutForwDatagrams.setDescription("The number of datagrams for which this entity was not their\nfinal IP destination and for which it was successful in\nfinding a path to their final destination in software.\nIn entities that do not act as IP routers, this counter will\ninclude only those datagrams that were Source-Routed via\nthis entity, and the Source-Route processing was successful.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCOutForwDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCOutForwDatagrams.setDescription("The number of datagrams for which this entity was not their\nfinal IP destination and for which it was successful\nin finding a path to their final destination in\nsoftware.  This object counts the same packets as\naristaSwFwdIpStatsOutForwDatagrams, but allows for larger\nvalues.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutDiscards.setDescription("The number of output IP datagrams for which no problem was\nencountered to prevent their transmission to their\ndestination, but were discarded in software (e.g., for lack\nof buffer space).  Note that this counter would include\ndatagrams counted in aristaSwFwdIpStatsOutForwDatagrams if\nany such datagrams met this (discretionary) discard criterion.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutFragReqds = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutFragReqds.setDescription("The number of IP datagrams that would require fragmentation\nin order to be transmitted.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutFragOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutFragOKs.setDescription("The number of IP datagrams that have been successfully\nfragmented.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutFragFails = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutFragFails.setDescription("The number of IP datagrams that have been discarded because\nthey needed to be fragmented but could not be.  This\nincludes IPv4 packets that have the DF bit set and IPv6\npackets that are being forwarded and exceed the outgoing\nlink MTU.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutFragCreates = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutFragCreates.setDescription("The number of output datagram fragments that have been\ngenerated as a result of IP fragmentation.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutTransmits = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutTransmits.setDescription("The total number of IP datagrams that this entity supplied\nby software to the lower layers for transmission.  This\nincludes datagrams generated locally and those forwarded in\nsoftware by this entity.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCOutTransmits = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCOutTransmits.setDescription("The total number of IP datagrams that this entity supplied\nby software to the lower layers for transmission.  This object\ncounts the same datagrams as aristaSwFwdIpStatsOutTransmits,\nbut allows for larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutOctets.setDescription("The total number of octets in IP datagrams delivered by software\nto the lower layers for transmission.  Octets from datagrams\ncounted in aristaSwFwdIpStatsOutTransmits MUST be counted\nhere.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCOutOctets.setDescription("The total number of octets in IP datagrams delivered by software\nto the lower layers for transmission.  This objects counts\nthe same octets as aristaSwFwdIpStatsOutOctets, but allows\nfor larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInMcastPkts.setDescription("The number of IP multicast datagrams received by software.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCInMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCInMcastPkts.setDescription("The number of IP multicast datagrams received by software.\nThis object counts the same datagrams as\naristaSwFwdIpStatsInMcastPkts but allows for larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInMcastOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInMcastOctets.setDescription("The total number of octets received by software in\nIP multicast datagrams.  Octets from datagrams counted in\naristaSwFwdIpStatsInMcastPkts MUST be counted here.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCInMcastOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCInMcastOctets.setDescription("The total number of octets received by software in\nIP multicast datagrams.  This object counts the same octets as\naristaSwFwdIpStatsInMcastOctets, but allows for larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutMcastPkts.setDescription("The number of IP multicast datagrams transmitted by software.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCOutMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCOutMcastPkts.setDescription("The number of IP multicast datagrams transmitted by software.\nThis object counts the same datagrams as\naristaSwFwdIpStatsOutMcastPkts, but allows for larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutMcastOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutMcastOctets.setDescription("The total number of octets transmitted by software in IP\nmulticast datagrams.  Octets from datagrams counted in\naristaSwFwdIpStatsOutMcastPkts MUST be counted here.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCOutMcastOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCOutMcastOctets.setDescription("The total number of octets transmitted by software in IP\nmulticast datagrams.  This object counts the same octets as\naristaSwFwdIpStatsOutMcastOctets, but allows for larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsInBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsInBcastPkts.setDescription("The number of IP broadcast datagrams received by software.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCInBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCInBcastPkts.setDescription("The number of IP broadcast datagrams received by software.\nThis object counts the same datagrams as\naristaSwFwdIpStatsInBcastPkts but allows for larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsOutBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsOutBcastPkts.setDescription("The number of IP broadcast datagrams transmitted by software.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsHCOutBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsHCOutBcastPkts.setDescription("The number of IP broadcast datagrams transmitted by software.\nThis object counts the same datagrams as\naristaSwFwdIpStatsOutBcastPkts, but allows for larger values.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\naristaSwFwdIpStatsDiscontinuityTime.")
aristaSwFwdIpStatsDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 46), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which\nany one or more of this entry's counters suffered a\ndiscontinuity.\n\nIf no such discontinuities have occurred since the last re-\ninitialization of the local management subsystem, then this\nobject contains a zero value.")
aristaSwFwdIpStatsRefreshRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 47), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaSwFwdIpStatsRefreshRate.setDescription("The minimum reasonable polling interval for this entry.\nThis object provides an indication of the minimum amount of\ntime required to update the counters in this entry.")
aristaSwIpFwdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 1, 2))
aristaSwIpFwdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 1))
aristaSwIpFwdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 2))

# Augmentions

# Groups

aristaSwFwdIpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 2, 1)).setObjects(*(("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutForwDatagrams"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInUnknownProtos"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInForwDatagrams"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutBcastPkts"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsReasmOKs"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutMcastPkts"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsRefreshRate"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInAddrErrors"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutFragFails"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutDiscards"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInBcastPkts"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInNoRoutes"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutFragCreates"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInTruncatedPkts"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutRequests"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutForwDatagrams"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsReasmFails"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutFragReqds"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInForwDatagrams"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInReceives"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutMcastPkts"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInDiscards"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInHdrErrors"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutFragOKs"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutTransmits"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInDelivers"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInMcastPkts"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInMcastPkts"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsReasmReqds"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutBcastPkts"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInBcastPkts"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutTransmits"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsDiscontinuityTime"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInReceives"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutRequests"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutNoRoutes"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInDelivers"), ) )
if mibBuilder.loadTexts: aristaSwFwdIpStatsGroup.setDescription("The group of required statistics objects.")
aristaSwFwdIpOctetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 2, 2)).setObjects(*(("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInMcastOctets"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInOctets"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutOctets"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutMcastOctets"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutMcastOctets"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInOctets"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutOctets"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInMcastOctets"), ) )
if mibBuilder.loadTexts: aristaSwFwdIpOctetGroup.setDescription("Octet counters, which are not supported on all systems.")

# Compliances

aristaSwIpFwdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 1, 2)).setObjects(*(("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpOctetGroup"), ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsGroup"), ) )
if mibBuilder.loadTexts: aristaSwIpFwdMIBCompliance.setDescription("The compliance statement for Arista switches that support\nsoftware forwarding of IPv4 and/or IPv6 packets.")

# Exports

# Module identity
mibBuilder.exportSymbols("ARISTA-SW-IP-FORWARDING-MIB", PYSNMP_MODULE_ID=aristaSwIpForwardingMIB)

# Objects
mibBuilder.exportSymbols("ARISTA-SW-IP-FORWARDING-MIB", aristaSwIpForwardingMIB=aristaSwIpForwardingMIB, aristaSwFwdIp=aristaSwFwdIp, aristaSwFwdIpStatsTable=aristaSwFwdIpStatsTable, aristaSwFwdIpStatsEntry=aristaSwFwdIpStatsEntry, aristaSwFwdIpStatsIPVersion=aristaSwFwdIpStatsIPVersion, aristaSwFwdIpStatsInReceives=aristaSwFwdIpStatsInReceives, aristaSwFwdIpStatsHCInReceives=aristaSwFwdIpStatsHCInReceives, aristaSwFwdIpStatsInOctets=aristaSwFwdIpStatsInOctets, aristaSwFwdIpStatsHCInOctets=aristaSwFwdIpStatsHCInOctets, aristaSwFwdIpStatsInHdrErrors=aristaSwFwdIpStatsInHdrErrors, aristaSwFwdIpStatsInNoRoutes=aristaSwFwdIpStatsInNoRoutes, aristaSwFwdIpStatsInAddrErrors=aristaSwFwdIpStatsInAddrErrors, aristaSwFwdIpStatsInUnknownProtos=aristaSwFwdIpStatsInUnknownProtos, aristaSwFwdIpStatsInTruncatedPkts=aristaSwFwdIpStatsInTruncatedPkts, aristaSwFwdIpStatsInForwDatagrams=aristaSwFwdIpStatsInForwDatagrams, aristaSwFwdIpStatsHCInForwDatagrams=aristaSwFwdIpStatsHCInForwDatagrams, aristaSwFwdIpStatsReasmReqds=aristaSwFwdIpStatsReasmReqds, aristaSwFwdIpStatsReasmOKs=aristaSwFwdIpStatsReasmOKs, aristaSwFwdIpStatsReasmFails=aristaSwFwdIpStatsReasmFails, aristaSwFwdIpStatsInDiscards=aristaSwFwdIpStatsInDiscards, aristaSwFwdIpStatsInDelivers=aristaSwFwdIpStatsInDelivers, aristaSwFwdIpStatsHCInDelivers=aristaSwFwdIpStatsHCInDelivers, aristaSwFwdIpStatsOutRequests=aristaSwFwdIpStatsOutRequests, aristaSwFwdIpStatsHCOutRequests=aristaSwFwdIpStatsHCOutRequests, aristaSwFwdIpStatsOutNoRoutes=aristaSwFwdIpStatsOutNoRoutes, aristaSwFwdIpStatsOutForwDatagrams=aristaSwFwdIpStatsOutForwDatagrams, aristaSwFwdIpStatsHCOutForwDatagrams=aristaSwFwdIpStatsHCOutForwDatagrams, aristaSwFwdIpStatsOutDiscards=aristaSwFwdIpStatsOutDiscards, aristaSwFwdIpStatsOutFragReqds=aristaSwFwdIpStatsOutFragReqds, aristaSwFwdIpStatsOutFragOKs=aristaSwFwdIpStatsOutFragOKs, aristaSwFwdIpStatsOutFragFails=aristaSwFwdIpStatsOutFragFails, aristaSwFwdIpStatsOutFragCreates=aristaSwFwdIpStatsOutFragCreates, aristaSwFwdIpStatsOutTransmits=aristaSwFwdIpStatsOutTransmits, aristaSwFwdIpStatsHCOutTransmits=aristaSwFwdIpStatsHCOutTransmits, aristaSwFwdIpStatsOutOctets=aristaSwFwdIpStatsOutOctets, aristaSwFwdIpStatsHCOutOctets=aristaSwFwdIpStatsHCOutOctets, aristaSwFwdIpStatsInMcastPkts=aristaSwFwdIpStatsInMcastPkts, aristaSwFwdIpStatsHCInMcastPkts=aristaSwFwdIpStatsHCInMcastPkts, aristaSwFwdIpStatsInMcastOctets=aristaSwFwdIpStatsInMcastOctets, aristaSwFwdIpStatsHCInMcastOctets=aristaSwFwdIpStatsHCInMcastOctets, aristaSwFwdIpStatsOutMcastPkts=aristaSwFwdIpStatsOutMcastPkts, aristaSwFwdIpStatsHCOutMcastPkts=aristaSwFwdIpStatsHCOutMcastPkts, aristaSwFwdIpStatsOutMcastOctets=aristaSwFwdIpStatsOutMcastOctets, aristaSwFwdIpStatsHCOutMcastOctets=aristaSwFwdIpStatsHCOutMcastOctets, aristaSwFwdIpStatsInBcastPkts=aristaSwFwdIpStatsInBcastPkts, aristaSwFwdIpStatsHCInBcastPkts=aristaSwFwdIpStatsHCInBcastPkts, aristaSwFwdIpStatsOutBcastPkts=aristaSwFwdIpStatsOutBcastPkts, aristaSwFwdIpStatsHCOutBcastPkts=aristaSwFwdIpStatsHCOutBcastPkts, aristaSwFwdIpStatsDiscontinuityTime=aristaSwFwdIpStatsDiscontinuityTime, aristaSwFwdIpStatsRefreshRate=aristaSwFwdIpStatsRefreshRate, aristaSwIpFwdMIBConformance=aristaSwIpFwdMIBConformance, aristaSwIpFwdMIBCompliances=aristaSwIpFwdMIBCompliances, aristaSwIpFwdMIBGroups=aristaSwIpFwdMIBGroups)

# Groups
mibBuilder.exportSymbols("ARISTA-SW-IP-FORWARDING-MIB", aristaSwFwdIpStatsGroup=aristaSwFwdIpStatsGroup, aristaSwFwdIpOctetGroup=aristaSwFwdIpOctetGroup)

# Compliances
mibBuilder.exportSymbols("ARISTA-SW-IP-FORWARDING-MIB", aristaSwIpFwdMIBCompliance=aristaSwIpFwdMIBCompliance)

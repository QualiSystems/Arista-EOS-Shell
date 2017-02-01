# PySNMP SMI module. Autogenerated from smidump -f python ARISTA-TEST-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jan 31 10:06:37 2017,
# Python version sys.version_info(major=2, minor=7, micro=6, releaselevel='final', serial=0)

# Imports

( aristaMibs, ) = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ZeroBasedCounter32, ) = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

aristaTestMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 3)).setRevisions(("2014-08-15 00:00","2011-03-31 13:00","2010-12-01 00:00",))
if mibBuilder.loadTexts: aristaTestMIB.setOrganization("Arista Networks, Inc.")
if mibBuilder.loadTexts: aristaTestMIB.setContactInfo("Arista Networks, Inc.\n\nPostal: 5453 Great America Parkway\n        Santa Clara, CA 9505\n\nTel: +1 408 547-5500\n\nE-mail: snmp@arista.com")
if mibBuilder.loadTexts: aristaTestMIB.setDescription("Arista Test MIB.")
aristaTestNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0))
aristaTestNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0))
aristaTestObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1))
aristaTestNotificationCounter = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 1), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaTestNotificationCounter.setDescription("Notifications counter - the number of times this notification has been sent.")
aristaTestNotificationComment = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaTestNotificationComment.setDescription("Notification comment specified by the user executing the test command.")
aristaTestConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2))
aristaTestCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1))
aristaTestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2))

# Augmentions

# Notifications

aristaTestNotification = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0, 1)).setObjects(*(("ARISTA-TEST-MIB", "aristaTestNotificationComment"), ("ARISTA-TEST-MIB", "aristaTestNotificationCounter"), ) )
if mibBuilder.loadTexts: aristaTestNotification.setDescription("Arista test notification. This notification is triggered whenever the user executes the -test snmp notification- Cli command.")

# Groups

aristaTestObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 1)).setObjects(*(("ARISTA-TEST-MIB", "aristaTestNotificationComment"), ("ARISTA-TEST-MIB", "aristaTestNotificationCounter"), ) )
if mibBuilder.loadTexts: aristaTestObjectsGroup.setDescription("The collection of objects in the ARISTA TEST MIB.")
aristaTestNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 2)).setObjects(*(("ARISTA-TEST-MIB", "aristaTestNotification"), ) )
if mibBuilder.loadTexts: aristaTestNotificationsGroup.setDescription("The collection of notifications in the ARISTA TEST MIB.")

# Compliances

aristaTestCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1, 1)).setObjects(*(("ARISTA-TEST-MIB", "aristaTestNotificationsGroup"), ("ARISTA-TEST-MIB", "aristaTestObjectsGroup"), ) )
if mibBuilder.loadTexts: aristaTestCompliance.setDescription("The compliance statement for SNMP entities which implement\nthe ARISTA TEST MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("ARISTA-TEST-MIB", PYSNMP_MODULE_ID=aristaTestMIB)

# Objects
mibBuilder.exportSymbols("ARISTA-TEST-MIB", aristaTestMIB=aristaTestMIB, aristaTestNotifications=aristaTestNotifications, aristaTestNotificationPrefix=aristaTestNotificationPrefix, aristaTestObjects=aristaTestObjects, aristaTestNotificationCounter=aristaTestNotificationCounter, aristaTestNotificationComment=aristaTestNotificationComment, aristaTestConformance=aristaTestConformance, aristaTestCompliances=aristaTestCompliances, aristaTestGroups=aristaTestGroups)

# Notifications
mibBuilder.exportSymbols("ARISTA-TEST-MIB", aristaTestNotification=aristaTestNotification)

# Groups
mibBuilder.exportSymbols("ARISTA-TEST-MIB", aristaTestObjectsGroup=aristaTestObjectsGroup, aristaTestNotificationsGroup=aristaTestNotificationsGroup)

# Compliances
mibBuilder.exportSymbols("ARISTA-TEST-MIB", aristaTestCompliance=aristaTestCompliance)

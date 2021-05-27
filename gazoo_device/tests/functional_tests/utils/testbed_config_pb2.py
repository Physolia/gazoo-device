# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: testbed_config.proto
# pylint: skip-file
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='testbed_config.proto',
  package='gazootest',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14testbed_config.proto\x12\tgazootest\"\xda\x02\n\rTestbedConfig\x12\"\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x11.gazootest.Device\x12\x0e\n\x06groups\x18\x02 \x03(\t\x12G\n\x10\x65xtra_dimensions\x18\x03 \x03(\x0b\x32-.gazootest.TestbedConfig.ExtraDimensionsEntry\x12K\n\x12testing_properties\x18\x04 \x03(\x0b\x32/.gazootest.TestbedConfig.TestingPropertiesEntry\x12\r\n\x05owner\x18\x05 \x01(\t\x1a\x36\n\x14\x45xtraDimensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16TestingPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd9\x02\n\x06\x44\x65vice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12M\n\x17\x64\x65vice_extra_dimensions\x18\x04 \x03(\x0b\x32,.gazootest.Device.DeviceExtraDimensionsEntry\x12Q\n\x19\x64\x65vice_testing_properties\x18\x05 \x03(\x0b\x32..gazootest.Device.DeviceTestingPropertiesEntry\x1a<\n\x1a\x44\x65viceExtraDimensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a>\n\x1c\x44\x65viceTestingPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3'
)




_TESTBEDCONFIG_EXTRADIMENSIONSENTRY = _descriptor.Descriptor(
  name='ExtraDimensionsEntry',
  full_name='gazootest.TestbedConfig.ExtraDimensionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gazootest.TestbedConfig.ExtraDimensionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='gazootest.TestbedConfig.ExtraDimensionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=324,
)

_TESTBEDCONFIG_TESTINGPROPERTIESENTRY = _descriptor.Descriptor(
  name='TestingPropertiesEntry',
  full_name='gazootest.TestbedConfig.TestingPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gazootest.TestbedConfig.TestingPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='gazootest.TestbedConfig.TestingPropertiesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=382,
)

_TESTBEDCONFIG = _descriptor.Descriptor(
  name='TestbedConfig',
  full_name='gazootest.TestbedConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='devices', full_name='gazootest.TestbedConfig.devices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groups', full_name='gazootest.TestbedConfig.groups', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_dimensions', full_name='gazootest.TestbedConfig.extra_dimensions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='testing_properties', full_name='gazootest.TestbedConfig.testing_properties', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='gazootest.TestbedConfig.owner', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TESTBEDCONFIG_EXTRADIMENSIONSENTRY, _TESTBEDCONFIG_TESTINGPROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=382,
)


_DEVICE_DEVICEEXTRADIMENSIONSENTRY = _descriptor.Descriptor(
  name='DeviceExtraDimensionsEntry',
  full_name='gazootest.Device.DeviceExtraDimensionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gazootest.Device.DeviceExtraDimensionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='gazootest.Device.DeviceExtraDimensionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=666,
)

_DEVICE_DEVICETESTINGPROPERTIESENTRY = _descriptor.Descriptor(
  name='DeviceTestingPropertiesEntry',
  full_name='gazootest.Device.DeviceTestingPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gazootest.Device.DeviceTestingPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='gazootest.Device.DeviceTestingPropertiesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=668,
  serialized_end=730,
)

_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='gazootest.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gazootest.Device.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='gazootest.Device.device_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='gazootest.Device.tags', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_extra_dimensions', full_name='gazootest.Device.device_extra_dimensions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_testing_properties', full_name='gazootest.Device.device_testing_properties', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DEVICE_DEVICEEXTRADIMENSIONSENTRY, _DEVICE_DEVICETESTINGPROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=730,
)

_TESTBEDCONFIG_EXTRADIMENSIONSENTRY.containing_type = _TESTBEDCONFIG
_TESTBEDCONFIG_TESTINGPROPERTIESENTRY.containing_type = _TESTBEDCONFIG
_TESTBEDCONFIG.fields_by_name['devices'].message_type = _DEVICE
_TESTBEDCONFIG.fields_by_name['extra_dimensions'].message_type = _TESTBEDCONFIG_EXTRADIMENSIONSENTRY
_TESTBEDCONFIG.fields_by_name['testing_properties'].message_type = _TESTBEDCONFIG_TESTINGPROPERTIESENTRY
_DEVICE_DEVICEEXTRADIMENSIONSENTRY.containing_type = _DEVICE
_DEVICE_DEVICETESTINGPROPERTIESENTRY.containing_type = _DEVICE
_DEVICE.fields_by_name['device_extra_dimensions'].message_type = _DEVICE_DEVICEEXTRADIMENSIONSENTRY
_DEVICE.fields_by_name['device_testing_properties'].message_type = _DEVICE_DEVICETESTINGPROPERTIESENTRY
DESCRIPTOR.message_types_by_name['TestbedConfig'] = _TESTBEDCONFIG
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestbedConfig = _reflection.GeneratedProtocolMessageType('TestbedConfig', (_message.Message,), {

  'ExtraDimensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtraDimensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TESTBEDCONFIG_EXTRADIMENSIONSENTRY,
    '__module__' : 'testbed_config_pb2'
    # @@protoc_insertion_point(class_scope:gazootest.TestbedConfig.ExtraDimensionsEntry)
    })
  ,

  'TestingPropertiesEntry' : _reflection.GeneratedProtocolMessageType('TestingPropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _TESTBEDCONFIG_TESTINGPROPERTIESENTRY,
    '__module__' : 'testbed_config_pb2'
    # @@protoc_insertion_point(class_scope:gazootest.TestbedConfig.TestingPropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _TESTBEDCONFIG,
  '__module__' : 'testbed_config_pb2'
  # @@protoc_insertion_point(class_scope:gazootest.TestbedConfig)
  })
_sym_db.RegisterMessage(TestbedConfig)
_sym_db.RegisterMessage(TestbedConfig.ExtraDimensionsEntry)
_sym_db.RegisterMessage(TestbedConfig.TestingPropertiesEntry)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {

  'DeviceExtraDimensionsEntry' : _reflection.GeneratedProtocolMessageType('DeviceExtraDimensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DEVICE_DEVICEEXTRADIMENSIONSENTRY,
    '__module__' : 'testbed_config_pb2'
    # @@protoc_insertion_point(class_scope:gazootest.Device.DeviceExtraDimensionsEntry)
    })
  ,

  'DeviceTestingPropertiesEntry' : _reflection.GeneratedProtocolMessageType('DeviceTestingPropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _DEVICE_DEVICETESTINGPROPERTIESENTRY,
    '__module__' : 'testbed_config_pb2'
    # @@protoc_insertion_point(class_scope:gazootest.Device.DeviceTestingPropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'testbed_config_pb2'
  # @@protoc_insertion_point(class_scope:gazootest.Device)
  })
_sym_db.RegisterMessage(Device)
_sym_db.RegisterMessage(Device.DeviceExtraDimensionsEntry)
_sym_db.RegisterMessage(Device.DeviceTestingPropertiesEntry)


_TESTBEDCONFIG_EXTRADIMENSIONSENTRY._options = None
_TESTBEDCONFIG_TESTINGPROPERTIESENTRY._options = None
_DEVICE_DEVICEEXTRADIMENSIONSENTRY._options = None
_DEVICE_DEVICETESTINGPROPERTIESENTRY._options = None
# @@protoc_insertion_point(module_scope)

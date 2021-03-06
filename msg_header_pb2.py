# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg-header.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg-header.proto',
  package='lucid.msg',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10msg-header.proto\x12\tlucid.msg\"i\n\rMessageHeader\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12\x12\n\npayloadVer\x18\x02 \x01(\r\x12\x10\n\x08\x61rxmlVer\x18\x03 \x01(\r\x12\x0b\n\x03seq\x18\x04 \x01(\r\x12\x0c\n\x04vlan\x18\x05 \x01(\r\x12\n\n\x02ts\x18\x06 \x01(\x04\x62\x06proto3'
)




_MESSAGEHEADER = _descriptor.Descriptor(
  name='MessageHeader',
  full_name='lucid.msg.MessageHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vin', full_name='lucid.msg.MessageHeader.vin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payloadVer', full_name='lucid.msg.MessageHeader.payloadVer', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arxmlVer', full_name='lucid.msg.MessageHeader.arxmlVer', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seq', full_name='lucid.msg.MessageHeader.seq', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vlan', full_name='lucid.msg.MessageHeader.vlan', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ts', full_name='lucid.msg.MessageHeader.ts', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['MessageHeader'] = _MESSAGEHEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageHeader = _reflection.GeneratedProtocolMessageType('MessageHeader', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEHEADER,
  '__module__' : 'msg_header_pb2'
  # @@protoc_insertion_point(class_scope:lucid.msg.MessageHeader)
  })
_sym_db.RegisterMessage(MessageHeader)


# @@protoc_insertion_point(module_scope)

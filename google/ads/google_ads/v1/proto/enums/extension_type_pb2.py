# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/extension_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/enums/extension_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\022ExtensionTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\n8google/ads/googleads_v1/proto/enums/extension_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xec\x01\n\x11\x45xtensionTypeEnum\"\xd6\x01\n\rExtensionType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x08\n\x04NONE\x10\x02\x12\x07\n\x03\x41PP\x10\x03\x12\x08\n\x04\x43\x41LL\x10\x04\x12\x0b\n\x07\x43\x41LLOUT\x10\x05\x12\x0b\n\x07MESSAGE\x10\x06\x12\t\n\x05PRICE\x10\x07\x12\r\n\tPROMOTION\x10\x08\x12\n\n\x06REVIEW\x10\t\x12\x0c\n\x08SITELINK\x10\n\x12\x16\n\x12STRUCTURED_SNIPPET\x10\x0b\x12\x0c\n\x08LOCATION\x10\x0c\x12\x16\n\x12\x41\x46\x46ILIATE_LOCATION\x10\rB\xe7\x01\n!com.google.ads.googleads.v1.enumsB\x12\x45xtensionTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_EXTENSIONTYPEENUM_EXTENSIONTYPE = _descriptor.EnumDescriptor(
  name='ExtensionType',
  full_name='google.ads.googleads.v1.enums.ExtensionTypeEnum.ExtensionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALLOUT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVIEW', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SITELINK', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRUCTURED_SNIPPET', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AFFILIATE_LOCATION', index=13, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=144,
  serialized_end=358,
)
_sym_db.RegisterEnumDescriptor(_EXTENSIONTYPEENUM_EXTENSIONTYPE)


_EXTENSIONTYPEENUM = _descriptor.Descriptor(
  name='ExtensionTypeEnum',
  full_name='google.ads.googleads.v1.enums.ExtensionTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTENSIONTYPEENUM_EXTENSIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=358,
)

_EXTENSIONTYPEENUM_EXTENSIONTYPE.containing_type = _EXTENSIONTYPEENUM
DESCRIPTOR.message_types_by_name['ExtensionTypeEnum'] = _EXTENSIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtensionTypeEnum = _reflection.GeneratedProtocolMessageType('ExtensionTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _EXTENSIONTYPEENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.extension_type_pb2'
  ,
  __doc__ = """Container for enum describing possible data types for an extension in an
  extension setting.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.ExtensionTypeEnum)
  ))
_sym_db.RegisterMessage(ExtensionTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
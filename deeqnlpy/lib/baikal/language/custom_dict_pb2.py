# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: baikal/language/custom_dict.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from baikal.language import dict_common_pb2 as baikal_dot_language_dot_dict__common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='baikal/language/custom_dict.proto',
  package='baikal.language',
  syntax='proto3',
  serialized_options=b'B\034CustomDictionaryServiceProtoP\001Z\037baikal.ai/proto/baikal/language',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!baikal/language/custom_dict.proto\x12\x0f\x62\x61ikal.language\x1a!baikal/language/dict_common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\"\xc9\x02\n\x14\x43ustomDictionaryMeta\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\x12>\n\x06np_set\x18\x02 \x01(\x0b\x32..baikal.language.CustomDictionaryMeta.DictMeta\x12>\n\x06\x63p_set\x18\x03 \x01(\x0b\x32..baikal.language.CustomDictionaryMeta.DictMeta\x12\x44\n\x0c\x63p_caret_set\x18\x04 \x01(\x0b\x32..baikal.language.CustomDictionaryMeta.DictMeta\x1aV\n\x08\x44ictMeta\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.baikal.language.DictType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bitems_count\x18\x03 \x01(\x05\"\xab\x01\n\x10\x43ustomDictionary\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\x12(\n\x06np_set\x18\x02 \x01(\x0b\x32\x18.baikal.language.DictSet\x12(\n\x06\x63p_set\x18\x03 \x01(\x0b\x32\x18.baikal.language.DictSet\x12.\n\x0c\x63p_caret_set\x18\x04 \x01(\x0b\x32\x18.baikal.language.DictSet\"\xc0\x01\n\x13\x43ustomDictionaryMap\x12P\n\x0f\x63ustom_dict_map\x18\x01 \x03(\x0b\x32\x37.baikal.language.CustomDictionaryMap.CustomDictMapEntry\x1aW\n\x12\x43ustomDictMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.baikal.language.CustomDictionary:\x02\x38\x01\"^\n\x1fGetCustomDictionaryListResponse\x12;\n\x0c\x64omain_dicts\x18\x01 \x03(\x0b\x32%.baikal.language.CustomDictionaryMeta\"1\n\x1aGetCustomDictionaryRequest\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\"c\n\x1bGetCustomDictionaryResponse\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\x12/\n\x04\x64ict\x18\x02 \x01(\x0b\x32!.baikal.language.CustomDictionary\"e\n\x1dUpdateCustomDictionaryRequest\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\x12/\n\x04\x64ict\x18\x02 \x01(\x0b\x32!.baikal.language.CustomDictionary\"=\n\x1eUpdateCustomDictionaryResponse\x12\x1b\n\x13updated_domain_name\x18\x01 \x01(\t\"D\n\x1fRemoveCustomDictionariesRequest\x12\x14\n\x0c\x64omain_names\x18\x01 \x03(\t\x12\x0b\n\x03\x61ll\x18\x02 \x01(\x08\"\xc6\x01\n RemoveCustomDictionariesResponse\x12g\n\x14\x64\x65leted_domain_names\x18\x01 \x03(\x0b\x32I.baikal.language.RemoveCustomDictionariesResponse.DeletedDomainNamesEntry\x1a\x39\n\x17\x44\x65letedDomainNamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x32\xb3\x05\n\x17\x43ustomDictionaryService\x12\x8b\x01\n\x17GetCustomDictionaryList\x12\x16.google.protobuf.Empty\x1a\x30.baikal.language.GetCustomDictionaryListResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1b/deeq-nlp/api/v1/customdict:\x01*\x12\xa6\x01\n\x13GetCustomDictionary\x12+.baikal.language.GetCustomDictionaryRequest\x1a,.baikal.language.GetCustomDictionaryResponse\"4\x82\xd3\xe4\x93\x02.\x12)/deeq-nlp/api/v1/customdict/{domain_name}:\x01*\x12\xaf\x01\n\x16UpdateCustomDictionary\x12..baikal.language.UpdateCustomDictionaryRequest\x1a/.baikal.language.UpdateCustomDictionaryResponse\"4\x82\xd3\xe4\x93\x02.\")/deeq-nlp/api/v1/customdict/{domain_name}:\x01*\x12\xae\x01\n\x18RemoveCustomDictionaries\x12\x30.baikal.language.RemoveCustomDictionariesRequest\x1a\x31.baikal.language.RemoveCustomDictionariesResponse\"-\x82\xd3\xe4\x93\x02\'\"\"/deeq-nlp/api/v1/customdict/delete:\x01*BAB\x1c\x43ustomDictionaryServiceProtoP\x01Z\x1f\x62\x61ikal.ai/proto/baikal/languageb\x06proto3'
  ,
  dependencies=[baikal_dot_language_dot_dict__common__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CUSTOMDICTIONARYMETA_DICTMETA = _descriptor.Descriptor(
  name='DictMeta',
  full_name='baikal.language.CustomDictionaryMeta.DictMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='baikal.language.CustomDictionaryMeta.DictMeta.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='baikal.language.CustomDictionaryMeta.DictMeta.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items_count', full_name='baikal.language.CustomDictionaryMeta.DictMeta.items_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=392,
  serialized_end=478,
)

_CUSTOMDICTIONARYMETA = _descriptor.Descriptor(
  name='CustomDictionaryMeta',
  full_name='baikal.language.CustomDictionaryMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_name', full_name='baikal.language.CustomDictionaryMeta.domain_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='np_set', full_name='baikal.language.CustomDictionaryMeta.np_set', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cp_set', full_name='baikal.language.CustomDictionaryMeta.cp_set', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cp_caret_set', full_name='baikal.language.CustomDictionaryMeta.cp_caret_set', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CUSTOMDICTIONARYMETA_DICTMETA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=478,
)


_CUSTOMDICTIONARY = _descriptor.Descriptor(
  name='CustomDictionary',
  full_name='baikal.language.CustomDictionary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_name', full_name='baikal.language.CustomDictionary.domain_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='np_set', full_name='baikal.language.CustomDictionary.np_set', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cp_set', full_name='baikal.language.CustomDictionary.cp_set', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cp_caret_set', full_name='baikal.language.CustomDictionary.cp_caret_set', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=481,
  serialized_end=652,
)


_CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY = _descriptor.Descriptor(
  name='CustomDictMapEntry',
  full_name='baikal.language.CustomDictionaryMap.CustomDictMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='baikal.language.CustomDictionaryMap.CustomDictMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='baikal.language.CustomDictionaryMap.CustomDictMapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=760,
  serialized_end=847,
)

_CUSTOMDICTIONARYMAP = _descriptor.Descriptor(
  name='CustomDictionaryMap',
  full_name='baikal.language.CustomDictionaryMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='custom_dict_map', full_name='baikal.language.CustomDictionaryMap.custom_dict_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=655,
  serialized_end=847,
)


_GETCUSTOMDICTIONARYLISTRESPONSE = _descriptor.Descriptor(
  name='GetCustomDictionaryListResponse',
  full_name='baikal.language.GetCustomDictionaryListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_dicts', full_name='baikal.language.GetCustomDictionaryListResponse.domain_dicts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=849,
  serialized_end=943,
)


_GETCUSTOMDICTIONARYREQUEST = _descriptor.Descriptor(
  name='GetCustomDictionaryRequest',
  full_name='baikal.language.GetCustomDictionaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_name', full_name='baikal.language.GetCustomDictionaryRequest.domain_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=945,
  serialized_end=994,
)


_GETCUSTOMDICTIONARYRESPONSE = _descriptor.Descriptor(
  name='GetCustomDictionaryResponse',
  full_name='baikal.language.GetCustomDictionaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_name', full_name='baikal.language.GetCustomDictionaryResponse.domain_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dict', full_name='baikal.language.GetCustomDictionaryResponse.dict', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=996,
  serialized_end=1095,
)


_UPDATECUSTOMDICTIONARYREQUEST = _descriptor.Descriptor(
  name='UpdateCustomDictionaryRequest',
  full_name='baikal.language.UpdateCustomDictionaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_name', full_name='baikal.language.UpdateCustomDictionaryRequest.domain_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dict', full_name='baikal.language.UpdateCustomDictionaryRequest.dict', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1097,
  serialized_end=1198,
)


_UPDATECUSTOMDICTIONARYRESPONSE = _descriptor.Descriptor(
  name='UpdateCustomDictionaryResponse',
  full_name='baikal.language.UpdateCustomDictionaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='updated_domain_name', full_name='baikal.language.UpdateCustomDictionaryResponse.updated_domain_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1200,
  serialized_end=1261,
)


_REMOVECUSTOMDICTIONARIESREQUEST = _descriptor.Descriptor(
  name='RemoveCustomDictionariesRequest',
  full_name='baikal.language.RemoveCustomDictionariesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_names', full_name='baikal.language.RemoveCustomDictionariesRequest.domain_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='all', full_name='baikal.language.RemoveCustomDictionariesRequest.all', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1263,
  serialized_end=1331,
)


_REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY = _descriptor.Descriptor(
  name='DeletedDomainNamesEntry',
  full_name='baikal.language.RemoveCustomDictionariesResponse.DeletedDomainNamesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='baikal.language.RemoveCustomDictionariesResponse.DeletedDomainNamesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='baikal.language.RemoveCustomDictionariesResponse.DeletedDomainNamesEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1475,
  serialized_end=1532,
)

_REMOVECUSTOMDICTIONARIESRESPONSE = _descriptor.Descriptor(
  name='RemoveCustomDictionariesResponse',
  full_name='baikal.language.RemoveCustomDictionariesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deleted_domain_names', full_name='baikal.language.RemoveCustomDictionariesResponse.deleted_domain_names', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1334,
  serialized_end=1532,
)

_CUSTOMDICTIONARYMETA_DICTMETA.fields_by_name['type'].enum_type = baikal_dot_language_dot_dict__common__pb2._DICTTYPE
_CUSTOMDICTIONARYMETA_DICTMETA.containing_type = _CUSTOMDICTIONARYMETA
_CUSTOMDICTIONARYMETA.fields_by_name['np_set'].message_type = _CUSTOMDICTIONARYMETA_DICTMETA
_CUSTOMDICTIONARYMETA.fields_by_name['cp_set'].message_type = _CUSTOMDICTIONARYMETA_DICTMETA
_CUSTOMDICTIONARYMETA.fields_by_name['cp_caret_set'].message_type = _CUSTOMDICTIONARYMETA_DICTMETA
_CUSTOMDICTIONARY.fields_by_name['np_set'].message_type = baikal_dot_language_dot_dict__common__pb2._DICTSET
_CUSTOMDICTIONARY.fields_by_name['cp_set'].message_type = baikal_dot_language_dot_dict__common__pb2._DICTSET
_CUSTOMDICTIONARY.fields_by_name['cp_caret_set'].message_type = baikal_dot_language_dot_dict__common__pb2._DICTSET
_CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY.fields_by_name['value'].message_type = _CUSTOMDICTIONARY
_CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY.containing_type = _CUSTOMDICTIONARYMAP
_CUSTOMDICTIONARYMAP.fields_by_name['custom_dict_map'].message_type = _CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY
_GETCUSTOMDICTIONARYLISTRESPONSE.fields_by_name['domain_dicts'].message_type = _CUSTOMDICTIONARYMETA
_GETCUSTOMDICTIONARYRESPONSE.fields_by_name['dict'].message_type = _CUSTOMDICTIONARY
_UPDATECUSTOMDICTIONARYREQUEST.fields_by_name['dict'].message_type = _CUSTOMDICTIONARY
_REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY.containing_type = _REMOVECUSTOMDICTIONARIESRESPONSE
_REMOVECUSTOMDICTIONARIESRESPONSE.fields_by_name['deleted_domain_names'].message_type = _REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY
DESCRIPTOR.message_types_by_name['CustomDictionaryMeta'] = _CUSTOMDICTIONARYMETA
DESCRIPTOR.message_types_by_name['CustomDictionary'] = _CUSTOMDICTIONARY
DESCRIPTOR.message_types_by_name['CustomDictionaryMap'] = _CUSTOMDICTIONARYMAP
DESCRIPTOR.message_types_by_name['GetCustomDictionaryListResponse'] = _GETCUSTOMDICTIONARYLISTRESPONSE
DESCRIPTOR.message_types_by_name['GetCustomDictionaryRequest'] = _GETCUSTOMDICTIONARYREQUEST
DESCRIPTOR.message_types_by_name['GetCustomDictionaryResponse'] = _GETCUSTOMDICTIONARYRESPONSE
DESCRIPTOR.message_types_by_name['UpdateCustomDictionaryRequest'] = _UPDATECUSTOMDICTIONARYREQUEST
DESCRIPTOR.message_types_by_name['UpdateCustomDictionaryResponse'] = _UPDATECUSTOMDICTIONARYRESPONSE
DESCRIPTOR.message_types_by_name['RemoveCustomDictionariesRequest'] = _REMOVECUSTOMDICTIONARIESREQUEST
DESCRIPTOR.message_types_by_name['RemoveCustomDictionariesResponse'] = _REMOVECUSTOMDICTIONARIESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomDictionaryMeta = _reflection.GeneratedProtocolMessageType('CustomDictionaryMeta', (_message.Message,), {

  'DictMeta' : _reflection.GeneratedProtocolMessageType('DictMeta', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMDICTIONARYMETA_DICTMETA,
    '__module__' : 'baikal.language.custom_dict_pb2'
    # @@protoc_insertion_point(class_scope:baikal.language.CustomDictionaryMeta.DictMeta)
    })
  ,
  'DESCRIPTOR' : _CUSTOMDICTIONARYMETA,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.CustomDictionaryMeta)
  })
_sym_db.RegisterMessage(CustomDictionaryMeta)
_sym_db.RegisterMessage(CustomDictionaryMeta.DictMeta)

CustomDictionary = _reflection.GeneratedProtocolMessageType('CustomDictionary', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMDICTIONARY,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.CustomDictionary)
  })
_sym_db.RegisterMessage(CustomDictionary)

CustomDictionaryMap = _reflection.GeneratedProtocolMessageType('CustomDictionaryMap', (_message.Message,), {

  'CustomDictMapEntry' : _reflection.GeneratedProtocolMessageType('CustomDictMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY,
    '__module__' : 'baikal.language.custom_dict_pb2'
    # @@protoc_insertion_point(class_scope:baikal.language.CustomDictionaryMap.CustomDictMapEntry)
    })
  ,
  'DESCRIPTOR' : _CUSTOMDICTIONARYMAP,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.CustomDictionaryMap)
  })
_sym_db.RegisterMessage(CustomDictionaryMap)
_sym_db.RegisterMessage(CustomDictionaryMap.CustomDictMapEntry)

GetCustomDictionaryListResponse = _reflection.GeneratedProtocolMessageType('GetCustomDictionaryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMDICTIONARYLISTRESPONSE,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.GetCustomDictionaryListResponse)
  })
_sym_db.RegisterMessage(GetCustomDictionaryListResponse)

GetCustomDictionaryRequest = _reflection.GeneratedProtocolMessageType('GetCustomDictionaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMDICTIONARYREQUEST,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.GetCustomDictionaryRequest)
  })
_sym_db.RegisterMessage(GetCustomDictionaryRequest)

GetCustomDictionaryResponse = _reflection.GeneratedProtocolMessageType('GetCustomDictionaryResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMDICTIONARYRESPONSE,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.GetCustomDictionaryResponse)
  })
_sym_db.RegisterMessage(GetCustomDictionaryResponse)

UpdateCustomDictionaryRequest = _reflection.GeneratedProtocolMessageType('UpdateCustomDictionaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECUSTOMDICTIONARYREQUEST,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.UpdateCustomDictionaryRequest)
  })
_sym_db.RegisterMessage(UpdateCustomDictionaryRequest)

UpdateCustomDictionaryResponse = _reflection.GeneratedProtocolMessageType('UpdateCustomDictionaryResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECUSTOMDICTIONARYRESPONSE,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.UpdateCustomDictionaryResponse)
  })
_sym_db.RegisterMessage(UpdateCustomDictionaryResponse)

RemoveCustomDictionariesRequest = _reflection.GeneratedProtocolMessageType('RemoveCustomDictionariesRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVECUSTOMDICTIONARIESREQUEST,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.RemoveCustomDictionariesRequest)
  })
_sym_db.RegisterMessage(RemoveCustomDictionariesRequest)

RemoveCustomDictionariesResponse = _reflection.GeneratedProtocolMessageType('RemoveCustomDictionariesResponse', (_message.Message,), {

  'DeletedDomainNamesEntry' : _reflection.GeneratedProtocolMessageType('DeletedDomainNamesEntry', (_message.Message,), {
    'DESCRIPTOR' : _REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY,
    '__module__' : 'baikal.language.custom_dict_pb2'
    # @@protoc_insertion_point(class_scope:baikal.language.RemoveCustomDictionariesResponse.DeletedDomainNamesEntry)
    })
  ,
  'DESCRIPTOR' : _REMOVECUSTOMDICTIONARIESRESPONSE,
  '__module__' : 'baikal.language.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.RemoveCustomDictionariesResponse)
  })
_sym_db.RegisterMessage(RemoveCustomDictionariesResponse)
_sym_db.RegisterMessage(RemoveCustomDictionariesResponse.DeletedDomainNamesEntry)


DESCRIPTOR._options = None
_CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY._options = None
_REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY._options = None

_CUSTOMDICTIONARYSERVICE = _descriptor.ServiceDescriptor(
  name='CustomDictionaryService',
  full_name='baikal.language.CustomDictionaryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1535,
  serialized_end=2226,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomDictionaryList',
    full_name='baikal.language.CustomDictionaryService.GetCustomDictionaryList',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_GETCUSTOMDICTIONARYLISTRESPONSE,
    serialized_options=b'\202\323\344\223\002 \022\033/deeq-nlp/api/v1/customdict:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetCustomDictionary',
    full_name='baikal.language.CustomDictionaryService.GetCustomDictionary',
    index=1,
    containing_service=None,
    input_type=_GETCUSTOMDICTIONARYREQUEST,
    output_type=_GETCUSTOMDICTIONARYRESPONSE,
    serialized_options=b'\202\323\344\223\002.\022)/deeq-nlp/api/v1/customdict/{domain_name}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateCustomDictionary',
    full_name='baikal.language.CustomDictionaryService.UpdateCustomDictionary',
    index=2,
    containing_service=None,
    input_type=_UPDATECUSTOMDICTIONARYREQUEST,
    output_type=_UPDATECUSTOMDICTIONARYRESPONSE,
    serialized_options=b'\202\323\344\223\002.\")/deeq-nlp/api/v1/customdict/{domain_name}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveCustomDictionaries',
    full_name='baikal.language.CustomDictionaryService.RemoveCustomDictionaries',
    index=3,
    containing_service=None,
    input_type=_REMOVECUSTOMDICTIONARIESREQUEST,
    output_type=_REMOVECUSTOMDICTIONARIESRESPONSE,
    serialized_options=b'\202\323\344\223\002\'\"\"/deeq-nlp/api/v1/customdict/delete:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMDICTIONARYSERVICE)

DESCRIPTOR.services_by_name['CustomDictionaryService'] = _CUSTOMDICTIONARYSERVICE

# @@protoc_insertion_point(module_scope)

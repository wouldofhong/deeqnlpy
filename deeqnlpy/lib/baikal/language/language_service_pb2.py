# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: baikal/language/language_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='baikal/language/language_service.proto',
  package='baikal.language',
  syntax='proto3',
  serialized_options=b'B\024LanguageServiceProtoP\001Z\037baikal.ai/proto/baikal/language',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&baikal/language/language_service.proto\x12\x0f\x62\x61ikal.language\x1a\x1cgoogle/api/annotations.proto\"-\n\x08\x44ocument\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x04 \x01(\t\"[\n\x08Sentence\x12\'\n\x04text\x18\x01 \x01(\x0b\x32\x19.baikal.language.TextSpan\x12&\n\x06tokens\x18\x02 \x03(\x0b\x32\x16.baikal.language.Token\"\xc8\x05\n\x08Morpheme\x12\'\n\x04text\x18\x01 \x01(\x0b\x32\x19.baikal.language.TextSpan\x12*\n\x03tag\x18\x02 \x01(\x0e\x32\x1d.baikal.language.Morpheme.Tag\x12\x13\n\x0bprobability\x18\x03 \x01(\x02\x12\x16\n\x0e\x64isambiguation\x18\x04 \x01(\x05\x12:\n\x0cout_of_vocab\x18\x05 \x01(\x0e\x32$.baikal.language.Morpheme.OutOfVocab\"^\n\nOutOfVocab\x12\x15\n\x11IN_WORD_EMBEDDING\x10\x00\x12\x10\n\x0cOUT_OF_VOCAB\x10\x01\x12\x12\n\x0eIN_CUSTOM_DICT\x10\x02\x12\x13\n\x0fIN_BUILTIN_DICT\x10\x03\"\x9d\x03\n\x03Tag\x12\x07\n\x03UNK\x10\x00\x12\x07\n\x03NNG\x10\x18\x12\x07\n\x03NNP\x10\x19\x12\x07\n\x03NNB\x10\x17\x12\x06\n\x02NF\x10\x16\x12\x06\n\x02NR\x10\x1b\x12\x06\n\x02NP\x10\x1a\x12\x06\n\x02VV\x10)\x12\x06\n\x02VA\x10&\x12\x06\n\x02VX\x10*\x12\x07\n\x03VCP\x10(\x12\x07\n\x03VCN\x10\'\x12\x07\n\x03MMA\x10\x12\x12\x07\n\x03MMD\x10\x13\x12\x07\n\x03MMN\x10\x14\x12\x07\n\x03MAG\x10\x10\x12\x07\n\x03MAJ\x10\x11\x12\x06\n\x02IC\x10\x06\x12\x07\n\x03JKS\x10\r\x12\x07\n\x03JKC\x10\t\x12\x07\n\x03JKG\x10\n\x12\x07\n\x03JKO\x10\x0b\x12\x07\n\x03JKB\x10\x08\x12\x07\n\x03JKV\x10\x0e\x12\x07\n\x03JKQ\x10\x0c\x12\x06\n\x02JX\x10\x0f\x12\x06\n\x02JC\x10\x07\x12\x06\n\x02\x45P\x10\x03\x12\x06\n\x02\x45\x46\x10\x02\x12\x06\n\x02\x45\x43\x10\x01\x12\x07\n\x03\x45TN\x10\x05\x12\x07\n\x03\x45TM\x10\x04\x12\x07\n\x03XPN\x10+\x12\x07\n\x03XSN\x10.\x12\x07\n\x03XSV\x10/\x12\x07\n\x03XSA\x10-\x12\x06\n\x02XR\x10,\x12\x06\n\x02SF\x10\x1e\x12\x06\n\x02SP\x10#\x12\x06\n\x02SS\x10$\x12\x06\n\x02SE\x10\x1d\x12\x06\n\x02SO\x10\"\x12\x06\n\x02SW\x10%\x12\x06\n\x02NA\x10\x15\x12\x06\n\x02SL\x10 \x12\x06\n\x02SH\x10\x1f\x12\x06\n\x02SN\x10!\x12\x06\n\x02NV\x10\x1c\"}\n\x05Token\x12\'\n\x04text\x18\x01 \x01(\x0b\x32\x19.baikal.language.TextSpan\x12,\n\tmorphemes\x18\x02 \x03(\x0b\x32\x19.baikal.language.Morpheme\x12\r\n\x05lemma\x18\x04 \x01(\t\x12\x0e\n\x06tagged\x18\x05 \x01(\t\"1\n\x08TextSpan\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x14\n\x0c\x62\x65gin_offset\x18\x02 \x01(\x05\"\xad\x01\n\x14\x41nalyzeSyntaxRequest\x12+\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\x19.baikal.language.Document\x12\x34\n\rencoding_type\x18\x02 \x01(\x0e\x32\x1d.baikal.language.EncodingType\x12\x1b\n\x13\x61uto_split_sentence\x18\x03 \x01(\x08\x12\x15\n\rcustom_domain\x18\x04 \x01(\t\"W\n\x15\x41nalyzeSyntaxResponse\x12,\n\tsentences\x18\x01 \x03(\x0b\x32\x19.baikal.language.Sentence\x12\x10\n\x08language\x18\x03 \x01(\t*8\n\x0c\x45ncodingType\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04UTF8\x10\x01\x12\t\n\x05UTF16\x10\x02\x12\t\n\x05UTF32\x10\x03\x32\x97\x01\n\x0fLanguageService\x12\x83\x01\n\rAnalyzeSyntax\x12%.baikal.language.AnalyzeSyntaxRequest\x1a&.baikal.language.AnalyzeSyntaxResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/deeq-nlp/api/v1/analyze:\x01*B9B\x14LanguageServiceProtoP\x01Z\x1f\x62\x61ikal.ai/proto/baikal/languageb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_ENCODINGTYPE = _descriptor.EnumDescriptor(
  name='EncodingType',
  full_name='baikal.language.EncodingType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UTF8', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UTF16', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UTF32', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1387,
  serialized_end=1443,
)
_sym_db.RegisterEnumDescriptor(_ENCODINGTYPE)

EncodingType = enum_type_wrapper.EnumTypeWrapper(_ENCODINGTYPE)
NONE = 0
UTF8 = 1
UTF16 = 2
UTF32 = 3


_MORPHEME_OUTOFVOCAB = _descriptor.EnumDescriptor(
  name='OutOfVocab',
  full_name='baikal.language.Morpheme.OutOfVocab',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IN_WORD_EMBEDDING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_VOCAB', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_CUSTOM_DICT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_BUILTIN_DICT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=432,
  serialized_end=526,
)
_sym_db.RegisterEnumDescriptor(_MORPHEME_OUTOFVOCAB)

_MORPHEME_TAG = _descriptor.EnumDescriptor(
  name='Tag',
  full_name='baikal.language.Morpheme.Tag',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NNG', index=1, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NNP', index=2, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NNB', index=3, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NF', index=4, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NR', index=5, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NP', index=6, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VV', index=7, number=41,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VA', index=8, number=38,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VX', index=9, number=42,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VCP', index=10, number=40,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VCN', index=11, number=39,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MMA', index=12, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MMD', index=13, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MMN', index=14, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAG', index=15, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAJ', index=16, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IC', index=17, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JKS', index=18, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JKC', index=19, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JKG', index=20, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JKO', index=21, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JKB', index=22, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JKV', index=23, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JKQ', index=24, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JX', index=25, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JC', index=26, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EP', index=27, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EF', index=28, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EC', index=29, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ETN', index=30, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ETM', index=31, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='XPN', index=32, number=43,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='XSN', index=33, number=46,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='XSV', index=34, number=47,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='XSA', index=35, number=45,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='XR', index=36, number=44,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SF', index=37, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SP', index=38, number=35,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SS', index=39, number=36,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SE', index=40, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SO', index=41, number=34,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SW', index=42, number=37,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NA', index=43, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SL', index=44, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SH', index=45, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SN', index=46, number=33,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NV', index=47, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=529,
  serialized_end=942,
)
_sym_db.RegisterEnumDescriptor(_MORPHEME_TAG)


_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='baikal.language.Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='baikal.language.Document.content', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='baikal.language.Document.language', index=1,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=89,
  serialized_end=134,
)


_SENTENCE = _descriptor.Descriptor(
  name='Sentence',
  full_name='baikal.language.Sentence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='baikal.language.Sentence.text', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokens', full_name='baikal.language.Sentence.tokens', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=136,
  serialized_end=227,
)


_MORPHEME = _descriptor.Descriptor(
  name='Morpheme',
  full_name='baikal.language.Morpheme',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='baikal.language.Morpheme.text', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='baikal.language.Morpheme.tag', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='probability', full_name='baikal.language.Morpheme.probability', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disambiguation', full_name='baikal.language.Morpheme.disambiguation', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='out_of_vocab', full_name='baikal.language.Morpheme.out_of_vocab', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MORPHEME_OUTOFVOCAB,
    _MORPHEME_TAG,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=942,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='baikal.language.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='baikal.language.Token.text', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='morphemes', full_name='baikal.language.Token.morphemes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lemma', full_name='baikal.language.Token.lemma', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tagged', full_name='baikal.language.Token.tagged', index=3,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=944,
  serialized_end=1069,
)


_TEXTSPAN = _descriptor.Descriptor(
  name='TextSpan',
  full_name='baikal.language.TextSpan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='baikal.language.TextSpan.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='begin_offset', full_name='baikal.language.TextSpan.begin_offset', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1071,
  serialized_end=1120,
)


_ANALYZESYNTAXREQUEST = _descriptor.Descriptor(
  name='AnalyzeSyntaxRequest',
  full_name='baikal.language.AnalyzeSyntaxRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='baikal.language.AnalyzeSyntaxRequest.document', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encoding_type', full_name='baikal.language.AnalyzeSyntaxRequest.encoding_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auto_split_sentence', full_name='baikal.language.AnalyzeSyntaxRequest.auto_split_sentence', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_domain', full_name='baikal.language.AnalyzeSyntaxRequest.custom_domain', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1123,
  serialized_end=1296,
)


_ANALYZESYNTAXRESPONSE = _descriptor.Descriptor(
  name='AnalyzeSyntaxResponse',
  full_name='baikal.language.AnalyzeSyntaxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sentences', full_name='baikal.language.AnalyzeSyntaxResponse.sentences', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='baikal.language.AnalyzeSyntaxResponse.language', index=1,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1298,
  serialized_end=1385,
)

_SENTENCE.fields_by_name['text'].message_type = _TEXTSPAN
_SENTENCE.fields_by_name['tokens'].message_type = _TOKEN
_MORPHEME.fields_by_name['text'].message_type = _TEXTSPAN
_MORPHEME.fields_by_name['tag'].enum_type = _MORPHEME_TAG
_MORPHEME.fields_by_name['out_of_vocab'].enum_type = _MORPHEME_OUTOFVOCAB
_MORPHEME_OUTOFVOCAB.containing_type = _MORPHEME
_MORPHEME_TAG.containing_type = _MORPHEME
_TOKEN.fields_by_name['text'].message_type = _TEXTSPAN
_TOKEN.fields_by_name['morphemes'].message_type = _MORPHEME
_ANALYZESYNTAXREQUEST.fields_by_name['document'].message_type = _DOCUMENT
_ANALYZESYNTAXREQUEST.fields_by_name['encoding_type'].enum_type = _ENCODINGTYPE
_ANALYZESYNTAXRESPONSE.fields_by_name['sentences'].message_type = _SENTENCE
DESCRIPTOR.message_types_by_name['Document'] = _DOCUMENT
DESCRIPTOR.message_types_by_name['Sentence'] = _SENTENCE
DESCRIPTOR.message_types_by_name['Morpheme'] = _MORPHEME
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['TextSpan'] = _TEXTSPAN
DESCRIPTOR.message_types_by_name['AnalyzeSyntaxRequest'] = _ANALYZESYNTAXREQUEST
DESCRIPTOR.message_types_by_name['AnalyzeSyntaxResponse'] = _ANALYZESYNTAXRESPONSE
DESCRIPTOR.enum_types_by_name['EncodingType'] = _ENCODINGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'baikal.language.language_service_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.Document)
  })
_sym_db.RegisterMessage(Document)

Sentence = _reflection.GeneratedProtocolMessageType('Sentence', (_message.Message,), {
  'DESCRIPTOR' : _SENTENCE,
  '__module__' : 'baikal.language.language_service_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.Sentence)
  })
_sym_db.RegisterMessage(Sentence)

Morpheme = _reflection.GeneratedProtocolMessageType('Morpheme', (_message.Message,), {
  'DESCRIPTOR' : _MORPHEME,
  '__module__' : 'baikal.language.language_service_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.Morpheme)
  })
_sym_db.RegisterMessage(Morpheme)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'baikal.language.language_service_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.Token)
  })
_sym_db.RegisterMessage(Token)

TextSpan = _reflection.GeneratedProtocolMessageType('TextSpan', (_message.Message,), {
  'DESCRIPTOR' : _TEXTSPAN,
  '__module__' : 'baikal.language.language_service_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.TextSpan)
  })
_sym_db.RegisterMessage(TextSpan)

AnalyzeSyntaxRequest = _reflection.GeneratedProtocolMessageType('AnalyzeSyntaxRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZESYNTAXREQUEST,
  '__module__' : 'baikal.language.language_service_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.AnalyzeSyntaxRequest)
  })
_sym_db.RegisterMessage(AnalyzeSyntaxRequest)

AnalyzeSyntaxResponse = _reflection.GeneratedProtocolMessageType('AnalyzeSyntaxResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZESYNTAXRESPONSE,
  '__module__' : 'baikal.language.language_service_pb2'
  # @@protoc_insertion_point(class_scope:baikal.language.AnalyzeSyntaxResponse)
  })
_sym_db.RegisterMessage(AnalyzeSyntaxResponse)


DESCRIPTOR._options = None

_LANGUAGESERVICE = _descriptor.ServiceDescriptor(
  name='LanguageService',
  full_name='baikal.language.LanguageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1446,
  serialized_end=1597,
  methods=[
  _descriptor.MethodDescriptor(
    name='AnalyzeSyntax',
    full_name='baikal.language.LanguageService.AnalyzeSyntax',
    index=0,
    containing_service=None,
    input_type=_ANALYZESYNTAXREQUEST,
    output_type=_ANALYZESYNTAXRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\"\030/deeq-nlp/api/v1/analyze:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LANGUAGESERVICE)

DESCRIPTOR.services_by_name['LanguageService'] = _LANGUAGESERVICE

# @@protoc_insertion_point(module_scope)

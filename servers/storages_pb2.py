# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0estorages.proto\x12\x07schemas\"8\n\rSchemaRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06vendor\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\"0\n\x06Schema\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06schema\x18\x02 \x01(\tB\x05\n\x03_id\"C\n\x0eSchemaResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12 \n\x07schemas\x18\x02 \x03(\x0b\x32\x0f.schemas.Schema\"M\n\x0cTableRequest\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12 \n\x07schemas\x18\x03 \x03(\x0b\x32\x0f.schemas.Schema\">\n\x05Table\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\tB\x05\n\x03_id\"@\n\rTableResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1e\n\x06tables\x18\x02 \x03(\x0b\x32\x0e.schemas.Table\"L\n\rColumnRequest\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x1e\n\x06tables\x18\x03 \x03(\x0b\x32\x0e.schemas.Table\"\x18\n\x06\x43olumn\x12\x0e\n\x06\x63olumn\x18\x01 \x01(\t\"C\n\x0e\x43olumnResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12 \n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x0f.schemas.Column\"g\n\x0bViewRequest\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0e\n\x06schema\x18\x03 \x01(\t\x12\r\n\x05table\x18\x04 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x05 \x03(\t\x12\x0b\n\x03row\x18\x06 \x01(\x05\"0\n\x0cViewResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07records\x18\x02 \x01(\x0c\"N\n\x10MigrationRequest\x12\x12\n\nsource_uri\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65stination_uri\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\t\"5\n\x11MigrationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xd2\x02\n\x17\x44\x61taSourceManageService\x12=\n\nGetSchemas\x12\x16.schemas.SchemaRequest\x1a\x17.schemas.SchemaResponse\x12:\n\tGetTables\x12\x15.schemas.TableRequest\x1a\x16.schemas.TableResponse\x12=\n\nGetColumns\x12\x16.schemas.ColumnRequest\x1a\x17.schemas.ColumnResponse\x12\x37\n\x08GetViews\x12\x14.schemas.ViewRequest\x1a\x15.schemas.ViewResponse\x12\x44\n\x0b\x44oMigration\x12\x19.schemas.MigrationRequest\x1a\x1a.schemas.MigrationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'storages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SCHEMAREQUEST']._serialized_start=27
  _globals['_SCHEMAREQUEST']._serialized_end=83
  _globals['_SCHEMA']._serialized_start=85
  _globals['_SCHEMA']._serialized_end=133
  _globals['_SCHEMARESPONSE']._serialized_start=135
  _globals['_SCHEMARESPONSE']._serialized_end=202
  _globals['_TABLEREQUEST']._serialized_start=204
  _globals['_TABLEREQUEST']._serialized_end=281
  _globals['_TABLE']._serialized_start=283
  _globals['_TABLE']._serialized_end=345
  _globals['_TABLERESPONSE']._serialized_start=347
  _globals['_TABLERESPONSE']._serialized_end=411
  _globals['_COLUMNREQUEST']._serialized_start=413
  _globals['_COLUMNREQUEST']._serialized_end=489
  _globals['_COLUMN']._serialized_start=491
  _globals['_COLUMN']._serialized_end=515
  _globals['_COLUMNRESPONSE']._serialized_start=517
  _globals['_COLUMNRESPONSE']._serialized_end=584
  _globals['_VIEWREQUEST']._serialized_start=586
  _globals['_VIEWREQUEST']._serialized_end=689
  _globals['_VIEWRESPONSE']._serialized_start=691
  _globals['_VIEWRESPONSE']._serialized_end=739
  _globals['_MIGRATIONREQUEST']._serialized_start=741
  _globals['_MIGRATIONREQUEST']._serialized_end=819
  _globals['_MIGRATIONRESPONSE']._serialized_start=821
  _globals['_MIGRATIONRESPONSE']._serialized_end=874
  _globals['_DATASOURCEMANAGESERVICE']._serialized_start=877
  _globals['_DATASOURCEMANAGESERVICE']._serialized_end=1215
# @@protoc_insertion_point(module_scope)

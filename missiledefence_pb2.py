# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: missiledefence.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14missiledefence.proto\x12\x0emissiledefense\"#\n\rSoldierFilter\x12\x12\n\nsoldier_id\x18\x01 \x01(\x05\"+\n\x0f\x43ommanderStatus\x12\x18\n\x10new_commander_id\x18\x03 \x01(\x05\"(\n\x12NewCommanderFilter\x12\x12\n\nsoldier_id\x18\x01 \x01(\x05\"g\n\x11\x43onnectionRequest\x12\x12\n\nsoldier_id\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x03(\x05\x12\x16\n\x0eno_of_soldiers\x18\x03 \x01(\x05\x12\x14\n\x0cwarzone_size\x18\x04 \x01(\x05\"J\n\x13NewCommanderDetails\x12\x12\n\nsoldier_id\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x03(\x05\x12\r\n\x05speed\x18\x03 \x01(\x05\"\x07\n\x05\x45mpty\"@\n\x06WasHit\x12\x12\n\nsoldier_id\x18\x01 \x01(\x05\x12\x10\n\x08is_alive\x18\x02 \x01(\x08\x12\x10\n\x08position\x18\x03 \x03(\x05\">\n\x0eMissileDetails\x12\x10\n\x08position\x18\x01 \x03(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\t\"\x18\n\tLayoutRow\x12\x0b\n\x03row\x18\x02 \x03(\x05\"p\n\x12MissileApproaching\x12/\n\x07missile\x18\x01 \x01(\x0b\x32\x1e.missiledefense.MissileDetails\x12)\n\x06layout\x18\x02 \x03(\x0b\x32\x19.missiledefense.LayoutRow2\xd9\x02\n\tCommander\x12X\n\rsoldier_ready\x12!.missiledefense.ConnectionRequest\x1a\".missiledefense.NewCommanderFilter\"\x00\x12\\\n\x13missile_approaching\x12\x1d.missiledefense.SoldierFilter\x1a\".missiledefense.MissileApproaching\"\x00\x30\x01\x12\x43\n\x06status\x12\x16.missiledefense.WasHit\x1a\x1f.missiledefense.CommanderStatus\"\x00\x12O\n\x0f\x65lect_commander\x12#.missiledefense.NewCommanderDetails\x1a\x15.missiledefense.Empty\"\x00\x42>\n\x1fio.grpc.examples.MissileDefenceB\x13MissileDefenceProtoP\x01\xa2\x02\x03MDSb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'missiledefence_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037io.grpc.examples.MissileDefenceB\023MissileDefenceProtoP\001\242\002\003MDS'
  _globals['_SOLDIERFILTER']._serialized_start=40
  _globals['_SOLDIERFILTER']._serialized_end=75
  _globals['_COMMANDERSTATUS']._serialized_start=77
  _globals['_COMMANDERSTATUS']._serialized_end=120
  _globals['_NEWCOMMANDERFILTER']._serialized_start=122
  _globals['_NEWCOMMANDERFILTER']._serialized_end=162
  _globals['_CONNECTIONREQUEST']._serialized_start=164
  _globals['_CONNECTIONREQUEST']._serialized_end=267
  _globals['_NEWCOMMANDERDETAILS']._serialized_start=269
  _globals['_NEWCOMMANDERDETAILS']._serialized_end=343
  _globals['_EMPTY']._serialized_start=345
  _globals['_EMPTY']._serialized_end=352
  _globals['_WASHIT']._serialized_start=354
  _globals['_WASHIT']._serialized_end=418
  _globals['_MISSILEDETAILS']._serialized_start=420
  _globals['_MISSILEDETAILS']._serialized_end=482
  _globals['_LAYOUTROW']._serialized_start=484
  _globals['_LAYOUTROW']._serialized_end=508
  _globals['_MISSILEAPPROACHING']._serialized_start=510
  _globals['_MISSILEAPPROACHING']._serialized_end=622
  _globals['_COMMANDER']._serialized_start=625
  _globals['_COMMANDER']._serialized_end=970
# @@protoc_insertion_point(module_scope)

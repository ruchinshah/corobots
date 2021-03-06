"""autogenerated by genpy from corobot_obstacle_avoidance_testing/Wall.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Wall(genpy.Message):
  _md5sum = "b9dcd15249d280cbfabbb015f7ba5fce"
  _type = "corobot_obstacle_avoidance_testing/Wall"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 rleft
float32 thetaleft
int32 conf_left
bool is_wall_left

float32 rright
float32 thetaright
int32 conf_right
bool is_wall_right

uint32 tdiv
uint32 height
int32[] accumulator

"""
  __slots__ = ['rleft','thetaleft','conf_left','is_wall_left','rright','thetaright','conf_right','is_wall_right','tdiv','height','accumulator']
  _slot_types = ['float32','float32','int32','bool','float32','float32','int32','bool','uint32','uint32','int32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       rleft,thetaleft,conf_left,is_wall_left,rright,thetaright,conf_right,is_wall_right,tdiv,height,accumulator

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Wall, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.rleft is None:
        self.rleft = 0.
      if self.thetaleft is None:
        self.thetaleft = 0.
      if self.conf_left is None:
        self.conf_left = 0
      if self.is_wall_left is None:
        self.is_wall_left = False
      if self.rright is None:
        self.rright = 0.
      if self.thetaright is None:
        self.thetaright = 0.
      if self.conf_right is None:
        self.conf_right = 0
      if self.is_wall_right is None:
        self.is_wall_right = False
      if self.tdiv is None:
        self.tdiv = 0
      if self.height is None:
        self.height = 0
      if self.accumulator is None:
        self.accumulator = []
    else:
      self.rleft = 0.
      self.thetaleft = 0.
      self.conf_left = 0
      self.is_wall_left = False
      self.rright = 0.
      self.thetaright = 0.
      self.conf_right = 0
      self.is_wall_right = False
      self.tdiv = 0
      self.height = 0
      self.accumulator = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_2fiB2fiB2I.pack(_x.rleft, _x.thetaleft, _x.conf_left, _x.is_wall_left, _x.rright, _x.thetaright, _x.conf_right, _x.is_wall_right, _x.tdiv, _x.height))
      length = len(self.accumulator)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.accumulator))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 34
      (_x.rleft, _x.thetaleft, _x.conf_left, _x.is_wall_left, _x.rright, _x.thetaright, _x.conf_right, _x.is_wall_right, _x.tdiv, _x.height,) = _struct_2fiB2fiB2I.unpack(str[start:end])
      self.is_wall_left = bool(self.is_wall_left)
      self.is_wall_right = bool(self.is_wall_right)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.accumulator = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_2fiB2fiB2I.pack(_x.rleft, _x.thetaleft, _x.conf_left, _x.is_wall_left, _x.rright, _x.thetaright, _x.conf_right, _x.is_wall_right, _x.tdiv, _x.height))
      length = len(self.accumulator)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.accumulator.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 34
      (_x.rleft, _x.thetaleft, _x.conf_left, _x.is_wall_left, _x.rright, _x.thetaright, _x.conf_right, _x.is_wall_right, _x.tdiv, _x.height,) = _struct_2fiB2fiB2I.unpack(str[start:end])
      self.is_wall_left = bool(self.is_wall_left)
      self.is_wall_right = bool(self.is_wall_right)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.accumulator = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2fiB2fiB2I = struct.Struct("<2fiB2fiB2I")

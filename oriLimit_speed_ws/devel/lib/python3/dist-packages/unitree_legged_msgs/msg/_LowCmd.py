# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from unitree_legged_msgs/LowCmd.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import unitree_legged_msgs.msg

class LowCmd(genpy.Message):
  _md5sum = "e4244bee8bd94ef34a8673aec97e6a88"
  _type = "unitree_legged_msgs/LowCmd"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 levelFlag                 
uint16 commVersion              # Old version Aliengo does not have
uint16 robotID                  # Old version Aliengo does not have
uint32 SN                       # Old version Aliengo does not have
uint8 bandWidth                 # Old version Aliengo does not have
MotorCmd[20] motorCmd
BmsCmd bms                      # new on Go1, battery command
# LED[4] led
uint8[40] wirelessRemote
uint32 reserve                  # Old version Aliengo does not have
uint32 crc

Cartesian[4] ff               # will delete # Old version Aliengo does not have
================================================================================
MSG: unitree_legged_msgs/MotorCmd
uint8 mode           # motor target mode
float32 q            # motor target position
float32 dq           # motor target velocity
float32 tau          # motor target torque
float32 Kp           # motor spring stiffness coefficient
float32 Kd           # motor damper coefficient
uint32[3] reserve    # motor target torque
================================================================================
MSG: unitree_legged_msgs/BmsCmd
uint8 off            # off 0xA5
uint8[3] reserve
================================================================================
MSG: unitree_legged_msgs/Cartesian
float32 x
float32 y
float32 z"""
  __slots__ = ['levelFlag','commVersion','robotID','SN','bandWidth','motorCmd','bms','wirelessRemote','reserve','crc','ff']
  _slot_types = ['uint8','uint16','uint16','uint32','uint8','unitree_legged_msgs/MotorCmd[20]','unitree_legged_msgs/BmsCmd','uint8[40]','uint32','uint32','unitree_legged_msgs/Cartesian[4]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       levelFlag,commVersion,robotID,SN,bandWidth,motorCmd,bms,wirelessRemote,reserve,crc,ff

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LowCmd, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.levelFlag is None:
        self.levelFlag = 0
      if self.commVersion is None:
        self.commVersion = 0
      if self.robotID is None:
        self.robotID = 0
      if self.SN is None:
        self.SN = 0
      if self.bandWidth is None:
        self.bandWidth = 0
      if self.motorCmd is None:
        self.motorCmd = [unitree_legged_msgs.msg.MotorCmd() for _ in range(20)]
      if self.bms is None:
        self.bms = unitree_legged_msgs.msg.BmsCmd()
      if self.wirelessRemote is None:
        self.wirelessRemote = b'\0'*40
      if self.reserve is None:
        self.reserve = 0
      if self.crc is None:
        self.crc = 0
      if self.ff is None:
        self.ff = [unitree_legged_msgs.msg.Cartesian() for _ in range(4)]
    else:
      self.levelFlag = 0
      self.commVersion = 0
      self.robotID = 0
      self.SN = 0
      self.bandWidth = 0
      self.motorCmd = [unitree_legged_msgs.msg.MotorCmd() for _ in range(20)]
      self.bms = unitree_legged_msgs.msg.BmsCmd()
      self.wirelessRemote = b'\0'*40
      self.reserve = 0
      self.crc = 0
      self.ff = [unitree_legged_msgs.msg.Cartesian() for _ in range(4)]

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
      buff.write(_get_struct_B2HIB().pack(_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth))
      if len(self.motorCmd) != 20:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (20, len(self.motorCmd), 'self.motorCmd')))
      for val1 in self.motorCmd:
        _x = val1
        buff.write(_get_struct_B5f().pack(_x.mode, _x.q, _x.dq, _x.tau, _x.Kp, _x.Kd))
        buff.write(_get_struct_3I().pack(*val1.reserve))
      _x = self.bms.off
      buff.write(_get_struct_B().pack(_x))
      _x = self.bms.reserve
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_3B().pack(*_x))
      else:
        buff.write(_get_struct_3s().pack(_x))
      _x = self.wirelessRemote
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_40B().pack(*_x))
      else:
        buff.write(_get_struct_40s().pack(_x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.reserve, _x.crc))
      if len(self.ff) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.ff), 'self.ff')))
      for val1 in self.ff:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.motorCmd is None:
        self.motorCmd = None
      if self.bms is None:
        self.bms = unitree_legged_msgs.msg.BmsCmd()
      if self.ff is None:
        self.ff = None
      end = 0
      _x = self
      start = end
      end += 10
      (_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth,) = _get_struct_B2HIB().unpack(str[start:end])
      self.motorCmd = []
      for i in range(0, 20):
        val1 = unitree_legged_msgs.msg.MotorCmd()
        _x = val1
        start = end
        end += 21
        (_x.mode, _x.q, _x.dq, _x.tau, _x.Kp, _x.Kd,) = _get_struct_B5f().unpack(str[start:end])
        start = end
        end += 12
        val1.reserve = _get_struct_3I().unpack(str[start:end])
        self.motorCmd.append(val1)
      start = end
      end += 1
      (self.bms.off,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 3
      self.bms.reserve = str[start:end]
      start = end
      end += 40
      self.wirelessRemote = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.reserve, _x.crc,) = _get_struct_2I().unpack(str[start:end])
      self.ff = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.ff.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B2HIB().pack(_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth))
      if len(self.motorCmd) != 20:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (20, len(self.motorCmd), 'self.motorCmd')))
      for val1 in self.motorCmd:
        _x = val1
        buff.write(_get_struct_B5f().pack(_x.mode, _x.q, _x.dq, _x.tau, _x.Kp, _x.Kd))
        buff.write(val1.reserve.tostring())
      _x = self.bms.off
      buff.write(_get_struct_B().pack(_x))
      _x = self.bms.reserve
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_3B().pack(*_x))
      else:
        buff.write(_get_struct_3s().pack(_x))
      _x = self.wirelessRemote
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_40B().pack(*_x))
      else:
        buff.write(_get_struct_40s().pack(_x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.reserve, _x.crc))
      if len(self.ff) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.ff), 'self.ff')))
      for val1 in self.ff:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.motorCmd is None:
        self.motorCmd = None
      if self.bms is None:
        self.bms = unitree_legged_msgs.msg.BmsCmd()
      if self.ff is None:
        self.ff = None
      end = 0
      _x = self
      start = end
      end += 10
      (_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth,) = _get_struct_B2HIB().unpack(str[start:end])
      self.motorCmd = []
      for i in range(0, 20):
        val1 = unitree_legged_msgs.msg.MotorCmd()
        _x = val1
        start = end
        end += 21
        (_x.mode, _x.q, _x.dq, _x.tau, _x.Kp, _x.Kd,) = _get_struct_B5f().unpack(str[start:end])
        start = end
        end += 12
        val1.reserve = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=3)
        self.motorCmd.append(val1)
      start = end
      end += 1
      (self.bms.off,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 3
      self.bms.reserve = str[start:end]
      start = end
      end += 40
      self.wirelessRemote = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.reserve, _x.crc,) = _get_struct_2I().unpack(str[start:end])
      self.ff = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.ff.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3B = None
def _get_struct_3B():
    global _struct_3B
    if _struct_3B is None:
        _struct_3B = struct.Struct("<3B")
    return _struct_3B
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_3s = None
def _get_struct_3s():
    global _struct_3s
    if _struct_3s is None:
        _struct_3s = struct.Struct("<3s")
    return _struct_3s
_struct_40B = None
def _get_struct_40B():
    global _struct_40B
    if _struct_40B is None:
        _struct_40B = struct.Struct("<40B")
    return _struct_40B
_struct_40s = None
def _get_struct_40s():
    global _struct_40s
    if _struct_40s is None:
        _struct_40s = struct.Struct("<40s")
    return _struct_40s
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_B2HIB = None
def _get_struct_B2HIB():
    global _struct_B2HIB
    if _struct_B2HIB is None:
        _struct_B2HIB = struct.Struct("<B2HIB")
    return _struct_B2HIB
_struct_B5f = None
def _get_struct_B5f():
    global _struct_B5f
    if _struct_B5f is None:
        _struct_B5f = struct.Struct("<B5f")
    return _struct_B5f

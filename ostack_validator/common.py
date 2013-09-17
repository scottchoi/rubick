
def find(l, predicate):
  results = [x for x in l if predicate(x)]
  return results[0] if len(results) > 0 else None

def index(l, predicate):
  i = 0
  while i<len(l):
    if predicate(l[i]):
      return i
    i += 1
  return -1

class Version:
  def __init__(self, major, minor=0, maintenance=0):
    "Create Version object by either passing 3 integers, one string or an another Version object"
    if isinstance(major, str):
      self.parts = [int(x) for x in major.split('.', 3)]
      while len(self.parts) < 3:
        self.parts.append(0)

    elif isinstance(major, Version):
      self.parts = major.parts
    else:
      self.parts = [int(major), int(minor), int(maintenance)]

  @property
  def major(self):
    return self.parts[0]

  @major.setter
  def major(self, value):
    self.parts[0] = int(value)

  @property
  def minor(self):
    return self.parts[1]

  @minor.setter
  def minor(self, value):
    self.parts[1] = int(value)

  @property
  def maintenance(self):
    return self.parts[2]

  @maintenance.setter
  def maintenance(self, value):
    self.parts[2] = value

  def __str__(self):
    return '.'.join([str(p) for p in self.parts])

  def __repr__(self):
    return '<Version %s>' % str(self)

  def __cmp__(self, other):
    for i in xrange(0, 3):
      x = self.parts[i] - other.parts[i]
      if x != 0:
        return -1 if x < 0 else 1

    return 0


class Mark(object):
  def __init__(self, source, line=0, column=0):
    self.source = source
    self.line = line
    self.column = column

  def __eq__(self, other):
    return (self.source == source) and (self.line == other.line) and (self.column == other.column)

  def __ne__(self, other):
    return not self == other

  def merge(self, other):
    return Mark(self.source, self.line + other.line - 1, self.column + other.column - 1)

  def __repr__(self):
    return '%s line %d column %d' % (self.source, self.line, self.column)

class Error:
  def __init__(self, message):
    self.message = message

  def __repr__(self):
    return '<%s "%s">' % (str(self.__class__).split('.')[-1][:-2], self.message)

  def __str__(self):
    return self.message

ERROR = 'ERROR'
WARNING = 'WARNING'
INFO = 'INFO'

class Issue(object):
  def __init__(self, type, message):
    self.type = type
    self.message = message

  def __repr__(self):
    return '<%s type=%s message=%s>' % (str(self.__class__).split('.')[-1][:-2], self.type, self.message)

  def __str__(self):
    return 'Error: %s' % self.message

class MarkedIssue(Issue):
  def __init__(self, type, message, mark):
    super(MarkedIssue, self).__init__(type, message)
    self.mark = mark

  def __repr__(self):
    return '<%s type=%s message=%s mark=%s>' % (str(self.__class__).split('.')[-1][:-2], self.type, self.message, self.mark)

  def __str__(self):
    return super(MarkedIssue, self).__str__() + (' (source "%s" line %d column %d)' % (self.mark.source, self.mark.line, self.mark.column))


class Inspection(object):
  def inspect(openstack):
    pass


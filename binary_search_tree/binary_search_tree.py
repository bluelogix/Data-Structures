class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return self
    elif target < self.value:
      if self.left is None:
        return None
      else:
        return self.left.contains(target)
    else:
      if self.right is None:
        return None
      else: 
        return self.right.contains(target)

  def get_max(self):
    current = self  
    while(current.right): 
        current = current.right 
    return current.value

  def for_each(self, cb):
    cb(self.value)
    if self.left:
        self.left.for_each(cb)
    if self.right:
        self.right.for_each(cb)
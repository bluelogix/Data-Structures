class Heap:
  def __init__(self):
    self.storage = []
    
  # need bubble up for 
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  # need sift down for 
  def delete(self):
    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
      else:
        break

  def _sift_down(self, index):
    pass


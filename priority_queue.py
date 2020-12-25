from queue import PriorityQueue

class MaxPriorityQueue:
  def __init__(self):
    self.queue = PriorityQueue()

  def put(self, item):
    self.queue.put((-item, item))
    return item

  def get(self):
    tmp = self.queue.get()
    return tmp[1]

  def empty(self):
    return self.queue.empty()

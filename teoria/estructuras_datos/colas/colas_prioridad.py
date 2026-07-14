import heapq


class PriorityQueue:
  def __init__(self):
    self._heap = []
    self._contador = 0

  def push(self, prioridad, valor):
    heapq.heappush(self._heap, (prioridad, self._contador, valor))
    self._contador += 1

  def pop(self):
    if not self._heap:
      return None
    prioridad, _, valor = heapq.heappop(self._heap)
    return prioridad, valor

  def peek(self):
    return None if not self._heap else (self._heap[0][0], self._heap[0][2])

  def __len__(self):
    return len(self._heap)


if __name__ == "__main__":
  pq = PriorityQueue()

  pq.push(5, "soporte estandar")
  pq.push(1, "soporte urgente")
  pq.push(10, "tarea batch")
  pq.push(3, "consulta general")

  print("peek inicial:", pq.peek())

  while len(pq):
    prioridad, valor = pq.pop()
    print(f"Atendiendo prioridad={prioridad} -> {valor}")
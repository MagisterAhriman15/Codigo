import heapq


class MaxHeap:
  def __init__(self):
    self._heap = []
    self._contador = 0

  def push(self, valor):
    heapq.heappush(self._heap, (-valor, self._contador, valor))
    self._contador += 1

  def pop(self):
    if not self._heap:
      return None
    _, _, valor = heapq.heappop(self._heap)
    return valor

  def heapify(self, valores):
    self._heap = [(-v, i, v) for i, v in enumerate(valores)]
    heapq.heapify(self._heap)
    self._contador = len(valores)

  def imprimir(self):
    print("[heap] n=", len(self._heap), "->", [v for _, _, v in self._heap])


if __name__ == "__main__":
  heap = MaxHeap()

  for v in (45, 10, 78, 32):
    heap.push(v)
  heap.imprimir()

  while len(heap._heap):
    print("extraido:", heap.pop())
  heap.imprimir()

  heap.heapify([5, 1, 9, 4, 2, 7])
  heap.imprimir()
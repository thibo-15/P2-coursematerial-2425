class CircularBuffer:
    def __init__(self, n):
        self.max_size = n
        self.buffer = []

    def add(self, item):
        if len(self.buffer) >= self.max_size:
            self.buffer.pop(0)  # Verwijder het oudste element
        self.buffer.append(item)  # Voeg het nieuwe element toe

    def __getitem__(self, index):
        return self.buffer[index] #geef item op index terug

    def __len__(self):
        return len(self.buffer) #geef lengte van buffer terug

    

# Test code
if __name__ == "__main__":
    buffer = CircularBuffer(3)

    print(len(buffer))  # Output: 0 (buffer is leeg)

    buffer.add('a')
    buffer.add('b')
    buffer.add('c')

    print(len(buffer))  # Output: 3
    print(buffer[0], buffer[1], buffer[2])  # Output: a b c

    buffer.add('d')  # 'a' wordt verwijderd
    print(len(buffer))  # Output: 3
    print(buffer[0], buffer[1], buffer[2])  # Output: b c d

    buffer.add('e')  # 'b' wordt verwijderd
    print(len(buffer))  # Output: 3
    print(buffer[0], buffer[1], buffer[2])  # Output: c d e
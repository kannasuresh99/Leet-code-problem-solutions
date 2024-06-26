def towers_of_hanoi(n, source, destination, auxilary):
    if n == 1:
        print(f"Moving disk 1 from {source} to {destination}")
    towers_of_hanoi(n-1, source, auxilary, destination)
    print(f"Moving the disk {n} from source {source} to destination {destination}")
    towers_of_hanoi(n-1, auxilary, destination, source)


towers_of_hanoi(2, 'A', 'C', 'B')
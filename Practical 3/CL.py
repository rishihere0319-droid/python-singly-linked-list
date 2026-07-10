class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Node inserted successfully.")

    def delete(self):
        if self.head is None:
            print("Linked List is empty.")  
            return

        temp = self.head
        self.head = self.head.next
        print(f"Deleted node: {temp.data}")

    def traverse(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head
        print("Linked List:", end=" ")

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


def main():
    sll = SinglyLinkedList()

    while True:
        print("\n===== Singly Linked List =====")
        print("1. Insert")
        print("2. Delete")
        print("3. Traverse")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            value = int(input("Enter value: "))
            sll.insert(value)

        elif choice == '2':
            sll.delete()

        elif choice == '3':
            sll.traverse()

        elif choice == '4':
            print("Program Ended.")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()

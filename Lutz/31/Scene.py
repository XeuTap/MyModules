class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        print(self.customer.line())
        print(self.clerk.line())
        print(self.parrot.line())


class Customer:
    def line(self):
        return "that's one ex-bird!"


class Clerk:
    def line(self):
        return "no it isn't"


class Parrot:
    def line(self):
        return None


if __name__ == '__main__':
    Scene().action()
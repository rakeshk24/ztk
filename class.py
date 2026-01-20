class App:
    def __init__(self, users, storage, username):
        self.users = users
        self.storage = storage
        self.username = username
        print(f'App: {self} created with the username: {self.username} and storage: {self.storage}')

    def login(self):
        if self.username == "owner" and self.users is not None:
            print(f'welcome {self.username}')
            print(f'storage is {self.storage}')
    
    def increase_capacity(self, capacity):
        self.storage += capacity
        print(f'storage now increased to {self.storage}')

app1 = App(10, 100, 'rakesh')
app1.login()
app1.increase_capacity(50)
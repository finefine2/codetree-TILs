class User:
    def __init__(self, next_id = "", next_level = 0):
        self.next_id = next_id
        self.next_level = next_level


user = User()
user.next_id = "codetree"
user.next_level = 10

user2_id, level2 = tuple(input().split())
user2 = User()
user2.user2_id = user2_id
user2.level2 = int(level2)

print(f"user {user.next_id} lv {user.next_level}")
print(f"user {user2.user2_id} lv {user2.level2}")
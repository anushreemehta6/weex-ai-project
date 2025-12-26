from bot.account import get_position
from bot.account import get_balance, get_position

status, data = get_position()
print(status)
print(data)


print("POSITIONS:")
print(get_position())

print("\nBALANCE:")
print(get_balance())

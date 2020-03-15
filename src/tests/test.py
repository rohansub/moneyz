from src.models.account import Account
from src.models.profile import Profile
from src.models.transaction import Transaction

p = Profile.create(name="test")
a = Account.create(name="test_account", profile=p)
t = Transaction.create(
    name="test_account", 
    value=0.0, 
    category="yeet", 
    description="supreme",
    account=a,
)

print(p)
print(t)
print(a)

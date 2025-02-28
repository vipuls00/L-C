import bcrypt

# Hashed password (your given hash)
hashed_password = b"$2b$12$zH9lHkJaIz238dPBmIVmLe2G/6pJPCCnKfZclBXp8/fvU4jTLvkk2"

# Input password to check
password = "ITTprom1234".encode()

# Verify if it matches
if bcrypt.checkpw(password, hashed_password):
    print("Password is correct!")
else:
    print("Incorrect password.")

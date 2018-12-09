import hashlib, itertools
inp = "bgvyzdsv"
def mine(zeros):
    prefix = "0" * zeros
    for i in itertools.count():
        key = inp + str(i)
        digest = hashlib.md5(key.encode("utf-8")).hexdigest()
        if digest.startswith(prefix):
            return(i)

print(mine(5))
print(mine(6))

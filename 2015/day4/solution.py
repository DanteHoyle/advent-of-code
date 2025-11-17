import hashlib

def mine_adventcoin(secret_key: str, difficulty: int):
    def salted_hash(text: str):
        salted_text = secret_key + text
        md5_hash = hashlib.md5(salted_text.encode('utf-8')).hexdigest()
        return md5_hash

    def is_valid_hash(hash: str, difficulty: int):
        return hash[:difficulty] == '0' * difficulty

    index = 1

    while not is_valid_hash(salted_hash(str(index)), difficulty):
        index += 1

    print('Finished mining AdventCoin!')
    print(f'Current Secret: {secret_key}')
    print(f'Current index: {index}')
    print(f'MD5 HASH: {salted_hash(str(index))}')

mine_adventcoin('iwrupvqb', 5)
mine_adventcoin('iwrupvqb', 6)

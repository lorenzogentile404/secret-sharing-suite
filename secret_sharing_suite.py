from random import randint

# https://lorenzogentile404.github.io/posts/2020/06/2020-06-14-queen-treasure/

# Common
def compute_shares(s, n):
    S = [0 for i in range(0,n)]
    for i in range(0, n):
        if i == n - 1:
            S[n-1] = (s - sum(S)) % q # s_n = s - (s_1 + ... + s_{n-1}) % q
        else:
            S[i] = randint(0,q-1) # s_1,...,s_{n-1}
        print('s_' + str(i + 1) + ': ' + str(S[i]))
    return S

def reconstruct(S):
    s_rec = sum(S) % q
    print('\ns_r:', s_rec)
    print('Reconstructed secret message:', int_to_string(s_rec,len(msg)))

string_to_int = lambda msg : int.from_bytes(bytes(msg, 'utf-8'), byteorder = 'big')
int_to_string = lambda n,l : n.to_bytes(l, byteorder='big').decode("utf-8")

selection = int(input('Select type of secret sharing:' +
            '\n(1) n-out-of-n secret sharing' +
            '\n(2) t-out-of-n secret sharing' +
            '\n(3) general access structure secret sharing\n'))

################################################################################

if selection == 1:
    print('\nn-out-of-n secret sharing\n')

    msg = input('Insert secret message: ')
    n = int(input('Insert number of parties n: ')) # Number of parties/shares

    q = 2**(len(msg)*8) # s, s1,..., s_n \in Z_q

    # Convert msg to int
    s = string_to_int(msg)
    print('\ns_i: ' + str(s) + '\n')

    # Parties
    P = [i for i in range(1,n+1)]
    print('Parties:',  P)

    # Compute shares
    S = compute_shares(s, n)

    # Distribute shares
    for i in range(0,len(S)):
        print('Send s_' + str(i + 1) + ' to party ' + str(i+1))

    # Reconstruct
    reconstruct(S)

################################################################################

elif selection == 2:
    print('\nt-out-of-n secret sharing\n')

    msg = input('Insert secret message: ')
    n = int(input('Insert number of parties n: ')) # Number of parties
    t = int(input('Insert number of parties required to reconstruct the secret t: ')) # Number of parties required to reconstruct the secret

    q = 2**(len(msg)*8) # s, s1,..., s_n \in Z_q

    # Convert msg to int
    s = string_to_int(msg)
    print('\ns_i: ' + str(s) + '\n')

    # Parties
    P = [i for i in range(1,n+1)]
    print('Parties:',  P)

    import itertools
    def findsubsets(s, n):
        return list(itertools.combinations(s, n))

    PI = findsubsets(P,t-1) # Secrecy structure PI = {T_1 = {}, ...}
    hatT = [list(set(P).difference(t)) for t in PI] # hatT = P \ T_i with T_i \in PI

    print('Secrecy structure PI (maximal unqualified sets):', str([list(t) for t in PI]))
    print('hatT = P \ T_i with T_i \in PI:', str(hatT))

    # Compute shares
    S = compute_shares(s, len(hatT))

    # Distribute shares
    for i, hatT in zip(range(0,len(S)), hatT):
        print('Send s_' + str(i + 1) + ' to parties in hatT_' + str(i + 1) + ': ' + str(hatT))

    # Reconstruct
    reconstruct(S)

################################################################################

elif selection == 3:
    print('\ngeneral access structure secret sharing\n')

    msg = input('Insert secret message: ')
    n = int(input('Insert number of parties n: ')) # Number of parties

    q = 2**(len(msg)*8) # s, s1,..., s_n \in Z_q

    # Convert msg to int
    s = string_to_int(msg)
    print('\ns_i: ' + str(s) + '\n')

    # Parties
    P = [i for i in range(1,n+1)]
    print('Parties:',  P)

    PI = input('Insert secrecy structure PI (maximal unqualified sets): ')
    import json
    PI = [tuple(t) for t in json.loads(PI)]

    hatT = [list(set(P).difference(t)) for t in PI] # hatT = P \ T_i with T_i \in PI

    print('Secrecy structure PI (maximal unqualified sets):', str([list(t) for t in PI]))
    print('hatT = P \ T_i with T_i \in PI:', str(hatT))

    # Compute shares
    S = compute_shares(s, len(hatT))

    # Distribute shares
    for i, hatT in zip(range(0,len(S)), hatT):
        print('Send s_' + str(i + 1) + ' to parties in hatT_' + str(i + 1) + ': ' + str(hatT))

    # Reconstruct
    reconstruct(S)

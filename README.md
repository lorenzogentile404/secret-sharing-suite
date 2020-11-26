# secret-sharing-suite

A Python script to play with different types of secret sharing:

  1. n-out-of-n secret sharing
  2. t-out-of-n secret sharing
  3. general access structure secret sharing

## Examples of usage

### n-out-of-n secret sharing
```console
user@host:~/secret-sharing-suite$ python3 secret_sharing_suite.py
Select type of secret sharing:
(1) n-out-of-n secret sharing
(2) t-out-of-n secret sharing
(3) general access structure secret sharing
1

n-out-of-n secret sharing

Insert secret message: This is a secret message!
Insert number of parties n: 4
Group Z_q with q = 1606938044258990275541962092341162602522202993782792835301376

s   = 529836718428447222471796390999758048326993546175927353304353

Parties =  [1, 2, 3, 4]
s_1,..., s_{n-1} <-$- Z_q
s_n = (s - (s_1 + ... + s_{n-1})) % q
s_1 = 817914728430332614209143214949107377860300844005888778691035
s_2 = 145313392047642646036453930347879639059238885116921328377986
s_3 = 755758932603553258688109479200183561363129400506854103187509
s_4 = 417787709605908979080051858843750072566527410329055978349199
Send s_1 to party 1
Send s_2 to party 2
Send s_3 to party 3
Send s_4 to party 4

s_r = (s_1 + ... + s_n) % q
s_r = 529836718428447222471796390999758048326993546175927353304353 => This is a secret message!
```
### t-out-of-n secret sharing
```console
user@host:~/secret-sharing-suite$ python3 secret_sharing_suite.py
Select type of secret sharing:
(1) n-out-of-n secret sharing
(2) t-out-of-n secret sharing
(3) general access structure secret sharing
2

t-out-of-n secret sharing

Insert secret message: This is a secret message!
Insert number of parties n: 4
Insert number of parties required to reconstruct the secret t: 2
Group Z_q with q = 1606938044258990275541962092341162602522202993782792835301376

s   = 529836718428447222471796390999758048326993546175927353304353

Parties =  [1, 2, 3, 4]
Secrecy structure PI (maximal unqualified sets) =  [[1], [2], [3], [4]]
Access structure GAMMA (minimal qualified sets) =  [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
hatT = P \ T_i with T_i \in PI =  [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]
s_1,..., s_{n-1} <-$- Z_q
s_n = (s - (s_1 + ... + s_{n-1})) % q
s_1 = 925169835384432937955312711009115986182093701172207045676629
s_2 = 401302881428885489144048802123171617449532688680514577349044
s_3 = 406991123064328225723394045830455401560902759380562673987451
s_4 = 403310922809790845191002924378177645656667390725435891592605
Send s_1 to parties in hatT_1 = [2, 3, 4]
Send s_2 to parties in hatT_2 = [1, 3, 4]
Send s_3 to parties in hatT_3 = [1, 2, 4]
Send s_4 to parties in hatT_4 = [1, 2, 3]

s_r = (s_1 + ... + s_n) % q
s_r = 529836718428447222471796390999758048326993546175927353304353 => This is a secret message!
```
### general access structure secret sharing
```console
user@host:~/secret-sharing-suite$ python3 python3 secret_sharing_suite.py
Select type of secret sharing:
(1) n-out-of-n secret sharing
(2) t-out-of-n secret sharing
(3) general access structure secret sharing
3

general access structure secret sharing

Insert secret message: This is a secret message!
Insert number of parties n: 4
Group Z_q with q = 1606938044258990275541962092341162602522202993782792835301376

s   = 529836718428447222471796390999758048326993546175927353304353

Parties =  [1, 2, 3, 4]
Insert secrecy structure PI (maximal unqualified sets): [[1,2],[1,3],[2,3],[4]]
Secrecy structure PI (maximal unqualified sets) =  [[1, 2], [1, 3], [2, 3], [4]]
Access structure GAMMA (minimal qualified sets) =  [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [4, 1], [4, 2], [4, 3]]
hatT = P \ T_i with T_i \in PI =  [[3, 4], [2, 4], [1, 4], [1, 2, 3]]
s_1,..., s_{n-1} <-$- Z_q
s_n = (s - (s_1 + ... + s_{n-1})) % q
s_1 = 788992307122825458459287124426901644515118169142077942167435
s_2 = 354342958127503155646430347994717505309344563776324740809949
s_3 = 172303602897870039551241174711831198212947169444821200294137
s_4 = 821135894539238844356799836207470302811786637595496305334208
Send s_1 to parties in hatT_1 = [3, 4]
Send s_2 to parties in hatT_2 = [2, 4]
Send s_3 to parties in hatT_3 = [1, 4]
Send s_4 to parties in hatT_4 = [1, 2, 3]

s_r = (s_1 + ... + s_n) % q
s_r = 529836718428447222471796390999758048326993546175927353304353 => This is a secret message!
```

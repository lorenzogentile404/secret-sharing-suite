# secret-sharing-suite

A Python script to play with different types of secret sharing:

  1. n-out-of-n secret sharing
  2. t-out-of-n secret sharing
  3. general access structure secret sharing

## Examples of usage

### n-out-of-n secret sharing
```
user@host:~/secret-sharing-suite$ python3 secret_sharing_suite.py 
Select type of secret sharing:
(1) n-out-of-n secret sharing
(2) t-out-of-n secret sharing
(3) general access structure secret sharing
1

n-out-of-n secret sharing

Insert secret message: This is a secret message!
Insert number of parties n: 3

s_i: 529836718428447222471796390999758048326993546175927353304353

Parties: [1, 2, 3]
s_1: 631519157167820681430365047978303167154375732121345006359298
s_2: 847850737790194400279938709133980823357035971160716282653838
s_3: 657404867729422416303454726228636660337784836676658899592593
Send s_1 to party 1
Send s_2 to party 2
Send s_3 to party 3

s_r: 529836718428447222471796390999758048326993546175927353304353
Reconstructed secret message: This is a secret message!
```
### t-out-of-n secret sharing
```
user@host:~/secret-sharing-suite$ python3 secret_sharing_suite.py 
Select type of secret sharing:
(1) n-out-of-n secret sharing
(2) t-out-of-n secret sharing
(3) general access structure secret sharing
2

t-out-of-n secret sharing

Insert secret message: This is a secret message!
Insert number of parties n: 3
Insert number of parties required to reconstruct the secret t: 2

s_i: 529836718428447222471796390999758048326993546175927353304353

Parties: [1, 2, 3]
Secrecy structure PI (maximal unqualified sets): [[1], [2], [3]]
hatT = P \ T_i with T_i \in PI: [[2, 3], [1, 3], [1, 2]]
s_1: 980744588102789935147659000985711570473065812494697434563814
s_2: 591920648007723199019988468479171551051910380225616178373938
s_3: 564109526576924363846111013876037529324220347238406575667977
Send s_1 to parties in hatT_1: [2, 3]
Send s_2 to parties in hatT_2: [1, 3]
Send s_3 to parties in hatT_3: [1, 2]

s_r: 529836718428447222471796390999758048326993546175927353304353
Reconstructed secret message: This is a secret message!
```
### general access structure secret sharing
```
user@host:~/secret-sharing-suite$ python3 secret_sharing_suite.py 
Select type of secret sharing:
(1) n-out-of-n secret sharing
(2) t-out-of-n secret sharing
(3) general access structure secret sharing
3

general access structure secret sharing

Insert secret message: This is a secret message!
Insert number of parties n: 4

s_i: 529836718428447222471796390999758048326993546175927353304353

Parties: [1, 2, 3, 4]
Insert secrecy structure PI (maximal unqualified sets): [[1, 2], [1, 3], [2, 3], [4]]
Secrecy structure PI (maximal unqualified sets): [[1, 2], [1, 3], [2, 3], [4]]
hatT = P \ T_i with T_i \in PI: [[3, 4], [2, 4], [1, 4], [1, 2, 3]]
s_1: 930498484205961274404947983597816134705089434447090211532930
s_2: 136177387220825017673519069020193725047389490208322475613250
s_3: 678136107205878343854210613019678983916912741357067991968860
s_4: 391962784054772862081080817703231807179804873946239509490689
Send s_1 to parties in hatT_1: [3, 4]
Send s_2 to parties in hatT_2: [2, 4]
Send s_3 to parties in hatT_3: [1, 4]
Send s_4 to parties in hatT_4: [1, 2, 3]

s_r: 529836718428447222471796390999758048326993546175927353304353
Reconstructed secret message: This is a secret message!
```

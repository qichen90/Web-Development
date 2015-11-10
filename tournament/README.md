# Tournament
<h3>Description</h3>
https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true
https://www.udacity.com/course/viewer#!/c-ud197/l-3521918727/m-3519689284

<h3>Files</h3>
* tournament.py -- implementation of a Swiss-system tournament
* tournament.sql -- table definitions for the tournament project.
* tournament_test.py -- Test cases for tournament.py

<h3>Usage</h3>
* start within VM
* import SQL file using ``` psql \i tournament.sql```
* run test ```python tournament_test.py```

<h3>Result</h3>
```
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```

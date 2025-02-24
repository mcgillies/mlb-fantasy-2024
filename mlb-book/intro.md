## MLB 2025 Analysis:

It is almost time for baseball season. Return of the nerds unite. 

I have created a set of predictions designed for my fantasy baseball league, an ESPN hosted 12 team points league. The easy and likely more reliable approach would be to simply convert one of the many projection systems on Fangraphs into fantasy points, however I wanted to take my own path. The scoring for players works as follows:

Pitchers:
    + 3 per IP (+ 1 per out)
    + 1 per K
    - 1 per BB
    - 1 per Hit
    - 2 per ER
    + 2 per Win
    - 2 per Loss
    + 2 per Hold
    + 5 per Save


Batters:
    + 1 per TB
    + 1 per R
    + 1 per RBI
    + 1 per BB
    + 1 per SB
    - 1 per K


The scoring can be edited in [here](https://github.com/mcgillies/mlb-fantasy-2025/blob/main/data_cleaning/calc_fpoints.py) if you are playing under a different scoring system. Although this is designed for fantasy purposes, it can still generally be applied for overall player value (minus defence). Batter fantasy score can be interpreted as an overarching offensive stat, while pitcher fantasy points function similarly, but to a lesser extent as "team" related stats such as Wins, Losses, Holds, and Saves are more prevalent. Keep in mind this definition of "team stats" as I will use it throughout. 

I would classify these more as supplemental rankings - there are many small nuances that I was not able to capture simply due to not having enough time to account for all of these. For example, pitchers converting from relievers to starters such as Clay Holmes are not adjusted for their new role. Keep this in mind when looking at the rankings and use judgement where need be. Other small issues do persist, such as players with the same name (ie. Luis Garcia) all being classified as one player. 

Note: the model does not predict rookies - I have not been able to correctly implement minor league data yet. 

Before all of this credit to Baseball Savant (https://baseballsavant.mlb.com/), Fangraphs (https://www.fangraphs.com/) along with RazzBall (https://razzball.com/) for the data used in my analysis. 

```{tableofcontents}
```

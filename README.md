# FireEmblemHeroesData
Uses Scrapy-Splash to scrape [https://fireemblem.gamepress.gg/](https://fireemblem.gamepress.gg/) for all available heroes, stats, recommended skill builds and IVs, and more.

Latest scraped data is available in raw JSON data here:

https://github.com/jacobspark/FireEmblemHeroesData/blob/master/feed_exports/index.json

Updated as of 3/17/19.

## Format
The data in the JSON file is formatted as following:

```js
{
       "Name":"Alm",
       "Tier Rating":"3",
       "Movement Type":"Infantry",
       "Weapon":"Red Sword",
       "Total Stats":"158",
       "Recommended Builds":[
          {
             "Weapon":"Falchion (Echoes) (Refined)",
             "Assist":"Reposition",
             "Special":"Moonbow",
             "A Skill":"Death Blow 4",
             "B Skill":"Windsweep 3",
             "C Skill":"Threaten Def 3",
             "S Skill":"Heavy Blade 3",
             "SP":"SP"
          }
       ],
       "Recommended IVs":[
       # Returns Worst, Average, or Best according to Gamepress's recommendation.
          {
             "HP":"Best",
             "ATK":"Best",
             "SPD":"Best",
             "DEF":"Average",
             "RES":"Worst"
          }
       ],
       "Stats":[
       # Each stat is formatted as [Low, Medium, High].
       # For some heroes who only have neutral stats (i.e., Alfonse), value of null is returned for Low and High stats.
          {
          # Level 1 Stats
             "1":{
                "No Weapon":{
                   "HP":[
                      "20",
                      "21",
                      "22"
                   ],
                   "ATK":[
                      "8",
                      "9",
                      "10"
                   ],
                   "SPD":[
                      "5",
                      "6",
                      "7"
                   ],
                   "DEF":[
                      "5",
                      "6",
                      "7"
                   ],
                   "RES":[
                      "4",
                      "5",
                      "6"
                   ]
                },
                "Weapon":{
                   "HP":[
                      "20",
                      "21",
                      "22"
                   ],
                   "ATK":[
                      "24",
                      "25",
                      "26"
                   ],
                   "SPD":[
                      "5",
                      "6",
                      "7"
                   ],
                   "DEF":[
                      "5",
                      "6",
                      null
                   ],
                   "RES":[
                      "4",
                      "5",
                      "6"
                   ]
                }
             },
             # Level 40 Stats
             "40":{
                "No Weapon":{
                   "HP":[
                      "42",
                      "45",
                      "22"
                   ],
                   "ATK":[
                      "30",
                      "33",
                      "10"
                   ],
                   "SPD":[
                      "27",
                      "30",
                      "7"
                   ],
                   "DEF":[
                      "24",
                      "28",
                      "7"
                   ],
                   "RES":[
                      "19",
                      "22",
                      "6"
                   ]
                },
                "Weapon":{
                   "HP":[
                      "42",
                      "45",
                      "48"
                   ],
                   "ATK":[
                      "46",
                      "49",
                      "52"
                   ],
                   "SPD":[
                      "27",
                      "30",
                      "33"
                   ],
                   "DEF":[
                      "24",
                      "28",
                      null
                   ],
                   "RES":[
                      "19",
                      "22",
                      "25"
                   ]
                }
             }
          }
       ]
    }
    ```

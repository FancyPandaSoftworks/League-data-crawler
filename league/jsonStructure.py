###Q ability of a champ
'''
[{'name': 'The Darkin Blade',
'icon': 'http://raw.communitydragon.org/latest/game/assets/characters/aatrox/hud/icons2d/aatrox_q.png',
'effects': [
{'description': "Active: Aatrox strikes all enemies in a line, dealing physical damage. The Darkin Blade can be reactivated twice within 4 seconds, with the first recast refreshing the timer. There's a 1 second cooldown between each cast. Enemies hit by the edge of the blade are dealt 50% bonus damage and are knocked up for 0.25 seconds, doubled to 0.5 seconds against monsters.",
'leveling': [{'attribute': 'Physical Damage',
            'modifiers': [{'values':
                            [10, 30, 50, 70, 90],
                            'units': ['', '', '', '', '']},
                            {'values': [60, 65, 70, 75, 80],
                            'units': ['% AD', '% AD', '% AD', '% AD', '% AD']}]},
            {'attribute': 'Amplified Damage',
            'modifiers': [{'values': [15, 45, 75, 105, 135],
                'units': ['', '', '', '', '']},
            {'values': [90, 97.5, 105, 112.5, 120],
            'units': ['% AD', '% AD', '% AD', '% AD', '% AD']}]}]},
{'description': 'First Recast: Aatrox strikes all enemies in a cone, dealing 25% increased damage than the first strike.',
'leveling': [{'attribute': 'Physical Damage',
'modifiers': [{'values': [12.5, 37.5, 62.5, 87.5, 112.5],
                'units': ['', '', '', '', '']},
                {'values': [75, 81.25, 87.5, 93.75, 100],
                'units': ['% AD', '% AD', '% AD', '% AD', '% AD']}]},
{'attribute': 'Amplified Damage',
'modifiers': [{'values': [18.75, 56.25, 93.75, 131.25, 168.75],
                'units': ['', '', '', '', '']},
                {'values': [112.5, 121.875, 131.25, 140.625, 150],
                'units': ['% AD', '% AD', '% AD', '% AD', '% AD']}]}]},
{'description': 'Second Recast: Aatrox strikes all enemies near the target area 225 units away, dealing 50% increased damage than the first strike.',
'leveling': [{'attribute': 'Physical Damage',
'modifiers': [{'values': [15, 45, 75, 105, 135],
                'units': ['', '', '', '', '']},
                {'values': [90, 97.5, 105, 112.5, 120],
                'units': ['% AD', '% AD', '% AD', '% AD', '% AD']}]},
{'attribute': 'Amplified Damage',
'modifiers': [{'values': [22.5, 67.5, 112.5, 157.5, 202.5],
                'units': ['', '', '', '', '']},
                {'values': [135, 146.25, 157.5, 168.75, 180],
                'units': ['% AD', '% AD', '% AD', '% AD', '% AD']}]}]},
{'description': 'Each strike deals 55% damage against minions.',
'leveling': [{'attribute': 'Maximum Non-Minion Damage',
'modifiers': [{'values': [56.25, 168.75, 281.25, 393.75, 506.25],
                'units': ['', '', '', '', '']},
                {'values': [337.5, 365.625, 393.75, 421.875, 450],
                'units': ['% AD', '% AD', '% AD', '% AD', '% AD']}]}]}],
'cost': None,
'cooldown': {'modifiers': [{'values': [14, 12, 10, 8, 6],
                'units': ['', '', '', '', '']}],
                'affectedByCdr': True},
'targeting': 'Direction', 'affects': 'Enemies', 'spellshieldable': 'True', 'resource': None, 'damageType': 'PHYSICAL_DAMAGE', 'spellEffects': 'spellaoe', 'projectile': None, 'onHitEffects': None, 'occurrence': None, 'notes': "Each cast counts as an ability activation for the purposes of on-cast effects such as Spellblade, charging  Spellbinder, and stacking  Force Pulse.\n Aatrox cannot move and cast abilities during the cast time, except for  Umbral Dash and  Flash.\n The hitbox and Aatrox's model are fixed to the initial target direction.\n Aatrox's facing-direction, for effects such as  Petrifying Gaze, is the direction he is moving, and not the direction the model is facing.\n\n All damage modifiers stack multiplicatively.\n The first cast extends at 50 units behind Aatrox, the second cast extends at 100 units.", 'blurb': 'Active:  Aatrox slams his greatsword down, dealing  physical damage. Targets hit with the edge of the blade receive more damage and are briefly  knocked up. He can swing three times, each with a different area of effect.', 'missileSpeed': None, 'rechargeRate': None, 'collisionRadius': None, 'tetherRadius': None, 'onTargetCdStatic': None, 'innerRadius': None, 'speed': None, 'width': '200', 'angle': '70°', 'castTime': '0.6', 'effectRadius': '300', 'targetRange': '650 / 525 / 180'}]
'''

'''
[{'name': 'Weapons of the Faithful', 
'icon': 'http://raw.communitydragon.org/latest/game/assets/characters/aphelios/hud/icons2d/apheliosq.png', 
'effects': [{'description': "The active effect of Aphelios' varies based on his current main hand weapon.", 
            'leveling': []}, 
            {'description': 'The individual actives do not share a cooldown.', 
            'leveling': []}], 
'cost': None, 
'cooldown': None, 'targeting': None, 'affects': None, 'spellshieldable': None, 'resource': None, 'damageType': None, 'spellEffects': None, 'projectile': None, 'onHitEffects': None, 'occurrence': None, 'notes': None, 

'blurb': "The active effect of  Aphelios'  varies based on his current main weapon.\n Calibrum -  Moonshot: Long range shot that marks its target for a long-range follow-up attack.\n Severum -  Onslaught: Gain  bonus movement speed while attacking a single enemy with both weapons.\n Gravitum -  Binding Eclipse:  Root all enemies who are * slowed by this weapon.\n Infernum -  Duskwave: Blast enemies in a cone and attack them with your off-hand weapon.\n Crescendum -  Sentry: Deploy a sentry that shoots your off-hand weapon.", 'missileSpeed': None, 'rechargeRate': None, 'collisionRadius': None, 'tetherRadius': None, 'onTargetCdStatic': None, 'innerRadius': None, 'speed': None, 'width': None, 'angle': None, 'castTime': None, 'effectRadius': None, 'targetRange': None}, 
{'name': 'Moonshot', 'icon': 'http://raw.communitydragon.org/latest/game/assets/characters/aphelios/hud/icons2d/apheliosq.png', 
'effects': [{'description': 'Calibrum - Active: Aphelios fires a bolt of energy in a line, dealing 60 − 160 (based on level) (+ 42% − 60% (based on level) bonus AD) (+ 100% AP) physical damage to the first enemy hit.', 
            'leveling': []}], 
'cost': {'modifiers': [{'values': [10, 10, 10, 10, 10], 
            'units': [' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight']}, 
            {'values': [60, 60, 60, 60, 60], 'units': ['', '', '', '', '']}]}, 
'cooldown': {'modifiers': [{'values': [10.0, 9.882352941176471, 9.764705882352942, 9.647058823529411, 9.529411764705882, 9.411764705882353, 9.294117647058824, 9.176470588235293, 9.058823529411764, 8.941176470588236, 8.823529411764707, 8.705882352941176, 8.588235294117647, 8.470588235294118, 8.352941176470589, 8.235294117647058, 8.117647058823529, 8.0], 
            'units': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']}], 
'affectedByCdr': True}, 'targeting': 'Direction', 'affects': 'Enemies', 'spellshieldable': 'True', 'resource': 'MANA', 'damageType': 'PHYSICAL_DAMAGE', 'spellEffects': 'spell', 'projectile': 'TRUE', 'onHitEffects': None, 'occurrence': None, 'notes': "Moonshot's name is modified based on Aphelios' off-hand weapon:\n  Resurgent Moonshot\n  Binding Moonshot\n  Incendiary Moonshot\n  Arcing Moonshot", 
'blurb': 'Active:  Aphelios fires a bolt of energy in a line, dealing physical damage and marks the first enemy hit.', 'missileSpeed': None, 'rechargeRate': None, 'collisionRadius': None, 'tetherRadius': None, 'onTargetCdStatic': None, 'innerRadius': None, 'speed': '1850', 'width': '90', 'angle': None, 'castTime': None, 'effectRadius': None, 'targetRange': '1450'}, {'name': 'Onslaught', 'icon': 'http://raw.communitydragon.org/latest/game/assets/characters/aphelios/hud/icons2d/apheliosq.png', 

'effects': [{'description': 'Severum - Active: For 1.75 seconds, Aphelios gains 20% (+ 10% per 100 AP) bonus movement speed and autonomously performs up to 6 (+ 3 per 100% bonus attack speed) attacks over the duration to the nearest enemy, prioritizing enemy champions.', 
            'leveling': []}, 
            {'description': 'Attacks alternate between Severum and his current off-hand weapon, each dealing 10 − 30 (based on level) (+ 21% − 30% (based on level) bonus AD) physical damage, 25% on-hit damage and can critically strike.', 
            'leveling': []}], 
'cost': {'modifiers': [{'values': [10, 10, 10, 10, 10], 
            'units': [' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight']}, 
            {'values': [60, 60, 60, 60, 60], 
            'units': ['', '', '', '', '']}]}, 
'cooldown': {'modifiers': [{'values': [10.0, 9.882352941176471, 9.764705882352942, 9.647058823529411, 9.529411764705882, 9.411764705882353, 9.294117647058824, 9.176470588235293, 9.058823529411764, 8.941176470588236, 8.823529411764707, 8.705882352941176, 8.588235294117647, 8.470588235294118, 8.352941176470589, 8.235294117647058, 8.117647058823529, 8.0], 
            'units': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']}], 
'affectedByCdr': True}, 'targeting': 'Auto-targeted', 'affects': 'Self, Enemies', 'spellshieldable': None, 'resource': 'MANA', 'damageType': 'PHYSICAL_DAMAGE', 'spellEffects': 'attack', 'projectile': 'SPECIAL', 'onHitEffects': None, 'occurrence': None, 'notes': "Severum's attacks are not  intercepted, but the attacks from the off-hand weapon are during Onslaught.\n Onslaught's name is modified based on Aphelios' off-hand weapon:\n  Precision Onslaught\n  Binding Onslaught\n  Incendiary Onslaught\n  Arcing Onslaught\n\n Onslaught doesn't apply on-attack effects.\n  Crescendum will not deal damage if blocked by  Wind Wall, but the stacks will still be gained.\n Cosmetically, the Moonlight cost is consumed through the duration.", 
'blurb': 'Active:  Aphelios gains  bonus movement speed and quickly attack a target with Severum and his current off-hand weapon dealing physical damage to them.', 'missileSpeed': None, 'rechargeRate': None, 'collisionRadius': None, 'tetherRadius': None, 'onTargetCdStatic': None, 'innerRadius': None, 'speed': None, 'width': None, 'angle': None, 'castTime': None, 'effectRadius': None, 'targetRange': None}, {'name': 'Binding Eclipse', 'icon': 'http://raw.communitydragon.org/latest/game/assets/characters/aphelios/hud/icons2d/apheliosq.png', 

'effects': [{'description': "Gravitum - Active: Aphelios expunges all enemies affected by Gravitum's slow, dealing 50 − 110 (based on level) (+ 26% − 35% (based on level) bonus AD) (+ 70% AP) magic damage and rooting them for 1 second.", 
'leveling': []}, 
{'description': 'Binding Eclipse also empowers in-flight Gravitum projectiles to instantly affect their targets upon hitting them.', 'leveling': []}], 'cost': {'modifiers': [{'values': [10, 10, 10, 10, 10], 'units': [' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight']}, {'values': [60, 60, 60, 60, 60], 'units': ['', '', '', '', '']}]}, 'cooldown': {'modifiers': [{'values': [12.0, 11.882352941176471, 11.764705882352942, 11.647058823529411, 11.529411764705882, 11.411764705882353, 11.294117647058824, 11.176470588235293, 11.058823529411764, 10.941176470588236, 10.823529411764707, 10.705882352941176, 10.588235294117647, 10.470588235294118, 10.352941176470589, 10.235294117647058, 10.117647058823529, 10.0], 'units': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']}], 'affectedByCdr': True}, 'targeting': 'Auto-targeted', 'affects': 'Enemies', 'spellshieldable': 'True', 'resource': 'MANA', 'damageType': 'MAGIC_DAMAGE', 'spellEffects': 'Spell', 'projectile': None, 'onHitEffects': None, 'occurrence': None, 'notes': None, 'blurb': 'Active:  Aphelios deals magic damage and roots all targets that are  slowed by Gravitum.', 'missileSpeed': None, 'rechargeRate': None, 'collisionRadius': None, 'tetherRadius': None, 'onTargetCdStatic': None, 'innerRadius': None, 'speed': None, 'width': None, 'angle': None, 'castTime': None, 'effectRadius': 'Global', 'targetRange': None}, {'name': 'Duskwave', 'icon': 'http://raw.communitydragon.org/latest/game/assets/characters/aphelios/hud/icons2d/apheliosq.png', 'effects': [{'description': 'Infernum - Active: Aphelios unleashes a wave of energy in a cone, dealing 25 − 65 (based on level) (+ 56% − 80% (based on level) bonus AD) (+ 70% AP) physical damage to all enemies hit and locking on to each of them. After a delay, Aphelios then fires a volley of attacks from his current off-hand weapon, one at each locked-on enemy, applying on-hit effects. There is no range limit for locked-on targets.', 'leveling': []}], 'cost': {'modifiers': [{'values': [10, 10, 10, 10, 10], 'units': [' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight']}, {'values': [60, 60, 60, 60, 60], 'units': ['', '', '', '', '']}]}, 'cooldown': {'modifiers': [{'values': [9.0, 8.823529411764707, 8.647058823529411, 8.470588235294118, 8.294117647058824, 8.117647058823529, 7.9411764705882355, 7.764705882352941, 7.588235294117647, 7.411764705882353, 7.235294117647059, 7.0588235294117645, 6.882352941176471, 6.705882352941176, 6.529411764705882, 6.352941176470588, 6.1764705882352935, 6.0], 'units': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']}], 'affectedByCdr': True}, 'targeting': 'Direction', 'affects': 'Enemies', 'spellshieldable': 'True', 'resource': 'MANA', 'damageType': 'PHYSICAL_DAMAGE', 'spellEffects': 'special', 'projectile': 'TRUE', 'onHitEffects': None, 'occurrence': None, 'notes': "The volley applies  area damage and the follow up attacks from the off-hand weapon deal  basic damage.\nThe hitbox also includes a very small portion behind Aphelios's character model\n Duskwave's name is modified based on Aphelios' off-hand weapon:\n  Precision Duskwave\n  Resurgent Duskwave\n  Binding Duskwave\n  Arcing Duskwave\n\n Aphelios is  locked-out of performing basic attacks until Duskwave resolves.\n The automatic attacks do not trigger on-attack effects.", 'blurb': 'Active:  Aphelios unleases a wave of energy in a cone, dealing physical damage to all enemies hit and locking on to each of them. After a delay he  basic attack all locked targets.', 'missileSpeed': None, 'rechargeRate': None, 'collisionRadius': None, 'tetherRadius': None, 'onTargetCdStatic': None, 'innerRadius': None, 'speed': None, 'width': None, 'angle': '40°', 'castTime': None, 'effectRadius': None, 'targetRange': '650'}, {'name': 'Sentry', 'icon': 'http://raw.communitydragon.org/latest/game/assets/characters/aphelios/hud/icons2d/apheliosq.png', 'effects': [{'description': "Crescendum - Active: Aphelios deploys an untargetable lunar sentry for up to 20 seconds. The sentry attacks if an enemy gets in range, reducing its duration to 4 seconds and becoming targetable. Deploying a new sentry reduces the eldest's duration to 4 seconds. A sentry has 6 health and take 3 damage per ranged basic attack and 4 damage per AoE abilities.", 'leveling': []}, {'description': "The sentry autonomously attacks the nearest enemy in range with a clone of Aphelios current off-hand weapon at 0.8 attack speed, dealing 25 − 85 (based on level) (+ 35% − 50% (based on level) bonus AD) (+ 50% AP) physical damage. The sentry can critically strike and benefits from Aphelios' attack speed and critical strike chance.", 'leveling': []}], 'cost': {'modifiers': [{'values': [10, 10, 10, 10, 10], 'units': [' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight', ' Moonlight']}, {'values': [60, 60, 60, 60, 60], 'units': ['', '', '', '', '']}]}, 'cooldown': {'modifiers': [{'values': [9.0, 8.823529411764707, 8.647058823529411, 8.470588235294118, 8.294117647058824, 8.117647058823529, 7.9411764705882355, 7.764705882352941, 7.588235294117647, 7.411764705882353, 7.235294117647059, 7.0588235294117645, 6.882352941176471, 6.705882352941176, 6.529411764705882, 6.352941176470588, 6.1764705882352935, 6.0], 'units': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']}], 'affectedByCdr': True}, 'targeting': 'Auto-targeted', 'affects': 'Enemies', 'spellshieldable': None, 'resource': 'MANA', 'damageType': 'PHYSICAL_DAMAGE', 'spellEffects': 'Pet', 'projectile': 'SPECIAL', 'onHitEffects': None, 'occurrence': None, 'notes': "Sentry's name is modified based on Aphelios' off-hand weapon:\n  Precision Sentry\n  Resurgent Sentry\n  Heals Aphelios for any damage it deals.\n\n  Binding Sentry\n  Incendiary Sentry", 'blurb': 'Active:  Aphelios deploys lunar sentry that uses his off-hand weapon. It attacks nearby enemies dealing physical damage.', 'missileSpeed': None, 'rechargeRate': None, 'collisionRadius': None, 'tetherRadius': None, 'onTargetCdStatic': None, 'innerRadius': None, 'speed': None, 'width': None, 'angle': None, 'castTime': None, 'effectRadius': '575', 'targetRange': '475'}]
'''


'''
[{'name': 'Orb of Deception', 
'icon': 'http://raw.communitydragon.org/latest/game/assets/characters/ahri/hud/icons2d/ahri_orbofdeception.png', 
'effects': [{'description': 
            'Passive: Ability hits grant an Essence Theft stack, up to a maximum of 3 per cast. At a maximum of 9 stacks, the next Orb of Deception consumes them all to heal Ahri for 3 / 5 / 9 / 18 (based on level) (+ 9% AP) every time an enemy is hit. Essence Theft is not stacked within the same instance.', 
            'leveling': []}, 
            {'description': 'Active: Ahri sends an orb of arcane energy in the target direction, dealing magic damage to all enemies it passes through. At maximum range, it homes back to Ahri, dealing true damage instead.', 
            'leveling': [{'attribute': 'Damage Per Pass', 
                        'modifiers': [{'values': [40, 65, 90, 115, 140], 
                                        'units': ['', '', '', '', '']}, 
                        {'values': [35, 35, 35, 35, 35], 
                        'units': ['% AP', '% AP', '% AP', '% AP', '% AP']}]}, 
            {'attribute': 'Total Mixed Damage', 
            'modifiers': [{'values': [80, 130, 180, 230, 280], 
                            'units': ['', '', '', '', '']}, 
                            {'values': [70, 70, 70, 70, 70], 
                            'units': ['% AP', '% AP', '% AP', '% AP', '% AP']}]}]}], 
            'cost': {'modifiers': [{'values': [65, 70, 75, 80, 85], 
                         'units': ['', '', '', '', '']}]}, 
            'cooldown': {'modifiers': [{'values': [7, 7, 7, 7, 7], 'units': ['', '', '', '', '']}], 'affectedByCdr': True}, 'targeting': 'Direction', 'affects': 'Enemies', 'spellshieldable': 'Special', 'resource': 'MANA', 'damageType': 'MIXED_DAMAGE', 'spellEffects': 'Area of effect', 'projectile': 'TRUE', 'onHitEffects': None, 'occurrence': None, 'notes': "Orb of Deception functions normally during flight regardless of Ahri's condition.\n Each pass of the projectile can only damage an enemy once.\n If Ahri is performing an attack animation when the orb switches direction, the attack animation is canceled.\n  Flash can be cast during the cast time of the ability.", 'blurb': 'Active:  Ahri sends out and pulls back her orb, dealing  magic damage on the way out and  true damage on the way back.', 'missileSpeed': None, 'rechargeRate': None, 'collisionRadius': None, 'tetherRadius': None, 'onTargetCdStatic': None, 'innerRadius': None, 'speed': '1700', 'width': '180', 'angle': None, 'castTime': None, 'effectRadius': None, 'targetRange': '880'}]'''

###All the abilities and the passive of a champ
'''"abilities": {
      "P": [
        {
          "name": "Vastayan Grace",
          "icon": "http://raw.communitydragon.org/latest/game/assets/characters/ahri/hud/icons2d/ahri_charm.png",
          "effects": [
            {
              "description": "Innate: Whenever Ahri lands 2 ability hits against a champion within 1.5 seconds, she gains 20% bonus movement speed for 3 seconds.",
              "leveling": []
            }
          ],
          "cost": null,
          "cooldown": {
            "modifiers": [
              {
                "values": [
                  9,
                  9,
                  9
                ],
                "units": [
                  "",
                  "",
                  ""
                ]
              }
            ],
            "affectedByCdr": false
          },
          "targeting": "Passive",
          "affects": "Self",
          "spellshieldable": null,
          "resource": null,
          "damageType": null,
          "spellEffects": null,
          "projectile": null,
          "onHitEffects": null,
          "occurrence": null,
          "notes": "No additional details.",
          "blurb": "Innate: Whenever  Ahri lands 2 ability hits on  champions within a short period, she briefly gains  bonus movement speed.",
          "missileSpeed": null,
          "rechargeRate": null,
          "collisionRadius": null,
          "tetherRadius": null,
          "onTargetCdStatic": null,
          "innerRadius": null,
          "speed": null,
          "width": null,
          "angle": null,
          "castTime": null,
          "effectRadius": null,
          "targetRange": null
        }
      ],
      "Q": [
        {
          "name": "Orb of Deception",
          "icon": "http://raw.communitydragon.org/latest/game/assets/characters/ahri/hud/icons2d/ahri_orbofdeception.png",
          "effects": [
            {
              "description": "Passive: Ability hits grant an Essence Theft stack, up to a maximum of 3 per cast. At a maximum of 9 stacks, the next Orb of Deception consumes them all to heal Ahri for 3 / 5 / 9 / 18 (based on level) (+ 9% AP) every time an enemy is hit. Essence Theft is not stacked within the same instance.",
              "leveling": []
            },
            {
              "description": "Active: Ahri sends an orb of arcane energy in the target direction, dealing magic damage to all enemies it passes through. At maximum range, it homes back to Ahri, dealing true damage instead.",
              "leveling": [
                {
                  "attribute": "Damage Per Pass",
                  "modifiers": [
                    {
                      "values": [
                        40,
                        65,
                        90,
                        115,
                        140
                      ],
                      "units": [
                        "",
                        "",
                        "",
                        "",
                        ""
                      ]
                    },
                    {
                      "values": [
                        35,
                        35,
                        35,
                        35,
                        35
                      ],
                      "units": [
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP"
                      ]
                    }
                  ]
                },
                {
                  "attribute": "Total Mixed Damage",
                  "modifiers": [
                    {
                      "values": [
                        80,
                        130,
                        180,
                        230,
                        280
                      ],
                      "units": [
                        "",
                        "",
                        "",
                        "",
                        ""
                      ]
                    },
                    {
                      "values": [
                        70,
                        70,
                        70,
                        70,
                        70
                      ],
                      "units": [
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP"
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "cost": {
            "modifiers": [
              {
                "values": [
                  65,
                  70,
                  75,
                  80,
                  85
                ],
                "units": [
                  "",
                  "",
                  "",
                  "",
                  ""
                ]
              }
            ]
          },
          "cooldown": {
            "modifiers": [
              {
                "values": [
                  7,
                  7,
                  7,
                  7,
                  7
                ],
                "units": [
                  "",
                  "",
                  "",
                  "",
                  ""
                ]
              }
            ],
            "affectedByCdr": true
          },
          "targeting": "Direction",
          "affects": "Enemies",
          "spellshieldable": "Special",
          "resource": "MANA",
          "damageType": "MIXED_DAMAGE",
          "spellEffects": "Area of effect",
          "projectile": "TRUE",
          "onHitEffects": null,
          "occurrence": null,
          "notes": "Orb of Deception functions normally during flight regardless of Ahri's condition.\n Each pass of the projectile can only damage an enemy once.\n If Ahri is performing an attack animation when the orb switches direction, the attack animation is canceled.\n  Flash can be cast during the cast time of the ability.",
          "blurb": "Active:  Ahri sends out and pulls back her orb, dealing  magic damage on the way out and  true damage on the way back.",
          "missileSpeed": null,
          "rechargeRate": null,
          "collisionRadius": null,
          "tetherRadius": null,
          "onTargetCdStatic": null,
          "innerRadius": null,
          "speed": "1700",
          "width": "180",
          "angle": null,
          "castTime": null,
          "effectRadius": null,
          "targetRange": "880"
        }
      ],
      "W": [
        {
          "name": "Fox-Fire",
          "icon": "http://raw.communitydragon.org/latest/game/assets/characters/ahri/hud/icons2d/ahri_foxfire.png",
          "effects": [
            {
              "description": "Active: Ahri summons three spectral flames which orbit her for up to 5 seconds.",
              "leveling": []
            },
            {
              "description": "Flames prioritize champions hit by Charm, then the target of Ahri's last basic attack within 3 seconds.",
              "leveling": []
            },
            {
              "description": "After 0.25 seconds, each flame targets a visible prioritized enemy; or after 0.4 seconds targets the closest visible enemy in range, prioritizing champions, dealing magic damage.",
              "leveling": [
                {
                  "attribute": "Magic Damage",
                  "modifiers": [
                    {
                      "values": [
                        40,
                        65,
                        90,
                        115,
                        140
                      ],
                      "units": [
                        "",
                        "",
                        "",
                        "",
                        ""
                      ]
                    },
                    {
                      "values": [
                        30,
                        30,
                        30,
                        30,
                        30
                      ],
                      "units": [
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP"
                      ]
                    }
                  ]
                }
              ]
            },
            {
              "description": "Subsequent flames on a target deal 30% damage.",
              "leveling": [
                {
                  "attribute": "Additional Magic Damage",
                  "modifiers": [
                    {
                      "values": [
                        12,
                        19.5,
                        27,
                        34.5,
                        42
                      ],
                      "units": [
                        "",
                        "",
                        "",
                        "",
                        ""
                      ]
                    },
                    {
                      "values": [
                        9,
                        9,
                        9,
                        9,
                        9
                      ],
                      "units": [
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP"
                      ]
                    }
                  ]
                },
                {
                  "attribute": "Total Single Target Damage",
                  "modifiers": [
                    {
                      "values": [
                        64,
                        104,
                        144,
                        184,
                        224
                      ],
                      "units": [
                        "",
                        "",
                        "",
                        "",
                        ""
                      ]
                    },
                    {
                      "values": [
                        48,
                        48,
                        48,
                        48,
                        48
                      ],
                      "units": [
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP"
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "cost": {
            "modifiers": [
              {
                "values": [
                  40,
                  40,
                  40,
                  40,
                  40
                ],
                "units": [
                  "",
                  "",
                  "",
                  "",
                  ""
                ]
              }
            ]
          },
          "cooldown": {
            "modifiers": [
              {
                "values": [
                  9,
                  8,
                  7,
                  6,
                  5
                ],
                "units": [
                  "",
                  "",
                  "",
                  "",
                  ""
                ]
              }
            ],
            "affectedByCdr": true
          },
          "targeting": "None",
          "affects": "Enemies",
          "spellshieldable": "True",
          "resource": "MANA",
          "damageType": "MAGIC_DAMAGE",
          "spellEffects": "Single target",
          "projectile": "TRUE",
          "onHitEffects": null,
          "occurrence": null,
          "notes": "Each missile of Fox-Fire has its own shorter non-priority range.\n Once locked-on, the missiles will pursue even if Ahri loses sight.\n If the target of Fox-Fire dies, the missile will fizzle.\n Any unused Fox-Fires will fizzle upon death.\n If Ahri uses  Zhonya's Hourglass while Fox-Fire is active, any orbs that have not acquired a target will fizzle.\n The cooldown of Fox-Fire begin once all the orbs have acquired a target or timed-out.",
          "blurb": "Active:  Ahri releases three fox-fires, that lock onto nearby enemies, dealing  magic damage to them. They prioritize her main target.",
          "missileSpeed": null,
          "rechargeRate": null,
          "collisionRadius": null,
          "tetherRadius": null,
          "onTargetCdStatic": null,
          "innerRadius": null,
          "speed": null,
          "width": null,
          "angle": null,
          "castTime": "false",
          "effectRadius": "700 / 725",
          "targetRange": null
        }
      ],
      "E": [
        {
          "name": "Charm",
          "icon": "http://raw.communitydragon.org/latest/game/assets/characters/ahri/hud/icons2d/ahri_charm.png",
          "effects": [
            {
              "description": "Active: Ahri blows a kiss in the target direction that deals magic damage to the first enemy hit, knocking down, charming and slowing them by 65%.",
              "leveling": [
                {
                  "attribute": "Magic damage",
                  "modifiers": [
                    {
                      "values": [
                        60,
                        90,
                        120,
                        150,
                        180
                      ],
                      "units": [
                        "",
                        "",
                        "",
                        "",
                        ""
                      ]
                    },
                    {
                      "values": [
                        40,
                        40,
                        40,
                        40,
                        40
                      ],
                      "units": [
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP",
                        "% AP"
                      ]
                    }
                  ]
                },
                {
                  "attribute": "Charm Duration",
                  "modifiers": [
                    {
                      "values": [
                        1.4,
                        1.55,
                        1.7,
                        1.85,
                        2
                      ],
                      "units": [
                        "",
                        "",
                        "",
                        "",
                        ""
                      ]
                    }
                  ]
                }
              ]
            },
            {
              "description": "An enemy hit by Charm is vulnerable for 3 seconds, taking 20% bonus damage from Ahri's abilities.",
              "leveling": []
            }
          ],
          "cost": {
            "modifiers": [
              {
                "values": [
                  70,
                  70,
                  70,
                  70,
                  70
                ],
                "units": [
                  "",
                  "",
                  "",
                  "",
                  ""
                ]
              }
            ]
          },
          "cooldown": {
            "modifiers": [
              {
                "values": [
                  12,
                  12,
                  12,
                  12,
                  12
                ],
                "units": [
                  "",
                  "",
                  "",
                  "",
                  ""
                ]
              }
            ],
            "affectedByCdr": true
          },
          "targeting": "Direction",
          "affects": "Enemies",
          "spellshieldable": "True",
          "resource": "MANA",
          "damageType": "MAGIC_DAMAGE",
          "spellEffects": "spell",
          "projectile": "TRUE",
          "onHitEffects": null,
          "occurrence": null,
          "notes": "The damage amplification also affects the true damage portion of  Orb of Deception.\n If the charmed enemy does not have  sight of Ahri they will stand still for its duration.\n The effect ends prematurely if Ahri dies.\n  Flash can be cast during the cast animation of Charm.",
          "blurb": "Active:  Ahri blows a kiss that deals  magic damage and  charms an enemy it encounters, instantly  stopping movement abilities and causing them to walk harmlessly towards her. Additionally, the target temporarily takes increased damage from her.",
          "missileSpeed": null,
          "rechargeRate": null,
          "collisionRadius": null,
          "tetherRadius": null,
          "onTargetCdStatic": null,
          "innerRadius": null,
          "speed": "1600",
          "width": "100",
          "angle": null,
          "castTime": null,
          "effectRadius": null,
          "targetRange": "975"
        }
      ],
      "R": [
        {
          "name": "Spirit Rush",
          "icon": "http://raw.communitydragon.org/latest/game/assets/characters/ahri/hud/icons2d/ahri_spiritrush.png",
          "effects": [
            {
              "description": "Active: Ahri dashes in the target direction and then fires energy bolts to up to 3 visible targets, dealing magic damage. Spirit Rush can be recast twice more at a 1 second static cooldown within 10 seconds of activation at no additional cost.",
              "leveling": [
                {
                  "attribute": "Magic damage",
                  "modifiers": [
                    {
                      "values": [
                        60,
                        90,
                        120
                      ],
                      "units": [
                        "",
                        "",
                        ""
                      ]
                    },
                    {
                      "values": [
                        35,
                        35,
                        35
                      ],
                      "units": [
                        "% AP",
                        "% AP",
                        "% AP"
                      ]
                    }
                  ]
                }
              ]
            },
            {
              "description": "Recast: Ahri dashes, mimicking the first cast's effects.",
              "leveling": [
                {
                  "attribute": "Maximum single target damage",
                  "modifiers": [
                    {
                      "values": [
                        180,
                        270,
                        360
                      ],
                      "units": [
                        "",
                        "",
                        ""
                      ]
                    },
                    {
                      "values": [
                        105,
                        105,
                        105
                      ],
                      "units": [
                        "% AP",
                        "% AP",
                        "% AP"
                      ]
                    }
                  ]
                },
                {
                  "attribute": "Maximum damage",
                  "modifiers": [
                    {
                      "values": [
                        540,
                        810,
                        1080
                      ],
                      "units": [
                        "",
                        "",
                        ""
                      ]
                    },
                    {
                      "values": [
                        315,
                        315,
                        315
                      ],
                      "units": [
                        "% AP",
                        "% AP",
                        "% AP"
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "cost": {
            "modifiers": [
              {
                "values": [
                  100,
                  100,
                  100
                ],
                "units": [
                  "",
                  "",
                  ""
                ]
              }
            ]
          },
          "cooldown": {
            "modifiers": [
              {
                "values": [
                  130,
                  105,
                  80
                ],
                "units": [
                  "",
                  "",
                  ""
                ]
              }
            ],
            "affectedByCdr": true
          },
          "targeting": "Direction",
          "affects": "Enemies",
          "spellshieldable": "True",
          "resource": "MANA",
          "damageType": "MAGIC_DAMAGE",
          "spellEffects": "Spell",
          "projectile": "TRUE",
          "onHitEffects": null,
          "occurrence": null,
          "notes": "Each cast counts as an ability activation for the purposes of on-cast effects such as Spellblade, charging  Spellbinder, and stacking  Force Pulse.\n Spirit Rush uses quick cast by default.\n There's a slight delay before a champion gains vision of the fog of war once inside it. Because of this, if Ahri dashes into it, it is possible that Spirit Rush will not target any enemy in range.\n If Ahri dies mid-dash, she will not fire the bolts.",
          "blurb": "Active:  Ahri  dashes forward and fires essence bolts, dealing  magic damage to nearby enemies. The ability can be cast up to three times before going on cooldown.",
          "missileSpeed": null,
          "rechargeRate": null,
          "collisionRadius": null,
          "tetherRadius": null,
          "onTargetCdStatic": null,
          "innerRadius": null,
          "speed": null,
          "width": null,
          "angle": null,
          "castTime": null,
          "effectRadius": "600",
          "targetRange": "450"
        }
      ]
    },'''

###Method 1 to get spells:
'''
championInformation = pd.DataFrame()
for champ in champs['data']:
    with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/" + latestPatch + "/data/en_US/champion/" + champ + ".json") as url:
        champions = json.loads(url.read().decode())
        #print(champ['data'])

        ###Get essential information
        champSpells = champions['data'][champ]['spells']
        #print(champ)

        ###Dataframe with champions with the spells
        oneChamp = {'champion',
                     'name',
                     'cooldown',
                     'effect'}
        oneChamp = pd.DataFrame(columns=oneChamp)

        for spells in champSpells:
            #print("Name: " + str(spells['name']))
            #print("cooldown: " + str(spells['cooldown']))
            #print("Effect: " + str(spells['effectBurn']))
            #print(" ")

            ###Spells
            spell = {'champion': champ,
                     'name': spells['name']}

            spell = pd.DataFrame(spell, index=[0])

            ###Damage, other information of the spells
            effect = pd.DataFrame({'effect': [spells['effectBurn']]}, index=[0])

            ###Cooldown of the spells
            coolDown = pd.DataFrame({'cooldown': [spells['cooldown']]}, index=[0])

            ###Merge
            spellData = pd.concat([spell, effect, coolDown], axis=1).reindex(spell.index)

            oneChamp = oneChamp.append(spellData)
            #print(oneChamp)
        #print(champSpells)
        #print(champions['data'][champ]['passive'])

        #passive = {'passive': champions['data'][champ]['passive']}
        #passive = pd.DataFrame(passive, index=[0])
        #champInfo = pd.concat([oneChamp, passive], axis=1).reindex(oneChamp.index)
        championInformation = championInformation.append(oneChamp)

print("hi")

'''

''' 
{"type":"champion",
"format":"standAloneComplex",
"version":"10.8.1",
"data":{"Ahri": 
    {"id":"Ahri",
    "key":"103",
    "name":"Ahri",
    "title":"the Nine-Tailed Fox",
    "image":{"full":"Ahri.png",
            "sprite":"champion0.png",
            "group":"champion",
            "x":48,"y":0,"w":48,"h":48},
    "skins":[{"id":"103000","num":0,"name":"default","chromas":false},{"id":"103001","num":1,"name":"Dynasty Ahri","chromas":false},{"id":"103002","num":2,"name":"Midnight Ahri","chromas":false},{"id":"103003","num":3,"name":"Foxfire Ahri","chromas":false},{"id":"103004","num":4,"name":"Popstar Ahri","chromas":true},{"id":"103005","num":5,"name":"Challenger Ahri","chromas":true},{"id":"103006","num":6,"name":"Academy Ahri","chromas":false},{"id":"103007","num":7,"name":"Arcade Ahri","chromas":false},{"id":"103014","num":14,"name":"Star Guardian Ahri","chromas":false},{"id":"103015","num":15,"name":"K/DA Ahri","chromas":false},{"id":"103016","num":16,"name":"K/DA Ahri Prestige Edition","chromas":false},{"id":"103017","num":17,"name":"Elderwood Ahri","chromas":true}],
    "lore":"Innately connected to the latent power of Runeterra, Ahri is a vastaya who can reshape magic into orbs of raw energy. She revels in toying with her prey by manipulating their emotions before devouring their life essence. Despite her predatory nature, Ahri retains a sense of empathy as she receives flashes of memory from each soul she consumes.","blurb":"Innately connected to the latent power of Runeterra, Ahri is a vastaya who can reshape magic into orbs of raw energy. She revels in toying with her prey by manipulating their emotions before devouring their life essence. Despite her predatory nature...",
    "allytips":["Use Charm to set up your combos, it will make landing Orb of Deception and Fox-Fire dramatically easier.","Initiate team fights using Charm, and chase down stragglers with Spirit Rush.","Spirit Rush enables Ahri's abilities, it opens up paths for Charm, helps double hitting with Orb of Deception, and closes to make use of Fox-Fire."],"enemytips":["Ahri's survivability is dramatically reduced when her Ultimate, Spirit Rush, is down.","Stay behind minions to make Charm difficult to land, this will reduce Ahri's damage potential significantly."],
    "tags":["Mage","Assassin"],
    "partype":"Mana",
    "info":{"attack":3,"defense":4,"magic":8,"difficulty":5},
    "stats":{"hp":526,"hpperlevel":92,"mp":418,"mpperlevel":25,"movespeed":330,"armor":20.88,"armorperlevel":3.5,"spellblock":30,"spellblockperlevel":0.5,"attackrange":550,"hpregen":6.5,"hpregenperlevel":0.6,"mpregen":8,"mpregenperlevel":0.8,"crit":0,"critperlevel":0,"attackdamage":53.04,"attackdamageperlevel":3,"attackspeedperlevel":2,"attackspeed":0.668},
    "spells":[{"id":"AhriOrbofDeception",
                "name":"Orb of Deception",
                "description":"Ahri sends out and pulls back her orb, dealing magic damage on the way out and true damage on the way back. After earning several spell hits, Ahri's next orb hits will restore her health.",
                "tooltip":"Deals {{ e1 }} <scaleAP>(+{{ a1 }})</scaleAP> magic damage on the way out, and {{ e1 }} <scaleAP>(+{{ a1 }})</scaleAP> true damage on the way back.<br /><br />Ahri's abilities generate Essence Theft stacks when they hit enemies (max {{ f4.0 }} per cast). At {{ f3.0 }} stacks, Ahri's next Orb of Deception that lands a hit will restore <scaleLevel>{{ f1.0 }}</scaleLevel> <scaleAP>(+{{ f2.-1 }})</scaleAP> health for each enemy hit.",
                "leveltip":{"label":["Damage","@AbilityResourceName@ Cost"],
                            "effect":["{{ e1 }} -> {{ e1NL }}","{{ cost }} -> {{ costNL }}"]},
                "maxrank":5,
                "cooldown":[7,7,7,7,7],
                "cooldownBurn":"7",
                "cost":[65,70,75,80,85],
                "costBurn":"65/70/75/80/85",
                "datavalues":{},
                "effect":[null,[40,65,90,115,140],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
                "effectBurn":[null,"40/65/90/115/140","0","0","0","0","0","0","0","0","0"],
                "vars":[{"link":"spelldamage","coeff":0.35,"key":"a1"},
                        {"link":"spelldamage","coeff":0.35,"key":"a1"}],
                "costType":" {{ abilityresourcename }}",
                "maxammo":"-1",
                "range":[880,880,880,880,880],
                "rangeBurn":"880",
                "image":{"full":"AhriOrbofDeception.png",
                "sprite":"spell0.png",
                "group":"spell","x":384,"y":48,"w":48,"h":48},
                "resource":"{{ cost }} {{ abilityresourcename }}"},

                {"id":"AhriFoxFire",
                "name":"Fox-Fire",
                "description":"Ahri releases three fox-fires, that lock onto and attack nearby enemies.",
                "tooltip":"Releases fox-fires that seek nearby enemies and deal {{ e1 }} <scaleAP>(+{{ a1 }})</scaleAP> magic damage.<br /><br />Enemies hit with multiple fox-fires take {{ e2 }}% damage from each additional fox-fire beyond the first, for a maximum of <scaleAP>{{ f1 }}</scaleAP> damage to a single enemy.<br /><br /><rules>Fox-fire prioritizes champions recently hit by Charm, then enemies Ahri recently attacked.<br />If Fox-fire cannot find a priority target, it targets champions over the nearest enemy if possible.</rules>",
                "leveltip":{"label":["Damage","Cooldown"],
                            "effect":["{{ e1 }} -> {{ e1NL }}","{{ cooldown }} -> {{ cooldownNL }}"]},
                "maxrank":5,
                "cooldown":[9,8,7,6,5],
                "cooldownBurn":"9/8/7/6/5",
                "cost":[40,40,40,40,40],
                "costBurn":"40",
                "datavalues":{},
                "effect":[null,[40,65,90,115,140],[30,30,30,30,30],[0.25,0.25,0.25,0.25,0.25],[150,150,150,150,150],[550,550,550,550,550],[5,5,5,5,5],[0.4,0.4,0.4,0.4,0.4],[725,725,725,725,725],[0,0,0,0,0],[0,0,0,0,0]],
                "effectBurn":[null,
                            "40/65/90/115/140",
                            "30",
                            "0.25",
                            "150",
                            "550",
                            "5",
                            "0.4",
                            "725",
                            "0",
                            "0"],
                "vars":[{"link":"spelldamage",
                        "coeff":0.3,
                        "key":"a1"}],
                "costType":" {{ abilityresourcename }}",
                "maxammo":"-1",
                "range":[700,700,700,700,700],
                "rangeBurn":"700",
                "image":{"full":"AhriFoxFire.png","sprite":"spell0.png","group":"spell","x":432,"y":48,"w":48,"h":48},
                "resource":"{{ cost }} {{ abilityresourcename }}"},
                {"id":"AhriSeduce",
                "name":"Charm",
                "description":"Ahri blows a kiss that damages and charms an enemy it encounters, instantly stopping movement abilities and causing them to walk harmlessly towards her. The target temporarily takes increased damage from Ahri.",
                "tooltip":"Blows a kiss that deals {{ e1 }} <scaleAP>(+{{ a1 }})</scaleAP> magic damage and charms the first enemy hit, causing them to walk harmlessly towards Ahri for {{ e2 }} second(s) and immediately stopping any in-progress movement abilities.<br /><br />Enemies hit by Charm become vulnerable for {{ e5 }} seconds, taking {{ e4 }}% more damage from Ahri's abilities.",
                "leveltip":{"label":["Damage","Duration"],
                            "effect":["{{ e1 }} -> {{ e1NL }}","{{ e2 }} -> {{ e2NL }}"]},
                "maxrank":5,"cooldown":[12,12,12,12,12],
                "cooldownBurn":"12",
                "cost":[70,70,70,70,70],
                "costBurn":"70",
                "datavalues":{},
                "effect":[null,
                        [60,90,120,150,180],
                        [1.4,1.55,1.7,1.85,2],
                        [-0.65,-0.65,-0.65,-0.65,-0.65],
                        [20,20,20,20,20],
                        [3,3,3,3,3],
                        [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
                "effectBurn":[null,
                            "60/90/120/150/180",
                            "1.4/1.55/1.7/1.85/2",
                            "-0.65",
                            "20",
                            "3",
                            "0",
                            "0",
                            "0",
                            "0",
                            "0"],
                "vars":[{"link":"spelldamage","coeff":0.4,"key":"a1"}],
                "costType":" {{ abilityresourcename }}",
                "maxammo":"-1","range":[975,975,975,975,975],
                "rangeBurn":"975",
                "image":{"full":"AhriSeduce.png","sprite":"spell0.png","group":"spell","x":0,"y":96,"w":48,"h":48},
                "resource":"{{ cost }} {{ abilityresourcename }}"},

                {"id":"AhriTumble",
                "name":"Spirit Rush",
                "description":"Ahri dashes forward and fires essence bolts, damaging nearby enemies. Spirit Rush can be cast up to three times before going on cooldown.",
                "tooltip":"Nimbly dashes forward firing {{ rmaxtargetspercast }} essence bolts at nearby enemies (prioritizing champions) dealing {{ rcalculateddamage }} magic damage.<br /><br />Can be cast up to {{ rmaxcasts }} times within {{ rrecastwindow }} seconds before going on cooldown.",
                "leveltip":{"label":["Damage","Cooldown"],
                            "effect":["{{ rbasedamage }} -> {{ rbasedamageNL }}","{{ cooldown }} -> {{ cooldownNL }}"]},
                "maxrank":3,
                "cooldown":[130,105,80],
                "cooldownBurn":"130/105/80",
                "cost":[100,100,100],
                "costBurn":"100",
                "datavalues":{},
                "effect":[null,
                        [0,0,0],
                        [0,0,0],
                        [0,0,0],
                        [0,0,0],
                        [0,0,0],
                        [0,0,0],
                        [0,0,0],
                        [1,1,1],
                        [0,0,0],
                        [0,0,0]],
                "effectBurn":[null,"0","0","0","0","0","0","0","1","0","0"],
                "vars":[],
                "costType":" {{ abilityresourcename }}",
                "maxammo":"-1",
                "range":[450,450,450],
                "rangeBurn":"450",
                "image":{"full":"AhriTumble.png","sprite":"spell0.png","group":"spell","x":48,"y":96,"w":48,"h":48},
                "resource":"{{ cost }} {{ abilityresourcename }}"}],
    "passive":{"name":"Vastayan Grace",
                "description":"Whenever Ahri's spells hit a champion 2 times within a short period, she briefly gains movement speed.",
                "image": {"full":"Ahri_SoulEater2.png","sprite":"passive0.png","group":"passive","x":48,"y":0,"w":48,"h":48}}'''




'''First json with all the information of the champions'''
''' 
{"type":"champion","format":"standAloneComplex","version":"10.8.1","data":
    {"Aatrox":{"version":"10.8.1",
               "id":"Aatrox",
               "key":"266",
               "name":"Aatrox",
               "title":"the Darkin Blade",
               "blurb":"Once honored defenders of Shurima against the Void, Aatrox and his brethren would eventually become an even greater threat to Runeterra, and were defeated only by cunning mortal sorcery. But after centuries of imprisonment, Aatrox was the first to find...",
               "info":{"attack":8,"defense":4,"magic":3,"difficulty":4},
               "image":{"full":"Aatrox.png","sprite":"champion0.png","group":"champion","x":0,"y":0,"w":48,"h":48},
               "tags":["Fighter","Tank"],"partype":"Blood Well",
               "stats":{"hp":580,"hpperlevel":90,"mp":0,"mpperlevel":0,"movespeed":345,"armor":38,"armorperlevel":3.25,"spellblock":32.1,"spellblockperlevel":1.25,"attackrange":175,"hpregen":3,"hpregenperlevel":1,"mpregen":0,"mpregenperlevel":0,"crit":0,"critperlevel":0,"attackdamage":60,"attackdamageperlevel":5,"attackspeedperlevel":2.5,"attackspeed":0.651}},

     "Ahri":{"version":"10.8.1",
             "id":"Ahri",
             "key":"103",
             "name":"Ahri",
             "title":"the Nine-Tailed Fox",
             "blurb":"Innately connected to the latent power of Runeterra, Ahri is a vastaya who can reshape magic into orbs of raw energy. She revels in toying with her prey by manipulating their emotions before devouring their life essence. Despite her predatory nature...","info":{"attack":3,"defense":4,"magic":8,"difficulty":5},
             "image":{"full":"Ahri.png","sprite":"champion0.png","group":"champion","x":48,"y":0,"w":48,"h":48},
             "tags":["Mage","Assassin"],"partype":"Mana",
             "stats":{"hp":526,"hpperlevel":92,"mp":418,"mpperlevel":25,"movespeed":330,"armor":20.88,"armorperlevel":3.5,"spellblock":30,"spellblockperlevel":0.5,"attackrange":550,"hpregen":6.5,"hpregenperlevel":0.6,"mpregen":8,"mpregenperlevel":0.8,"crit":0,"critperlevel":0,"attackdamage":53.04,"attackdamageperlevel":3,"attackspeedperlevel":2,"attackspeed":0.668}}}}
'''
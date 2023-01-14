# -*- encoding: utf-8 -*-
'''
@File    :   equipment.py
@Time    :   2022/12/26 11:41:56
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   
'''

import sys
import os
sys.path.append(os.path.abspath('./'))

import random,time
from enum import Enum 
from models.effect import Effect



class Qaulity(Enum):
    Trash = 0
    Poor = 1
    Common = 2
    Uncommon = 3
    Rare = 4
    Epic = 5
    Legendary = 6
    Heirloom = 7 
    Quest = 10
    Undefined = 11
    
class QaulityColor(Enum):
    Trash = "#808080"
    Poor = "#C0C0C0"
    Common = "#FFFFFF"
    Uncommon = "#00FF00"
    Rare = "#4169E1"
    Epic = "#9932CC"
    Legendary = "#FF8C00"
    Heirloom = "#D2B48C"
    Quest = "#F08080"
    Undefined = "#2F4F4F"
    
class EquipmentType(Enum):
    Helmet=0
    Breastplate=1
    Legarmor=2
    Armarmor=3
    Pauldrons=4 #肩甲
    Gloves=5
    Belt=6
    Cloak=7
    Shoe=8
    Accessorie1=9
    Accessorie2=10
    Ring1=11
    Ring2=12
    
    Mainweapon=13
    Offhandweapon=14
    Twohandweapon=15
    Ammunition=16  #弹药
    
    Robe=17
    Underwear=18
    
    
    
class Value:
    def __init__(self):
        self.value={
            
        }
        self.type=None 
        self.attack=0
        self.phisic_defense=0
        self.magic_defense=0
        
        # attrabute
        self.strength = 0
        self.intelligence = 0
        self.dexterity = 0
        self.vitality = 0
        self.psyche = 0
        self.agility = 0
        self.accuracy = 0
        
        #health
        self.health = 0
        self.health_percent = 0
        self.health_recovery = 0
        self.health_absorb=0
        
        
        #magic
        self.mana = 0
        self.mana_percent=0
        self.mana_recovery=0
        self.mana_absorb=0
        
        #other
        self.attack_speed=0
        self.mobility=0
        
    

class Equipment:
    def __init__(self):
        self.describe=""
        self.name=""
        self.quality=Qaulity.Undefined
        self.icon=""
        self.value=Value()
        self.effect=Effect()
        
        
        
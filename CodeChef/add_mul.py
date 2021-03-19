# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:03:12 2020

@author: Ritul Singh
"""
# Runner.prototype.gameOver = function() {console.log("TechSpartan")}
n = int(input())
if n%2 == 0:
    if n >= 2 and n <= 5:
        print("Not Weird")
    if n >= 6 and n <= 20:
        print("Weird")
    if n > 20:
        print("Not Weird")
if n%2 != 0:
    print("Weird")

        





core(dice):
       37     # You need to write this method
       ~  38     total = 0
       +  39     # Look for tripplets
       +  40     for i in range(1,7):
           +  41         if dice.count(i) >= 3:
               +  42             dice.remove(i)
               +  43             dice.remove(i)
               +  44             dice.remove(i)
               +  45             if i == 1:
                   +  46                 total += 1000
                   +  47             else:
                       +  48                 total += 100 * i
                          49
                          +  50     # Add up extras
                          +  51     for die in dice:
                              +  52         if die == 1:
                                  +  53             total += 100
                                  +  54         if die == 5:
                                      +  55             total += 50
                                      +  56     return total

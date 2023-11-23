import re

a = '''Load Average
 Slot  Status  1-Min  5-Min 15-Min
  RP0 Healthy   1.58   1.90   1.96

Memory (kB)
 Slot  Status    Total     Used (Pct)     Free (Pct) Committed (Pct)
  RP0 Healthy  3987564  2767664 (69%)  1219900 (31%)   3739724 (94%)

CPU Utilization
 Slot  CPU   User System   Nice   Idle    IRQ   SIRQ IOwait
  RP0    0   2.30   3.80   0.00  92.60   0.90   0.40   0.00
         1   2.00   5.00   0.00  91.70   0.90   0.40   0.00
         2  45.24   2.30   0.00  51.85   0.50   0.10   0.00
         3  62.50  18.40   0.00  15.10   3.80   0.20   0.00'''

d = {}
b = a.split("\n")[5]
c = a.split("\n")[6]

Total_mem = c.split(" ")[5]
Used_mem = c.split(" ")[7]
d['Total'] = Total_mem
d['Used'] = Used_mem
print(d)




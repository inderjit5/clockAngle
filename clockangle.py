period = int(input())
longitude = float(())

time = (period/360.0)*longitude
hours=(int(time))
if (hours>12):
    hours=hours-12 
    
minute=(time-hours)*60
hours_angle=(hours+minute/60)*30
minute_angle=(minute/5)*30
angle =abs(hours_angle-minute_angle)
min_angle=min(angle,360-angle)

print("{0:.2f}".formate(min_angle))
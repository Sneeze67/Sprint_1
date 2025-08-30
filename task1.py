str = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0
new_str = str.split(',')
for values in new_str:
    values = values.replace(' ', ',')
    components = values.split(',')
    for component in components:
        if 'h' in component:
            hours = int(component.replace('h',''))
            total_minutes += hours * 60
        elif 'm' in component:
            minutes = int(component.replace('m',''))
            total_minutes += minutes
        elif 's' in component:
            seconds = int(component.replace('s',''))
            total_minutes += seconds / 60
print(int(total_minutes))
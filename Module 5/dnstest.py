from dns import resolver

result = resolver.resolve('ivytech.edu','A')
for ipval in result:
    print('IP',ipval.to_text())


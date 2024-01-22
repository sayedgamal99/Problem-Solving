theset = set()
email = input().strip()
att = email.find('@')
local,domain = email.split('@')
local = local.split('+')[0]
local = local.replace('.','')
final_email = local+'@'+domain
theset.add(final_email)
print(theset)
print(len(theset))


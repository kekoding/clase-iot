# %%
import re

texto = f'''\

+52 811168432
+49-529910199
'''

m = re.search(r"((?<=\+)\d{2})(?: ?-?)(\d+)", texto)

print(f"La lada internacional es {m.group(1)}")

print(f"El teléfono es {m.group(2)}")
# %%

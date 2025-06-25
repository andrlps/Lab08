from model.model import Model

model = Model()
for e in model.listNerc:
    if e.id == 3:
        nerc = e
print(model.worstCase(nerc,4,200))